"""File containing tests specific for the djWasabi/request.py file."""

import sys
import os
import requests
import json
import pytest
import responses
from requests.exceptions import RequestException

currentPath = os.path.dirname(os.path.realpath(__file__))
rootPath = os.path.join(currentPath, "..")
libraryDir = os.path.join(rootPath, "lib")
sys.path.append(libraryDir)
from djWasabi import djWasabi


@responses.activate
def test_request__get_name():
    with open("tests/resources/dj-wasabi-release.json") as f:
        jsonData = json.load(f)
    responses.add(responses.GET, 'https://fake.url.com/dj-wasabi-release',
                  json=jsonData, status=200)

    success, output = djWasabi.request._get(url='https://fake.url.com/dj-wasabi-release')

    assert success
    assert output.json()['name'] == "dj-wasabi-release"
    assert output.status_code == 200


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
