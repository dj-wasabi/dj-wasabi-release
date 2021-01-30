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


def test_config_readconfig():
    """Test the reading of the yaml configuration
    :return:
    """
    yamlConfig = djWasabi.config.readConfig(rootPath=rootPath)
    assert yamlConfig['owner'] == "Werner Dijkerman"


def test_config_readconfig_failure():
    """Test the reading of the yaml configuration when the file doesn't exist.
    :return:
    """
    with pytest.raises(ValueError, match="File /tmp/dj-wasabi.yml does not exist."):
        djWasabi.config.readConfig(rootPath="/tmp")


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


def test_generic_githubUrl():
    """Test the githubUrl function.
    """
    githubUrl = djWasabi.generic.getGithubUrl(owner="dj-wasabi", repository="consul")
    assert githubUrl == "https://api.github.com/repos/dj-wasabi/consul"


def test_generic_githubUrl_no_owner():
    """Test the githubUrl function without providing owner.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the owner of the repository."):
        djWasabi.generic.getGithubUrl(repository="consul")


def test_generic_githubUrl_no_repository():
    """Test the githubUrl function without providing repository.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the name of the repository."):
        djWasabi.generic.getGithubUrl(owner="dj-wasabi")


def test_request__get_consul_name():
    """Test the _get function with providing url.

    Get return: {'id': <NUM>, 'node_id': '<ASAS>', 'name': 'consul', 'full_name': 'dj-wasabi/consul', 'private': False, 'owner'
    :return:
    """
    owner, repository = djWasabi.git.readRepository(repo="git@github.com:dj-wasabi/consul.git")
    githubUrl = djWasabi.generic.getGithubUrl(owner=owner, repository=repository)

    success, output = djWasabi.request._get(url=githubUrl)
    assert success
    assert output.json()['name'] == "consul"


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
