#!/usr/bin/env python

import os
import yaml
import sys


def readConfig(rootPath=None):
    """ Will read the configuration file and return the content.

    :rtype: dict
    :return: The content of the configuration file.
    """
    configFile = os.path.join(rootPath, "dj-wasabi.yml")

    with open(configFile, 'r') as stream:
        try:
            _load = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return _load


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
        raise ValueError('Provided key does not exist.')
