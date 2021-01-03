"""asas."""

import sys
import os
import requests
import pytest

currentPath = os.path.dirname(os.path.realpath(__file__))
rootPath = os.path.join(currentPath, "..")
libraryDir = os.path.join(rootPath, "lib")
sys.path.append(libraryDir)
from djWasabi import djWasabi


def test_readRepository_repo():
    """Test the _get function with wrong_uri.
    :return:
    """
    repo = djWasabi.git.readRepository(repo="git@github.com:dj-wasabi/consul.git")
    assert repo == "dj-wasabi/consul"


def test_readconfig():
    """Test the _get function with wrong_uri.
    :return:
    """
    yamlConfig = djWasabi.config.readConfig(rootPath=rootPath)
    assert yamlConfig['owner'] == "Werner Dijkerman"
