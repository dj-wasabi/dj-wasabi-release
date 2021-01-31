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


def test_myoutput(capsys):
    djWasabi.generic.debugLog(debug=True, message="We will create a release")
    captured = capsys.readouterr()
    assert captured.out == "We will create a release\n"


def test_myoutput_no_debug(capsys):
    djWasabi.generic.debugLog(debug=False, message="We will create a release")
    captured = capsys.readouterr()
    assert not captured.out


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
    githubUrl = djWasabi.generic.getGithubUrl(owner="dj-wasabi", repository="dj-wasabi-release")
    assert githubUrl == "https://api.github.com/repos/dj-wasabi/dj-wasabi-release"


def test_generic_githubUrl_no_owner():
    """Test the githubUrl function without providing owner.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the owner of the repository."):
        djWasabi.generic.getGithubUrl(repository="dj-wasabi-release")


def test_generic_githubUrl_no_repository():
    """Test the githubUrl function without providing repository.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the name of the repository."):
        djWasabi.generic.getGithubUrl(owner="dj-wasabi")


def test_generic_getString():
    """Test the function to get a string from a string
    :return:
    """
    myString = "mystringhere"
    output = djWasabi.generic.getString(data=myString)
    assert output == "mystringhere"


def test_generic_getString_list():
    """Test the function to get a string from a list
    :return:
    """
    myList = ["my", "string", "here"]
    output = djWasabi.generic.getString(data=myList)
    assert output == "my string here"


def test_generic_getString_list_separator():
    """Test the function to get a string from a list
    :return:
    """
    myList = ["my", "string", "here"]
    output = djWasabi.generic.getString(data=myList, separater=",")
    assert output == "my,string,here"


def test_generic_executeCommand():
    """Test the to execute command to do an ls
    :return:
    """
    command = ["ls", "CHANGELOG.md"]
    output = djWasabi.generic.executeCommand(command=command)
    assert output == "CHANGELOG.md"


def test_generic_executeCommand_no_command():
    """Test the execute command without argument.
    :return:
    """
    with pytest.raises(ValueError, match="Please provide the command we want to execute."):
        djWasabi.generic.executeCommand()


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
