#!/usr/bin/env python
"""This script is responsible for configuring the git repositories based on a configuration found in the 'dj-wasabi.yml` file."""

import os
import sys
import requests
import argparse
import json

currentPath = os.path.dirname(os.path.realpath(__file__))
libraryDir = os.path.join(currentPath, "lib")
sys.path.append(libraryDir)
from djWasabi import djWasabi


def get_args():
    """Support the command-line arguments listed below."""
    parser = argparse.ArgumentParser(description="""This script is responsible for
    configuring the git repositories based on a configuration found in the
    'dj-wasabi.yml` file.""")
    parser.add_argument('-D', '--debug', required=False, action='store_true', help="""Print some
    debug information""")
    parser.add_argument('-r', '--repo', required=False, action='store',
                        help='The name of the repository. Example "git@github.com:dj-wasabi/consul.git"', type=str)
    parser.add_argument('-t', '--token', required=False, action='store',
                        help='The Github API token.', type=str)
    return parser.parse_args()


def updateRepository(url: str = None, headers: dict = None, data: dict = None, config: dict = None):
    """Configure the Guthub git repository.

    :param url: The URL to the Github repository.
    :type url: str
    :param headers: The headers.
    :type headers: dict
    :param data: The headers.
    :type data: dict
    :param config: The headers.
    :type config: dict
    """
    patchData = {}
    configOptions = [
        "wiki", "projects", "issues", "archived", "private", "allow_squash_merge",
        "allow_merge_commit", "allow_rebase_merge", "delete_branch_on_merge"
    ]
    headers['Accept'] = "application/vnd.github.v3+json"

    # Check configuration with current setup
    for configOption in configOptions:
        if configOption in config:
            if configOption in ["wiki", "projects", "issues"]:
                has_configOption = "has_{s}".format(s=configOption)
                if data[has_configOption] != config[configOption]:
                    patchData[has_configOption] = config[configOption]
                continue
            if data[configOption] != config[configOption]:
                patchData[configOption] = config[configOption]

    # Patching the repository
    if len(patchData):
        djWasabi.generic.debugLog(
            debug=is_debug,
            message="We have the following configuration options {r}".format(r=json.dumps(patchData))
        )
        success, _data = request._patch(url=url, headers=headers, data=json.dumps(patchData))
        request.verifyResponse(success=success, data=_data)


def repositorySecurity(url: str = None, headers: dict = None, config: dict = None):
    securityUrl = "{g}/vulnerability-alerts".format(g=url)
    headers['Accept'] = "application/vnd.github.dorian-preview+json"
    _success, _securityData = request._get(url=securityUrl, headers=headers)
    securityData = _securityData.json()
    if securityData['message'] == "Vulnerability alerts are disabled.":
        securityEnabled = False
    else:
        securityEnabled = True

    if config['vulnerability'] and not securityEnabled:
        # Enable it
        success, _ = request._put(url=securityUrl, headers=headers)
        if success:
            print("Enabled it")
    elif not config['vulnerability'] and securityEnabled:
        # Disable it
        success, _ = request._delete(url=securityUrl, headers=headers)
        if success:
            print("Disabled it")
    else:
        # We don't have to do anything.
        print("asas")


def main():
    global is_debug
    global request
    args = get_args()
    is_debug = args.debug
    repo = args.repo
    token = args.token

    request = djWasabi.http.request(debug=is_debug)
    yamlConfigFile = os.path.join(currentPath, "dj-wasabi.yml")
    yamlConfig = djWasabi.config.readYamlFile(file=yamlConfigFile)
    if token is None:
        token = djWasabi.config.readOsEnv(key="CHANGELOG_GITHUB_TOKEN")
    headers = {
        'Authorization': 'token {t}'.format(t=token)
    }

    # Get configuration from 'dj-wasabi.yml'
    owner, repository = djWasabi.git.readRepository(repo=repo, debug=is_debug)
    repoConfig = djWasabi.config.getRepository(
        config=yamlConfig['repositories'],
        name=repository,
        default=yamlConfig['repository_default']
    )

    # Get data from Github
    githubUrl = djWasabi.generic.getGithubUrl(owner=owner, repository=repository)
    _success, _repoData = request._get(url=githubUrl, headers=headers)
    repoData = request.verifyResponse(success=_success, data=_repoData)
    djWasabi.generic.debugLog(
        debug=is_debug,
        message="We have the following JSON data: {r}".format(r=json.dumps(repoData))
    )

    # Update the repository
    updateRepository(url=githubUrl, headers=headers, data=repoData, config=repoConfig)

    # Disable for now, until I have it working properly.
    # repositorySecurity(url=githubUrl, headers=headers, config=repoConfig)


if __name__ == "__main__":
    main()
