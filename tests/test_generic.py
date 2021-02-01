"""File containing tests specific for the djWasabi/generic.py file."""

import sys
import os
import requests
import pytest

currentPath = os.path.dirname(os.path.realpath(__file__))
rootPath = os.path.join(currentPath, "..")
libraryDir = os.path.join(rootPath, "lib")
sys.path.append(libraryDir)
from djWasabi import djWasabi


def test_generic_debugLog(capsys):
    djWasabi.generic.debugLog(debug=True, message="We will create a release")
    captured = capsys.readouterr()
    assert captured.out == "We will create a release\n"


def test_generic_debugLog_no_debug(capsys):
    djWasabi.generic.debugLog(debug=False, message="We will create a release")
    captured = capsys.readouterr()
    assert not captured.out


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
