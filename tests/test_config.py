"""File containing tests specific for the djWasabi/config.py file."""

import sys
import os
import requests
import pytest

currentPath = os.path.dirname(os.path.realpath(__file__))
rootPath = os.path.join(currentPath, "..")
libraryDir = os.path.join(rootPath, "lib")
sys.path.append(libraryDir)
from djWasabi import djWasabi


def test_config_readYamlFile():
    """Test the reading of the yaml configuration
    :return:
    """
    yamlConfig = djWasabi.config.readYamlFile(file="tests/resources/config.yml")
    assert yamlConfig['dummy']
    assert yamlConfig['pizza'] == "I Like it"


def test_config_readYamlFile_no_file():
    """Test the reading of the yaml configuration when the file doesn't exist.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide a path to the YAML file."):
        djWasabi.config.readYamlFile()


def test_config_readYamlFile_failure():
    """Test the reading of the yaml configuration when the file doesn't exist.
    :return:
    """
    with pytest.raises(ValueError, match="File /tmp/dj-wasabi.yml does not exist."):
        djWasabi.config.readYamlFile(file="/tmp/dj-wasabi.yml")


def test_config_readYamlFile_failure_no_yaml():
    """Test the reading of the yaml configuration when the file doesn't exist.
    :return:
    """
    with pytest.raises(ValueError, match="File does not contain YAML"):
        djWasabi.config.readYamlFile(file="/etc/hosts")


def test_config_readOsEnv():
    """Test the the getting of environment variable.
    :return:
    """
    envKey = djWasabi.config.readOsEnv(key="DJWASABI")
    assert envKey == "test"


def test_config_readOsEnv_not_existing():
    """Test the the getting of environment variable which doesn't exist.
    :return:
    """
    with pytest.raises(ValueError, match="Provided key does not exist."):
        djWasabi.config.readOsEnv(key="NOT_EXISTING")


def test_config_getConfiguration():
    """Get the repository configuration for existing repository.
    """
    default = {
        "wiki": True,
        "archived": False
    }
    repositories = [
        {
            "name": "docker-local-development-puppet",
            "archived": True
        }
    ]

    config = djWasabi.config.getRepository(
        config=repositories, name="docker-local-development-puppet",
        default=default
    )
    print(config)
    assert config['name'] == "docker-local-development-puppet"
    assert config['archived']


def test_config_getConfiguration_false():
    """Get the repository configuration for not existing repository.
    """
    default = {
        "wiki": True,
        "archived": False
    }
    repositories = [
        {
            "name": "docker-local-development-puppet",
            "archived": True
        }
    ]

    config = djWasabi.config.getRepository(
        config=repositories, default=default,
        name="docker-local-development-puppet_none"
    )
    assert not config
