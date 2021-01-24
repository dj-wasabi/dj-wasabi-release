#!/usr/bin/env python

import subprocess
from . import generic


def readRepository(repo=None, debug=False):
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
    _data = _repository.split('.')[0]
    owner = _data.split('/')[0]
    repo = _data.split('/')[1]

    generic.debugLog(debug=debug, message="Git {o} with repository: {r}".format(o=owner, r=repo))
    return (owner, repo)


def cloneRepository(name=None, repositoryUrl=None, debug=False):
    """ Clone the provided git repository into specific directory.

    """
    command = "git clone {r} {d}".format(r=repositoryUrl, d=name)
    _repository_string = generic.executeCommand(command=command)
    generic.debugLog(debug=debug, message=_repository_string)
