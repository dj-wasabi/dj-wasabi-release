"""File containing tests specific for the djWasabi/container.py file."""

import sys
import os
import requests
import pytest

currentPath = os.path.dirname(os.path.realpath(__file__))
rootPath = os.path.join(currentPath, "..")
libraryDir = os.path.join(rootPath, "lib")
sys.path.append(libraryDir)
from djWasabi import djWasabi


def test_container_getValueArg_owner():
    """Test the to execute command to do an ls
    :return:
    """
    value = "owner"
    owner = "dj-wasabi"
    repository = "dj-wasabi-release"
    output = djWasabi.container.getValueArg(
        value=value,
        owner=owner,
        repository=repository
    )
    assert output == "dj-wasabi"


def test_container_getValueArg_repository():
    """Test the to execute command to do an ls
    :return:
    """
    value = "repository"
    owner = "dj-wasabi"
    repository = "dj-wasabi-release"
    output = djWasabi.container.getValueArg(
        value=value,
        owner=owner,
        repository=repository
    )
    assert output == "dj-wasabi-release"


def test_container_getValueArg_none():
    """Test the to execute command to do an ls
    :return:
    """
    value = "notexisting"
    owner = "dj-wasabi"
    repository = "dj-wasabi-release"
    output = djWasabi.container.getValueArg(
        value=value,
        owner=owner,
        repository=repository
    )
    assert output is None


def test_container_createContainerCommand():
    """Test the docker run with only Docker image.
    :return:
    """
    configuration = {
        "image": "dj-wasabi/consul"
    }
    owner = "dj-wasabi"
    repository = "dj-wasabi-release"
    container = djWasabi.container.createContainerCommand(
        configuration=configuration,
        owner=owner,
        repository=repository
    )
    output = djWasabi.generic.getString(data=container)
    assert output == "docker run --rm dj-wasabi/consul"


def test_container_createContainerCommand_environment():
    """Test the docker run with only Docker image.
    :return:
    """
    configuration = {
        "image": "dj-wasabi/consul",
        "environment": ["DJWASABI"]

    }
    owner = "dj-wasabi"
    repository = "dj-wasabi-release"
    container = djWasabi.container.createContainerCommand(
        configuration=configuration,
        owner=owner,
        repository=repository
    )
    output = djWasabi.generic.getString(data=container)
    assert output == "docker run --rm -e DJWASABI=test dj-wasabi/consul"


def test_container_createContainerCommand_volumes():
    """Test the docker run with only Docker image.
    :return:
    """

    configuration = {
        "image": "dj-wasabi/consul",
        "volumes": {
            "PWD": "/data",
            "/data": "/data"
        }

    }
    owner = "dj-wasabi"
    repository = "dj-wasabi-release"
    container = djWasabi.container.createContainerCommand(
        configuration=configuration,
        owner=owner,
        repository=repository
    )
    output = djWasabi.generic.getString(data=container)
    value = "docker run --rm -v {v}:/data -v /data:/data dj-wasabi/consul".format(v=os.getcwd())
    assert output == value


def test_container_createContainerCommand_noImage():
    """Test the _delete function without providing url.
    :return:
    """
    configuration = {
        "volumes": {
            "PWD": "/data",
            "/data": "/data"
        }

    }
    owner = "dj-wasabi"
    repository = "dj-wasabi-release"
    with pytest.raises(ValueError, match="Please provide the Docker image."):
        djWasabi.container.createContainerCommand(
            configuration=configuration,
            owner=owner,
            repository=repository
        )
