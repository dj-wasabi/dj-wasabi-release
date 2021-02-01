"""File containing tests specific for the djWasabi/request.py file."""

import sys
import os
import requests
import pytest

currentPath = os.path.dirname(os.path.realpath(__file__))
rootPath = os.path.join(currentPath, "..")
libraryDir = os.path.join(rootPath, "lib")
sys.path.append(libraryDir)
from djWasabi import djWasabi


def test_request__get_name():
    """Test the _get function with providing url.

    Get return: {'id': <NUM>, 'node_id': '<ASAS>', 'name': 'dj-wasabi-release', 'full_name': 'dj-wasabi/dj-wasabi-release', ..
    :return:
    """
    owner, repository = djWasabi.git.readRepository(repo="git@github.com:dj-wasabi/dj-wasabi-release.git")
    githubUrl = djWasabi.generic.getGithubUrl(owner=owner, repository=repository)

    success, output = djWasabi.request._get(url=githubUrl)
    assert success
    assert output.json()['name'] == "dj-wasabi-release"


def test_request__get_no_url():
    """Test the _get function without providing url.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the URL."):
        djWasabi.request._get()


def test_request__patch_no_url():
    """Test the _patch function without providing url.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the URL."):
        djWasabi.request._patch()


def test_request__post_no_url():
    """Test the _post function without providing url.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the URL."):
        djWasabi.request._post()


def test_request__put_no_url():
    """Test the _put function without providing url.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the URL."):
        djWasabi.request._put()


def test_request__delete_no_url():
    """Test the _delete function without providing url.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the URL."):
        djWasabi.request._delete()
