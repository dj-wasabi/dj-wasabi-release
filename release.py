#!/usr/bin/env python

import os
import sys
import requests
import argparse
import json

currentPath = os.path.dirname(os.path.realpath(__file__))
libraryDir = os.path.join(currentPath, "lib")
sys.path.append(libraryDir)
from djWasabi import djWasabi

try:
    import yaml
except:
    print('Please install: pip install pyyaml')
    sys.exit(1)


def get_args():
    """Support the command-line arguments listed below."""
    parser = argparse.ArgumentParser(description="""This script will create a tag, update where
    needed the CHANGELOG.md and CONTRIBUTORS file and create a release in Github with the provided
    version. Can also provided the latest tag or generate (without commit) a CHANGELOG.md.""")
    parser.add_argument('-c', '--create', required=False, action='store',
                        help='Create a tag and a complete release with provided version.', type=str)
    parser.add_argument('-d', '--docs', required=False, action='store_true',
                        help='Create and/or Update the CHANGELOG.md file.')
    parser.add_argument('-D', '--debug', required=False, action='store_true', help="""Print some
    debug information""")
    parser.add_argument('-l', '--list', required=False, action='store_true',
                        help='Provides the latest created tag in this repository.')
    parser.add_argument('-t', '--token', required=False, action='store',
                        help='The Github API token, or set environment variable "CHANGELOG_GITHUB_TOKEN".', type=str)
    return parser.parse_args()


def updateChangelogMd(command=None, version=None):
    """ Generate and committing the CHANGELOG.md file when it is changed.

    :param command: The command to generate the CHANGELOG.md file.
    :type command: list
    :param version: The version.
    :type version: str
    """
    djWasabi.generic.executeCommand(command=command)
    if version is not None:
        djWasabi.git.commitFile(
            file="CHANGELOG.md",
            message="Updating {f} file for release {v}".format(f="CHANGELOG.md", v=version),
            debug=is_debug
        )


def createUpdateContributerFile(version=None):
    _file = "CONTRIBUTORS"
    if not os.path.isfile(_file):
        touchFile = ["touch", _file]
        djWasabi.generic.executeCommand(command=touchFile)
    createCommand = ["git shortlog -s -n --all --no-merges | awk '{$1=\"\"}1' | sort -u > CONTRIBUTORS"]
    djWasabi.generic.executeCommand(command=createCommand)
    djWasabi.git.commitFile(
        file=_file,
        message="Updating {f} file for release {v}".format(f=_file, v=version),
        debug=is_debug
    )


def generateReleaseDict(version=None):
    _branch = djWasabi.git.getMainBranch()
    myDict = {
        "tag_name": version,
        "target_commitish": _branch,
        "name": version,
        "body": "",
        "draft": False,
        "prerelease": False
    }
    return json.dumps(myDict)


def main():
    global is_debug
    global owner, repository
    args = get_args()
    is_debug = args.debug
    version = args.create
    listTags = args.list
    docs = args.docs

    if not djWasabi.container.validateDockerRunning():
        print('We stop now again')

    print('We stop now')
    sys.exit(1)

    token = djWasabi.config.readOsEnv(key="CHANGELOG_GITHUB_TOKEN")
    headers = {
        "Authorization": 'token {t}'.format(t=token),
        "Accept": "application/vnd.github.v3+json"
    }

    owner, repository = djWasabi.git.readRepository(debug=is_debug)
    githubUrl = djWasabi.generic.getGithubUrl(owner=owner, repository=repository)
    yamlConfig = djWasabi.config.readConfig(rootPath=currentPath)
    dockerCommand = djWasabi.container.createContainerCommand(
        configuration=yamlConfig['changelog'],
        owner=owner, repository=repository
    )

    if version:
        print("We will create a 'release' for tag: {v}".format(v=version))
        if djWasabi.git.getCheckTag(tag=version):
            print("We have already a tag with version: {v}".format(v=version))
            sys.exit(1)

        gitPullCommand = ["git", "pull"]
        djWasabi.generic.executeCommand(command=gitPullCommand)

        gitFetchCommand = ["git", "fetch", "-p"]
        djWasabi.generic.executeCommand(command=gitFetchCommand)

        gitTagCOmmand = ["git", "tag", "-a", version, "-m", version]
        djWasabi.generic.executeCommand(command=gitTagCOmmand)

        gitTagCOmmand = ["git", "push", "--tags"]
        djWasabi.generic.executeCommand(command=gitTagCOmmand)

        # changelog
        updateChangelogMd(command=dockerCommand, version=version)

        # Update Contributors file and create release in Github
        createUpdateContributerFile(version=version)
        githubUrlRelease = "{g}/releases".format(g=githubUrl)
        releaseData = generateReleaseDict(version=version)
        djWasabi.generic.debugLog(
            message="We use {u} to create a release with data: {d}".format(
                u=githubUrlRelease,
                d=releaseData
            ), debug=is_debug)
        djWasabi.request._post(url=githubUrlRelease, data=releaseData, headers=headers)

        # Push the changes.
        gitTagCommand = ["git", "push"]
        djWasabi.generic.executeCommand(command=gitTagCommand)
    elif listTags:
        print("Generating 'CHANGELOG.md' file.")
        print(djWasabi.git.getLatestTag())
    elif docs:
        updateChangelogMd(command=dockerCommand)
    else:
        print('No action done.')


if __name__ == "__main__":
    main()
