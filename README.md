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
	-h		Will print this help message.
	-l		Will print last created tag.

Note:
	Please make sure that Docker is running and the environment
	variable "CHANGELOG_GITHUB_TOKEN" is set with correct value.
```
