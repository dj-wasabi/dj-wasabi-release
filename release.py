#!/usr/bin/env python
"""Will create a tag, update the CHANGELOG.md and CONTRIBUTORS file and create a release in Github with the provided version."""

import os
import sys
import requests
import argparse
import json
import platform

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


def updateChangelogMd(command: list = None, version: str = None):
    """ Generate and committing the CHANGELOG.md file when it is changed.

    :param command: The command to generate the CHANGELOG.md file.
    :type command: list
    :param version: The version.
    :type version: str
    """
    djWasabi.generic.executeCommand(command=command)
    # if version is not None:
    #     djWasabi.git.commitFile(
    #         file="CHANGELOG.md",
    #         message="Updating {f} file for release {v}".format(f="CHANGELOG.md", v=version),
    #         debug=is_debug
    #     )


def createUpdateContributerFile(version: str = None):
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


def generateReleaseDict(version: str = None) -> dict:
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


def updateSphinxDocs(version: str = None):
    """Update the Sphinx release information with provided version.

    :param version: The version.
    :type version: str
    """
    _os = platform.system()
    _command = ["ls -l"]
    _file = "docs/source/conf.py"
    if os.path.isfile(_file):
        if _os == "Darwin":
            _command = "sed -i '' \"s/release = .*$/release = '{v}'/g\" {f}".format(
                v=version, f=_file
            )
        else:
            _command = "sed -i \"s/release = .*$/release = '{v}'/g\" {f}".format(
                v=version, f=_file
            )
        djWasabi.generic.executeCommand(command=_command)
        djWasabi.git.commitFile(
            file=_file,
            message="Updating {f} file for release {v}".format(f=_file, v=version),
            debug=is_debug
        )
    else:
        print("No Sphinx documentation available.")


def main():
    global is_debug
    global owner, repository
    args = get_args()
    is_debug = args.debug
    version = args.create
    listTags = args.list
    docs = args.docs

    if not djWasabi.container.validateDockerRunning():
        print('Docker is not running, we will stop onow.')
        sys.exit(1)

    token = djWasabi.config.readOsEnv(key="CHANGELOG_GITHUB_TOKEN")
    headers = {
        "Authorization": 'token {t}'.format(t=token),
        "Accept": "application/vnd.github.v3+json"
    }

    owner, repository = djWasabi.git.readRepository(debug=is_debug)
    githubUrl = djWasabi.generic.getGithubUrl(owner=owner, repository=repository)
    yamlConfigFile = os.path.join(currentPath, "dj-wasabi.yml")
    yamlConfig = djWasabi.config.readYamlFile(file=yamlConfigFile)
    dockerCommand = djWasabi.container.createContainerCommand(
        configuration=yamlConfig['changelog'],
        owner=owner, repository=repository, version=version
    )

    if version:
        print("We will create a 'release' for tag: {v}".format(v=version))
        if djWasabi.git.getCheckTag(tag=version):
            print("We have already a tag with version: {v}".format(v=version))
            sys.exit(1)

        print('Pulling latest information from Github.')
        gitPullCommand = ["git", "pull"]
        djWasabi.generic.executeCommand(command=gitPullCommand)

        gitFetchCommand = ["git", "fetch", "-p"]
        djWasabi.generic.executeCommand(command=gitFetchCommand)

        print('Updating Sphinx-docs release information if applicable.')
        updateSphinxDocs(version=version)

        print('Creating a tag and push version {v}.'.format(v=version))
        gitTagCOmmand = ["git", "tag", "-a", version, "-m", version]
        djWasabi.generic.executeCommand(command=gitTagCOmmand)

        gitTagCOmmand = ["git", "push", "--tags"]
        djWasabi.generic.executeCommand(command=gitTagCOmmand)

        # changelog
        print('Updating CONTRIBUTORS and CHANGELOG files.')
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
        request = djWasabi.http.request()
        request._post(url=githubUrlRelease, data=releaseData, headers=headers)

        # Push the changes.
        print('Pushing latest changes.')
        gitTagCommand = ["git", "push"]
        djWasabi.generic.executeCommand(command=gitTagCommand)
    elif listTags:
        print(djWasabi.git.getLatestTag())
    elif docs:
        print('Updating CHANGELOG file.')
        updateChangelogMd(command=dockerCommand)
    else:
        print('No action done.')


if __name__ == "__main__":
    main()
