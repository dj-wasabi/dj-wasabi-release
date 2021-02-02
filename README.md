# dj-wasabi-release

<img align="right"  src="https://raw.githubusercontent.com/dj-wasabi/dj-wasabi-release/main/.github/image.jpg">

**Table of contents**:

- [dj-wasabi-release](#dj-wasabi-release)
  * [Introduction](#introduction)
  * [Github Actions](#github-actions)
- [Scripts](#scripts)
  * [release.py](#releasepy)
  * [label.py](#labelpy)
  * [repository.py](#repositorypy)
- [Configuration](#configuration)
  * [labels](#labels)
  * [script](#script)
  * [Repository](#repository)

![MasterRun](https://github.com/dj-wasabi/dj-wasabi-release/workflows/MasterRun/badge.svg) ![run-all](https://github.com/dj-wasabi/dj-wasabi-release/workflows/run-all/badge.svg) ![Python test_djWasabi](https://github.com/dj-wasabi/dj-wasabi-release/workflows/Python%20test_djWasabi/badge.svg)

## Introduction

This is a "private" repository that contains the script(s) that I use for maintaining my own set of repositories.

Documentation available [here](https://dj-wasabi.github.io/dj-wasabi-release/build/html/).

## Github Actions

Several actions are part of this repository.

| job | branch | Description |
|-----|-|---|
| main | `main` | After each merge/commit into `main` the `CHANGELOG.md` will be updated and committed in the repository. |
| python-package | `<ALL>` | If a `git clone` needs to be executed. |
| run-all | `main` | It will execute the `run-all.py` script to run all the scripts.|

The `main` Github Action is also used by other git repositories.

# Scripts

## release.py

This is a script that will create a tag in the current repository where it is executed and will do the following:

1. Create a tag;
2. Will push this tag to Github;
3. Will create a "release" in Github;
4. Commits `CONTRIBUTORS` file where needed;
5. Commits `CHANGELOG.md` file where needed;
6. Pushes the commits to Github

Example `help` message:

```bash
$ ./release.py -h
usage: release.py [-h] [-c CREATE] [-d] [-D] [-l] [-t TOKEN]

This script will create a tag, update where needed the CHANGELOG.md and CONTRIBUTORS file and create a release in Github with the provided version. Can also provided the latest tag or generate (without commit) a CHANGELOG.md.

optional arguments:
  -h, --help            show this help message and exit
  -c CREATE, --create CREATE
                        Create a tag and a complete release with provided version.
  -d, --docs            Create and/or Update the CHANGELOG.md file.
  -D, --debug           Print some debug information
  -l, --list            Provides the latest created tag in this repository.
  -t TOKEN, --token TOKEN
                        The Github API token, or set environment variable "CHANGELOG_GITHUB_TOKEN".
```

## label.py

A script that reads the information from the `dj-wasabi.yml` file and based on a key named `labels` it
will create/delete/update labels in the git repository on Github.

```bash
$ ./label.py -h
usage: label.py [-h] [-D] [-r REPO] [-t TOKEN]

This script is responsible for creating/deleting labels in current git repositoryin Github based on a configuration cound in the 'dj-wasabi.yml' file.

optional arguments:
  -h, --help            show this help message and exit
  -D, --debug           Print some debug information
  -r REPO, --repo REPO  The name of the repository
  -t TOKEN, --token TOKEN
                        The Github API token.
```

## repository.py

A script that reads the information from the `dj-wasabi.yml` file and will configure the repositories with wiki or projects enabled.

```bash
$ ./repository.py -h
usage: repository.py [-h] [-D] [-r REPO] [-t TOKEN]

This script is responsible for configuring the git repositories based on a configuration found in the 'dj-wasabi.yml' file.

optional arguments:
  -h, --help            show this help message and exit
  -D, --debug           Print some debug information
  -r REPO, --repo REPO  The name of the repository. Example "git@github.com:dj-wasabi/consul.git"
  -t TOKEN, --token TOKEN
                        The Github API token.
```

# Configuration

## labels

A list with labels.

| Configuration | Description |
|------|---|
| name | The name of the label. |
| color | The colorcode of the label, without `#`. |
| description | The description of the label..|

## script

An configuration which contains a list of scripts that will be executed on all repositories (found in key `repositories`).


| Configuration | Description |
|------|---|
| name | The name of the script. |
| clone | If a `git clone` needs to be executed. |
| args | A list with arguments that needs to be appended for correct execution.|


## Repository

The keys `repository_defaults` contains the default configuration for all repositires. The configuration in the `repositries` will override de defaults specifically for this repository.

| Configuration | Description |
|------|---|
| wiki | Either `true` to enable the wiki for this repository or `false` to disable it. |
| issues | Either `true` to enable issues for this repository or `false` to disable them. |
| projects| Either `true` to enable projects for this repository or `false` to disable them. |
| archived | `true` to archive this repository. Note: You cannot unarchive repositories through the API. |
| visibility | Can be `public` or `private`.|
| allow_squash_merge | Either `true` to allow squash-merging pull requests, or `false` to prevent squash-merging.|
| allow_merge_commit | Either `true` to allow merging pull requests with a merge commit, or `false` to prevent merging pull requests with merge commits.|
| allow_rebase_merge | Either `true` to allow automatically deleting head branches when pull requests are merged, or `false` to prevent automatic deletion.|
| delete_branch_on_merge | `true` to archive this repository. Note: You cannot unarchive repositories through the API. |
