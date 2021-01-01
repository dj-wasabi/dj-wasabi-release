# dj-wasabi-release

## Introduction

This is a "private" repository that contains the script(s) that I use for maintaining my own set of repositories.

### release

This is a script that will create a tag in the current repository where it is executed and will do the following:

1. Create a tag;
2. Will push this tag to Github;
3. Will create a "release" in Github;
4. Commits `AUTHORS` file where needed;
5. Commits `CHANGELOG.md` file where needed;
6. Pushes the commits to Github

Example `help` message:

```bash
$ ./release.sh -h
This script will either provide the last created tag.
or will create a new tag and push this to Github.

	-c <tag>	Create a tag named <tag> and pushes this
			information to Github and creates a release.
	-d		Will generate CHANGELOG.md.
	-h		Will print this help message.
	-l		Will print last created tag.

Note:
	Please make sure that Docker is running and the environment
	variable "CHANGELOG_GITHUB_TOKEN" is set with correct value.
```

### label

A script that reads the information from the `dj-wasabi.yml` file and based on a key named `labels` it
will create/delete/update labels in the git repository on Github.

```bash
$ ./label.py -h
usage: label.py [-h] [-D]

This script is responsible for creating/deleting labels in current git repository in Github based on a configuration cound in the 'dj-wasabi.yml' file.

optional arguments:
  -h, --help   show this help message and exit
  -D, --debug  Print some debug information
```

