#!/usr/bin/env python

import tempfile
import subprocess


def debugLog(debug=False, message=None):
    """ Debug message when debug is enabled.

    :param debug: If we have debug enabled or not.
    :type debug: bool
    :param message: The message we want to print.
    :type message: str
    """
    if debug:
        print(message)


def compareDictsInLists(source1=None, source2=None):
    # pairs = zip(source1, source2)
    return [i for i in source1 if i not in source2]


def keysExistInDict(element=None, *keys):
    """ Check if *keys (nested) exists in element.

    :param element: The dict we want to check.
    :type element: dict
    """
    if not isinstance(element, dict):
        raise ValueError('We expects dict as first argument.')
    if len(keys) == 0:
        raise ValueError('We expects at least two arguments, one given.')

    _element = element
    for key in keys:
        if key in _element:
            try:
                _element = _element[key]
            except KeyError:
                return False
        else:
            return False
    return True


def makeTempDir():
    """ Make a temporary directory.

    :rtype: str
    :return: The path to the temporary directory.
    """
    return tempfile.mkdtemp()


def getString(data=None, separater=" "):
    """ Debug message when debug is enabled.

    :param data: The value in either str or list.
    :type data: str,list
    :param separater: The separater between the words.
    :type separater: str
    :rtype: str
    :return: The message in string.
    """
    if isinstance(data, str):
        return data
    elif isinstance(data, list):
        return separater.join(data)


def executeCommand(command=None, shell=True, debug=False):
    """Executing a command and returns the output.

    :param command: The command we want to execute.
    :type command: str,list
    :param shell: If we want to make use of a shell
    :type shell: bool
    :param debug: If we have debug enabled or not.
    :type debug: bool
    :rtype: str
    :return: The complete url to the Github repository
    """
    if not command:
        raise ValueError('Please provide the command we want to execute.')
    _command = getString(data=command, separater=" ")
    debugLog(message='Executing command: {c}'.format(c=_command), debug=debug)
    proc = subprocess.Popen(_command, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.communicate()[0].decode().strip('\n')


def getRepoUrl(owner=None, repository=None):
    """Get the complete URL for the Github repository.

    :param owner: The name of the owner of the repository.
    :type owner: str
    :param repository: The name of the repository
    :type repository: str
    :rtype: str
    :return: The complete url to the Github repository
    """
    if not owner:
        raise ValueError('Please provide the owner of the repository.')
    if not repository:
        raise ValueError('Please provide the name of the repository.')
    return "git@github.com:{o}/{r}.git".format(o=owner, r=repository)


def getGithubUrl(owner=None, repository=None):
    """Get the complete URL for the Github repository.

    :param owner: The name of the owner of the repository.
    :type owner: str
    :param repository: The name of the repository
    :type repository: str
    :rtype: str
    :return: The complete url to the Github repository
    """
    if not owner:
        raise ValueError('Please provide the owner of the repository.')
    if not repository:
        raise ValueError('Please provide the name of the repository.')
    return "https://api.github.com/repos/{o}/{r}".format(o=owner, r=repository)
