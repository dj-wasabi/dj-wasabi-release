#!/usr/bin/env python

import subprocess
from . import generic


def readRepository(repo: str = None, debug: bool = False) -> tuple:
    """Get the remote url and return the username and repository.

    :rtype: str
    :return: The username/repository of the current directory.
    """
    if repo is None:
        command = "git config --get remote.origin.url"
        _repository_string = generic.executeCommand(command=command, debug=debug)
    else:
        _repository_string = repo
    print(_repository_string)
    if _repository_string.startswith('https'):
        _data = _repository_string.rsplit('/', 2)
        owner = _data[1]
        repo = _data[2].split('.')[0]
    else:
        _repository = _repository_string.split(':')[1]
        _data = _repository.split('.')[0]
        owner = _data.split('/')[0]
        repo = _data.split('/')[1]

    generic.debugLog(debug=debug, message="Git {o} with repository: {r}".format(o=owner, r=repo))
    return (owner, repo)


def cloneRepository(name: str = None, repositoryUrl: str = None, debug: bool = False):
    """Clone the provided git repository into specific directory.

    """
    command = "git clone {r} {d}".format(r=repositoryUrl, d=name)
    _repository_string = generic.executeCommand(command=command)
    generic.debugLog(debug=debug, message=_repository_string)


def getCheckTag(tag: str = None) -> bool:
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


def getMainBranch() -> str:
    """Get the current main of master branch.

    :rtype: str
    :return: The 'main' or 'master' branch
    """
    _command = [
        "git", "branch", "-r", "--points-at", "refs/remotes/origin/HEAD",
        "| tee | grep -- '->' | awk '{print $3}'"
    ]
    _output = generic.executeCommand(command=_command)
    return _output.split('/')[1]


def getLatestTag() -> str:
    """Get the latest tag created.

    :rtype: str
    :return: The latest created tag.
    """
    _command = ["git", "describe", "--abbrev=0"]
    return generic.executeCommand(command=_command)


def commitFile(file: str = None, message: str = None, debug: bool = False) -> bool:
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
