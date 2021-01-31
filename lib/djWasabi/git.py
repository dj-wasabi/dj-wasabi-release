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


def getCheckTag(tag=None):
    """Check if we have already a tag with same name.

    :param tag: The name of the tag.
    :type tag: str
    :rtype: bool
    :return: If the tag exist (True) or not (False)
    """
    if tag is None:
        raise ValueError('Please provide a tag to check.')
    _command = ["git", "tag", "|", "grep", tag, "|", "wc", "-l"]
    _output = int(generic.executeCommand(command=_command))
    if _output == 0:
        return False
    else:
        return True


def getMainBranch():
    """Get the current main of master branch.

    :rtype: str
    :return: The 'main' or 'master' branch
    """
    _command = ["git", "rev-parse", "--abbrev-ref", "HEAD"]
    return generic.executeCommand(command=_command)


def getLatestTag():
    """Get the latest tag created.

    :rtype: str
    :return: The latest created tag.
    """
    _command = ["git", "describe", "--abbrev=0"]
    return generic.executeCommand(command=_command)


def commitFile(file=None, message=None, debug=False):
    """Commit a file when it is changed.

    :param file: The name of the file we want to commit.
    :type file: str
    :param message: The commit message we want to use.
    :type message: str
    :param debug: If we want debug logging enabled.
    :type debug: Bool
    :rtype: bool
    :return: When committed (True), or no commit has been made (False)
    """
    changelogdUpdated = ["git", "status", "|", "grep", file, "|", "wc", "-l"]
    changelogdUpdatedOutput = int(generic.executeCommand(command=changelogdUpdated))
    if changelogdUpdatedOutput >= 1:
        gitAddCommand = ["git", "add", file]
        generic.executeCommand(command=gitAddCommand)
        gitCommitCommand = ['git commit -m "{m}" {f}'.format(m=message, f=file)]
        generic.debugLog(debug=debug, message="Executing command: {c}".format(c=gitCommitCommand))
        generic.executeCommand(command=gitCommitCommand)
        return True
    return False
