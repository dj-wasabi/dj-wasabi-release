#!/usr/bin/env python

import os
import sys

try:
    import yaml
except:
    print('Please install: pip install pyyaml')
    sys.exit(1)


def readConfig(rootPath: str = None) -> dict:
    """ Will read the configuration file and return the content.

    :rtype: dict
    :return: The content of the configuration file.
    """
    configFile = os.path.join(rootPath, "dj-wasabi.yml")

    try:
        with open(configFile, 'r') as stream:
            try:
                _load = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return _load
    except IOError:
        raise ValueError('File {f} does not exist.'.format(f=configFile))


def readOsEnv(key: str = None) -> str:
    """ Will get the value for the provided environment variable..

    :param key: The name of the environment variable.
    :type key: str
    :rtype: str
    :return: When exist, the value for environment variable.
    """
    if key in os.environ:
        return os.environ[key]
    else:
        raise ValueError('Provided key does not exist.')


def getRepository(config: dict = None, name: str = None, default: dict = None) -> dict:
    """Get the correct configuration for the repository.

    :param default: The default configuration we will override.
    :type default: dict
    :param config: The compleet repository list.
    :type config: list
    :param name: The name of the current repository we want to find.
    :type name: str
    :rtype: dict
    :return: The combination of the default and overriden config.
    """
    for entry in config:
        if entry['name'] == name:
            return combineConfig(default=default, config=entry)
    return False


def combineConfig(default: dict = None, config: dict = None) -> dict:
    """Override the default with the configuration.

    :param default: The default configuration we will override.
    :type default: dict
    :param config: The information
    :type config: dict
    :rtype: dict
    :return: The combination of the default and overriden config.
    """
    default['name'] = config['name']
    for key in config:
        if key in default:
            if default[key] != config[key]:
                default[key] = config[key]
    return default
