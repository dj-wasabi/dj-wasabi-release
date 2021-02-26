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
def test_http__get_name():
    with open("tests/resources/dj-wasabi-release.json") as f:
        jsonData = json.load(f)
    responses.add(responses.GET, 'https://fake.url.com/dj-wasabi-release',
                  json=jsonData, status=200)

    request = djWasabi.http.request(debug=True)
    success, output = request._get(url='https://fake.url.com/dj-wasabi-release')

    assert success
    assert output.json()['name'] == "dj-wasabi-release"
    assert output.status_code == 200


def test_http__get_no_url():
    """Test the _get function without providing url.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the URL."):
        request = djWasabi.http.request()
        request._get()


@responses.activate
def test_http__get_name_fail():
    with open("tests/resources/dj-wasabi-release.json") as f:
        jsonData = json.load(f)
    responses.add(responses.GET, 'https://fake.url.com/dj-wasabi-release',
                  json=jsonData, status=200)

    request = djWasabi.http.request()
    success, output = request._get(
        url='https://fake.url.com/dj-wasabi-releas',
        username="fake", password="fake")
    assert not success


@responses.activate
def test_http__patch_name():
    with open("tests/resources/dj-wasabi-release.json") as f:
        jsonData = json.load(f)
    responses.add(responses.PATCH, 'https://fake.url.com/dj-wasabi-release',
                  json=jsonData, status=200)

    request = djWasabi.http.request()
    success, output = request._patch(url='https://fake.url.com/dj-wasabi-release')

    assert success
    assert output.json()['name'] == "dj-wasabi-release"
    assert output.status_code == 200


def test_http__patch_no_url():
    """Test the _patch function without providing url.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the URL."):
        request = djWasabi.http.request()
        request._patch()


@responses.activate
def test_http__patch_name_fail():
    with open("tests/resources/dj-wasabi-release.json") as f:
        jsonData = json.load(f)
    responses.add(responses.PATCH, 'https://fake.url.com/dj-wasabi-release',
                  json=jsonData, status=200)

    request = djWasabi.http.request()
    success, output = request._patch(
        url='https://fake.url.com/dj-wasabi-releas',
        username="fake", password="fake")

    assert not success


@responses.activate
def test_http__post_name():
    with open("tests/resources/dj-wasabi-release.json") as f:
        jsonData = json.load(f)
    responses.add(responses.POST, 'https://fake.url.com/dj-wasabi-release',
                  json=jsonData, status=201)

    request = djWasabi.http.request()
    success, output = request._post(url='https://fake.url.com/dj-wasabi-release')

    assert success
    assert output.json()['name'] == "dj-wasabi-release"
    assert output.status_code == 201


def test_http__post_no_url():
    """Test the _post function without providing url.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the URL."):
        request = djWasabi.http.request()
        request._post()


@responses.activate
def test_http__post_name_fail():
    with open("tests/resources/dj-wasabi-release.json") as f:
        jsonData = json.load(f)
    responses.add(responses.POST, 'https://fake.url.com/dj-wasabi-release',
                  json=jsonData, status=201)

    request = djWasabi.http.request()
    success, output = request._post(
        url='https://fake.url.com/dj-wasabi-releas',
        username="fake", password="fake")

    assert not success


@responses.activate
def test_http__put_name():
    with open("tests/resources/dj-wasabi-release.json") as f:
        jsonData = json.load(f)
    responses.add(responses.PUT, 'https://fake.url.com/dj-wasabi-release',
                  json=jsonData, status=200)

    request = djWasabi.http.request()
    success, output = request._put(url='https://fake.url.com/dj-wasabi-release')

    assert success
    assert output.json()['name'] == "dj-wasabi-release"
    assert output.status_code == 200


def test_http__put_no_url():
    """Test the _put function without providing url.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the URL."):
        request = djWasabi.http.request()
        request._put()


@responses.activate
def test_http__put_name_fail():
    with open("tests/resources/dj-wasabi-release.json") as f:
        jsonData = json.load(f)
    responses.add(responses.PUT, 'https://fake.url.com/dj-wasabi-release',
                  json=jsonData, status=200)

    request = djWasabi.http.request()
    success, output = request._put(
        url='https://fake.url.com/dj-wasabi-releas',
        username="fake", password="fake")

    assert not success


@responses.activate
def test_http__delete_name():
    responses.add(responses.DELETE, 'https://fake.url.com/dj-wasabi-release',
                  json="", status=204)

    request = djWasabi.http.request()
    success, output = request._delete(url='https://fake.url.com/dj-wasabi-release')

    assert success
    assert output.json() == ""
    assert output.status_code == 204


def test_http__delete_no_url():
    """Test the _delete function without providing url.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the URL."):
        request = djWasabi.http.request()
        request._delete()


@responses.activate
def test_http__delete_name_fail():
    responses.add(responses.DELETE, 'https://fake.url.com/dj-wasabi-release',
                  json="", status=204)

    request = djWasabi.http.request()
    success, output = request._delete(
        url='https://fake.url.com/dj-wasabi-releas',
        username="fake", password="fake")

    assert not success
