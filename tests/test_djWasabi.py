"""asas."""

import sys
import os
import requests
import pytest

currentPath = os.path.dirname(os.path.realpath(__file__))
libraryDir = os.path.join(currentPath, "..", "lib")
sys.path.append(libraryDir)
from djWasabi import djWasabi


def test_readRepository_repo():
    """Test the _get function with wrong_uri.
    :return:
    """
    repo = djWasabi.git.readRepository(repo="git@github.com:dj-wasabi/consul.git")
    assert repo == "dj-wasabi/consul"
