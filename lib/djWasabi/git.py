#!/usr/bin/env python

import subprocess
from . import generic


def readRepository(repo=None, debug=True):
    """ Get the remote url and return the username and repository.

    :rtype: str
    :return: The username/repository of the current directory.
    """
    if repo is None:
        command = "git config --get remote.origin.url"
        _repository_string = generic.executeCommand(command=command)
    else:
        _repository_string = repo
    _repository = _repository_string.split(':')[1]
    generic.debugLog(debug=True, message="Git repository: {m}".format(m=_repository.split('.')[0]))
    return _repository.split('.')[0]


def cloneRepository(name=None, repository=None, debug=False):
    """ Clone the provided git repository into specific directory.

    """
    command = "git clone {r} {d}".format(r=repository, d=name)
    _repository_string = generic.executeCommand(command=command)
    generic.debugLog(debug=debug, message=_repository_string)
