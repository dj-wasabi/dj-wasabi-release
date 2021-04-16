#!/usr/bin/env python

import os
from . import config
from . import generic


def validateDockerRunning():
    """Validate if Docker is running.

    :rtype: bool
    :return: If Docker is running (True) or not (False)
    """
    dockerCommand = ["docker", "ps"]
    _output = generic.executeCommand(command=dockerCommand)
    if _output == 'Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?':
        return False
    else:
        return True


def getValueArg(value: str = None, owner: str = None, repository: str = None, version: str = None) -> str:
    """Create a 'docker run' command based on configuration.

    :param value: The variable you want to get.
    :type value: str
    :param owner: The name of the owner of the repository.
    :type owner: str
    :param repository: The name of the repository
    :type repository: str
    :param version: The version of the release.
    :type version: str
    :rtype: str
    :return: The complete url to the Github repository
    """
    if value == "owner":
        return owner
    elif value == "repository":
        return repository
    elif value == "version":
        return version
    else:
        return None


def createContainerCommand(configuration: dict = None, owner: str = None, repository: str = None, version: str = None,
                           debug: bool = False
                           ) -> str:
    """Create a 'docker run' command based on configuration.

    :param configuration: The Docker configuration.
    :type configuration: dict
    :param owner: The name of the owner of the repository.
    :type owner: str
    :param repository: The name of the repository
    :type repository: str
    :param version: The version of the release.
    :type version: str
    :rtype: str
    :return: The complete url to the Github repository
    """
    if 'image' not in configuration:
        raise ValueError('Please provide the Docker image.')
    command = ["docker", "run", "--rm"]

    # Envs
    if 'environment' in configuration:
        for env in configuration['environment']:
            command.append("-e")
            _env = config.readOsEnv(key=env)
            _env_string = "{e}={s}".format(e=env, s=_env)
            command.append(_env_string)
    # Volumes
    if 'volumes' in configuration:
        for volume in configuration['volumes']:
            command.append("-v")
            if volume == "PWD":
                _volumeString = "{v}:{d}".format(v=os.getcwd(), d=configuration['volumes'][volume])
            else:
                _volumeString = "{v}:{d}".format(v=volume, d=configuration['volumes'][volume])
            command.append(_volumeString)
    command.append(configuration['image'])
    # Arguments
    if 'arguments' in configuration:
        for arg in configuration['arguments']:
            # generic.debugLog(debug=True, message="value is {a}".format(a=arg))
            if arg == "version" and version is None:
                continue
            myvalue = getValueArg(value=arg, owner=owner, repository=repository, version=version)
            myArg = "{k} {v}".format(k=configuration['arguments'][arg], v=myvalue)
            command.append(myArg)
    generic.debugLog(debug=debug, message="Executing command: {c}".format(c=command))
    return command
