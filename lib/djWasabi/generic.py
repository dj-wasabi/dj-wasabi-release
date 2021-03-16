#!/usr/bin/env python

import tempfile
import subprocess


def debugLog(debug: bool = False, message: str = None):
    """Debug message when debug is enabled.

    :param debug: If we have debug enabled or not.
    :type debug: bool
    :param message: The message we want to print.
    :type message: str
    :example:

    >>> import djWasabi
    >>> djWasabi.generic.debugLog(debug=True, message="my Message")
    my Message

    """
    if debug:
        print(message)


def compareDictsInLists(source1: list = None, source2: list = None) -> list:
    # pairs = zip(source1, source2)
    return [i for i in source1 if i not in source2]


def keysExistInDict(element: dict = None, *keys) -> bool:
    """Check if keys nested exists in element.

    :param element: The dict we want to check.
    :type element: dict
    :rtype: bool
    :return: If the keys exist (True) or not (False)
    :example:

    >>> import djWasabi
    >>> data = {"name": {"key": {"value": "doc"}}}
    >>> print(djWasabi.generic.keysExistInDict(element=data, "name", "key"))
    True
    """
    if not isinstance(element, dict):
        raise ValueError('We expects dict as first argument.')
    if len(keys) == 0:
        raise ValueError('We expects at least two arguments, one given.')

    _element = element
    for key in keys:
        if key in _element:
            _element = _element[key]
        else:
            return False
    return True


def makeTempDir() -> str:
    """Make a temporary directory.

    :rtype: str
    :return: The path to the temporary directory.
    """
    return tempfile.mkdtemp()


def getString(data: dict = None, separater: str = " ") -> str:
    """Debug message when debug is enabled.

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


def executeCommand(command: str = None, shell: bool = True, debug: bool = False) -> str:
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


def getRepoUrl(owner: str = None, repository: str = None) -> str:
    """Get the complete URL for the Github repository.

    :param owner: The name of the owner of the repository.
    :type owner: str
    :param repository: The name of the repository
    :type repository: str
    :rtype: str
    :return: The complete url to the Github repository
    :example:

    >>> import djWasabi
    >>> print(djWasabi.generic.getRepoUrl(owner="dj-wasabi", repository="dj-wasabi-release")
    git@github.com:dj-wasabi/dj-wasabi-release.git
    """
    if not owner:
        raise ValueError('Please provide the owner of the repository.')
    if not repository:
        raise ValueError('Please provide the name of the repository.')
    return "git@github.com:{o}/{r}.git".format(o=owner, r=repository)


def getGithubUrl(owner: str = None, repository: str = None) -> str:
    """Get the complete URL for the Github repository.

    :param owner: The name of the owner of the repository.
    :type owner: str
    :param repository: The name of the repository
    :type repository: str
    :rtype: str
    :return: The complete url to the Github repository
    :example:

    >>> import djWasabi
    >>> print(djWasabi.generic.getGithubUrl(owner="dj-wasabi", repository="dj-wasabi-release")
    https://api.github.com/repos/dj-wasabi/dj-wasabi-release
    """
    if not owner:
        raise ValueError('Please provide the owner of the repository.')
    if not repository:
        raise ValueError('Please provide the name of the repository.')
    return "https://api.github.com/repos/{o}/{r}".format(o=owner, r=repository)
