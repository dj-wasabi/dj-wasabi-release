"""File containing tests specific for the djWasabi/git.py file."""

import sys
import os
import requests
import pytest

currentPath = os.path.dirname(os.path.realpath(__file__))
rootPath = os.path.join(currentPath, "..")
libraryDir = os.path.join(rootPath, "lib")
sys.path.append(libraryDir)
from djWasabi import djWasabi


def test_git_readRepository_with_https_repo():
    """Test the read repository with the repo git repo.
    :return:
    """
    owner, repo = djWasabi.git.readRepository(repo="https://github.com/dj-wasabi/pre-commit-hooks")
    assert owner == "dj-wasabi"
    assert repo == "pre-commit-hooks"


def test_git_readRepository_with_repo():
    """Test the read repository with the repo git repo.
    :return:
    """
    owner, repo = djWasabi.git.readRepository(repo="git@github.com:dj-wasabi/consul.git")
    assert owner == "dj-wasabi"
    assert repo == "consul"


def test_git_readRepository_without_repo():
    """Test the read repository without argument, provide the current git info back.
    :return:
    """
    owner, repo = djWasabi.git.readRepository()
    assert owner == "dj-wasabi"
    assert repo == "dj-wasabi-release"


# def test_git_readRepository_getMainBranch():
#     """Test the return of the "main" branch.
#     :return:
#     """
#     output = djWasabi.git.getMainBranch()
#     assert output == "main"


# def test_git_readRepository_getLatestTag():
#     """Test the return of the "main" branch.
#     :return:
#     """
#     output = djWasabi.git.getLatestTag()
#     assert output.startswith('0.')
