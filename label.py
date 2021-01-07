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
    parser = argparse.ArgumentParser(description="""This script is responsible for
    creating/deleting labels in current git repositoryin Github based on a configuration
    cound in the 'dj-wasabi.yml` file.""")
    parser.add_argument('-D', '--debug', required=False, action='store_true', help="""Print some
    debug information""")
    parser.add_argument('-r', '--repo', required=False, action='store',
                        help='The name of the repository', type=str)
    parser.add_argument('-t', '--token', required=False, action='store',
                        help='The Github API token.', type=str)
    return parser.parse_args()


def cleanDataGithubLabels(data=None):
    """ Will get the current labels data from Github and only return specific info.

    :param data: The current information of all the labels.
    :type data: dict
    :rtype: list
    :return: Only specific set of keys per label
    """
    _new_data = []
    for entry in data:
        if 'name' not in entry:
            continue
        elif 'color' not in entry:
            continue
        elif 'description' not in entry:
            continue

        value = {
            'name': str(entry['name']),
            'color': str(entry['color']),
            'description': str(entry['description']),
        }
        _new_data.append(value)
    _new_data_sorted = sorted(_new_data, key=lambda k: k['name'])
    return _new_data_sorted


def getGithubLabels(repository=None, headers=None):
    """ Will get all labels in repository.

    :param repository: The username/repository information.
    :type repository: str
    :param headers: The headers used for requests to Github
    :type headers: dicts
    :rtype: list
    :return: All labels from current repository.
    """
    githubUrl = 'https://api.github.com/repos/{r}/labels'.format(r=repository)
    djWasabi.generic.debugLog(debug=is_debug, message="The Github URL {r}".format(r=githubUrl))
    _githubLabels = requests.get(githubUrl, headers=headers)
    return cleanDataGithubLabels(data=_githubLabels.json())


def compareLabelsCreate(config=None, github=None):
    return djWasabi.generic.compareDictsInLists(source1=config, source2=github)
    djWasabi.generic.debugLog(debug=is_debug, message="print 'config': {r}".format(r=config))
    djWasabi.generic.debugLog(debug=is_debug, message="print 'github': {r}".format(r=github))


def compareLabelsDelete(config=None, github=None):
    return djWasabi.generic.compareDictsInLists(source1=github, source2=config)
    djWasabi.generic.debugLog(debug=is_debug, message="print 'config': {r}".format(r=config))
    djWasabi.generic.debugLog(debug=is_debug, message="print 'github': {r}".format(r=github))


def createOrUpdateLabel(repository=None, headers=None, entry=None):
    githubUrl = 'https://api.github.com/repos/{r}/labels'.format(r=repository)
    githubUrlName = '{g}/{n}'.format(g=githubUrl, n=entry['name'])
    headers['Accept'] = "application/vnd.github.v3.text-match+json"
    djWasabi.generic.debugLog(debug=is_debug, message="The full Github labels url: {r}".format(r=githubUrlName))

    labelExist = requests.get(githubUrlName, headers=headers)
    if labelExist.status_code == 200:
        print('Patching label {n}'.format(n=entry['name']))
        r = requests.patch(githubUrlName, headers=headers, data=json.dumps(entry))
        djWasabi.generic.debugLog(debug=is_debug, message="The Github PATCH data: {r}".format(r=r.text))
    else:
        print('Creating label {n}'.format(n=entry['name']))
        r = requests.post(githubUrl, headers=headers, data=json.dumps(entry))
        djWasabi.generic.debugLog(debug=is_debug, message="The Github POST data: {r}".format(r=r.text))


def deleteLabel(repository=None, headers=None, name=None):
    githubUrl = 'https://api.github.com/repos/{r}/labels/{n}'.format(r=repository, n=name)
    headers['Accept'] = "application/vnd.github.v3.text-match+json"
    print('Deleting repo {n}'.format(n=name))
    r = requests.delete(githubUrl, headers=headers)
    djWasabi.generic.debugLog(debug=is_debug, message="The Github DELETE data: {r}".format(r=r.text))


def main():
    #
    global is_debug
    args = get_args()
    is_debug = args.debug
    repo = args.repo
    token = args.token
    yamlConfig = djWasabi.config.readConfig(rootPath=currentPath)
    if token is None:
        token = djWasabi.config.readOsEnv(key="CHANGELOG_GITHUB_TOKEN")
    headers = {'Authorization': 'token {t}'.format(t=token)}

    # TODO validate provided repository
    repository = djWasabi.git.readRepository(repo=repo, debug=is_debug)

    # Get label from configuration file.
    _labels = yamlConfig['labels']
    labels = sorted(_labels, key=lambda k: k['name'])

    # Create or Update the labels
    githubLabels = getGithubLabels(repository=repository, headers=headers)
    diffLabels = compareLabelsCreate(config=labels, github=githubLabels)
    djWasabi.generic.debugLog(debug=is_debug, message="We have differences: {r}".format(r=diffLabels))

    if (len(diffLabels) >= 1):
        print('New or updates Labels found.')
        for entry in diffLabels:
            print('Create or update label {s}'.format(s=entry['name']))
            createOrUpdateLabel(repository=repository, headers=headers, entry=entry)

    # Delete if any labels that exist in repository.
    githubLabels = getGithubLabels(repository=repository, headers=headers)
    diffLabels = compareLabelsDelete(config=labels, github=githubLabels)

    if (len(diffLabels) >= 1):
        print('Delete not needed labels.')
        for entry in diffLabels:
            print('Delete label {s}'.format(s=entry['name']))
            deleteLabel(repository=repository, headers=headers, name=entry['name'])


if __name__ == "__main__":
    main()
