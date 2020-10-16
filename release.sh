#!/usr/bin/env bash

set -euo pipefail

function help() {
  echo -e "This is the help message.\n"
  echo -e "\c-l\t\tCreate a tag"
  echo -e "\t-l\t\tWill show last tag"
  exit 1
}

function getLatestTag() {
  git describe --abbrev=0
}

function verifyGitTag(){
  local TAG=$1
  git tag | grep "^${TAG}$" | wc -l
}

function createRelease(){
  local VERSION=$1
  local TAG_ALREAD_EXIST=$(verifyGitTag $VERSION)
  if [[ $TAG_ALREAD_EXIST -eq 1 ]]
    then  echo "ERROR - Release already exist"
          exit 1
  fi
  createGitTag $VERSION
}

function createGitTag() {
  local VERSION=$1
  echo "git tag -a $VERSION -m $VERSION"
}


if [[ $# -eq 0 ]]
  then  help
fi

while getopts 'c:lh' OPTION; do
  case "$OPTION" in
    c)
      createRelease $OPTARG
      ;;

    l)
      getLatestTag
      ;;

    h)
      help
      exit 0
      ;;

    ?)
      help
      exit 1
      ;;
  esac
done
shift "$(($OPTIND -1))"

# Get GIT related information
GITHUB_URL=$(git config --get remote.origin.url)
GITHUB_USER=$(echo $GITHUB_URL | awk -F ':' '{print $2}' | awk -F '/' '{print $1}')
GITHUB_PROJECT=$(echo $GITHUB_URL | xargs basename | sed 's/.git//g')

echo $GITHUB_PROJECT
