#!/usr/bin/env python
#

import os
import sys
import requests
import subprocess
import argparse
import json

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
    return parser.parse_args()


def readOsEnv(key=None):
  """ Will get the value for the provided environment variable..

  :param key: The name of the environment variable.
  :typem key: str
  :rtype: str
  :return: When exist, the value for environment variable.
  """
  if key in os.environ:
    return os.environ[key]
  else:
    print('Provided {s} does not exist.'.format(s=key))
    sys.exit(1)


def readConfig():
  """ Will read the configuration file and return the content.

  :rtype: dict
  :return: The content of the configuration file.
  """
  currentPath = os.path.dirname(os.path.realpath(__file__))
  configFile = os.path.join(currentPath, "dj-wasabi.yml")

  with open(configFile, 'r') as stream:
    try:
        _load = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
  return _load


def readRepository():
  """ Get the remote url and return the username and repository.

  :rtype: str
  :return: The username/repository of the current directory.
  """
  command = "git config --get remote.origin.url"
  proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  _repository_string = proc.communicate()[0].decode().strip('\n')
  _repository = _repository_string.split(':')[1]
  return _repository[:-4]


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
  _githubLabels = requests.get(githubUrl, headers=headers)
  return cleanDataGithubLabels(data=_githubLabels.json())


def compareLabelsCreate(config=None, github=None):
  pairs = zip(config, github)
  return [i for i in config if i not in github]


def compareLabelsDelete(config=None, github=None):
  pairs = zip(config, github)
  return [i for i in github if i not in config]


def createOrUpdateLabel(repository=None, headers=None,  entry=None):
  githubUrl = 'https://api.github.com/repos/{r}/labels'.format(r=repository)
  githubUrlName = '{g}/{n}'.format(g=githubUrl, n=entry['name'])
  headers['Accept'] = "application/vnd.github.v3.text-match+json"

  labelExist = requests.get(githubUrlName, headers=headers)
  if labelExist.status_code == 200:
    print('Patching label {n}'.format(n=entry['name']))
    requests.patch(githubUrlName, headers=headers, data=json.dumps(entry))
  else:
    print('Creating label {n}'.format(n=entry['name']))
    r = requests.post(githubUrl, headers=headers, data=json.dumps(entry))
    if is_debug:
      print(r.text)


def deleteLabel(repository=None, headers=None,  name=None):
  githubUrl = 'https://api.github.com/repos/{r}/labels/{n}'.format(r=repository, n=name)
  headers['Accept'] = "application/vnd.github.v3.text-match+json"
  print('Deleting repo {n}'.format(n=name))
  r = requests.delete(githubUrl, headers=headers)
  if is_debug:
    print(r.text)


def main():
  #
  global is_debug
  args = get_args()
  is_debug = args.debug
  yamlConfig = readConfig()
  repository = readRepository()
  token = readOsEnv(key="CHANGELOG_GITHUB_TOKEN")
  headers = {'Authorization': 'token {t}'.format(t=token)}

  # Get label from configuration file.
  _labels = yamlConfig['labels']
  labels = sorted(_labels, key=lambda k: k['name']) 

  # Create or Update the labels
  githubLabels = getGithubLabels(repository=repository, headers=headers)
  diffLabels = compareLabelsCreate(config=labels, github=githubLabels)
  if(len(diffLabels) >= 1):
    print('New or updates Labels found.')
    for entry in diffLabels:
      print('Create or update label {s}'.format(s=entry['name']))
      createOrUpdateLabel(repository=repository, headers=headers, entry=entry)

  # Delete if any labels that exist in repository.
  githubLabels = getGithubLabels(repository=repository, headers=headers)
  diffLabels = compareLabelsDelete(config=labels, github=githubLabels)
  if(len(diffLabels) >=1):
    print('Delete not needed labels.')
    for entry in diffLabels:
      print('Delete label {s}'.format(s=entry['name']))
      deleteLabel(repository=repository, headers=headers, name=entry['name'])


if __name__ == "__main__":
    main()