#!/usr/bin/env python

import tempfile
import subprocess


def debugLog(debug=False, message=None):
    if debug:
        print(message)


def compareDictsInLists(source1=None, source2=None):
    # pairs = zip(source1, source2)
    return [i for i in source1 if i not in source2]


def makeTempDir():
    """ Make a temporary directory.

    :rtype: str
    :return: The path to the temporary directory.
    """
    return tempfile.mkdtemp()


def getString(data=None, separater=" "):
    if isinstance(data, str):
        return data
    elif isinstance(data, list):
        return separater.join(data)


def executeCommand(command=None):
    """
    """
    if not command:
        raise ValueError('Please provide the command we want to execute.')
    _command = getString(data=command, separater=" ")
    proc = subprocess.Popen(_command, shell=True, stdout=subprocess.PIPE)
    return proc.communicate()[0].decode().strip('\n')


def getRepoUrl(owner=None, repository=None):
    """Get the complete URL for the Github repository.

    :param owner: The name of the owner of the repository.
    :typem owner: str
    :param repository: The name of the repository
    :typem repository: str
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
    :typem owner: str
    :param repository: The name of the repository
    :typem repository: str
    :rtype: str
    :return: The complete url to the Github repository
    """
    if not owner:
        raise ValueError('Please provide the owner of the repository.')
    if not repository:
        raise ValueError('Please provide the name of the repository.')
    return "https://api.github.com/repos/{o}/{r}".format(o=owner, r=repository)
