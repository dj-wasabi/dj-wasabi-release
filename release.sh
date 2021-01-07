#!/usr/bin/env bash
#
# This script will be used for creating tags and releases for the dj-wasabi related repositories
# in an automated and (hopefully) structured way. :)

set -euo pipefail

function help() {
  echo -e "This script will either provide the last created tag."
  echo -e "or will create a new tag and push this to Github."
  echo -e "\n\t-c <tag>\tCreate a tag named <tag> and pushes this"
  echo -e "\t\t\tinformation to Github and creates a release."
  echo -e "\t-d\t\tWill generate CHANGELOG.md."
  echo -e "\t-h\t\tWill print this help message."
  echo -e "\t-l\t\tWill print last created tag."
  echo -e "\nNote:"
  echo -e "\tPlease make sure that Docker is running and the environment"
  echo -e "\tvariable \"CHANGELOG_GITHUB_TOKEN\" is set with correct value."
  exit 1
}

function getLatestTag() {
  # Print the latest created git tag.
  git describe --abbrev=0
}

function verifyGitTag(){
  # Verify if the provided tag locally exist (1) or not (0).
  local TAG=$1
  git tag | grep -c "^${TAG}$" || true
}

function createRelease(){
  # The "main" function to start creating everything for a single release.
  local VERSION=$1
  local TAG_ALREAD_EXIST
  TAG_ALREAD_EXIST=$(verifyGitTag "${VERSION}")
  if [[ $TAG_ALREAD_EXIST -eq 1 ]]
    then  echo "ERROR - Release already exist"
          exit 1
  fi
  pullGit
  createGitTag "${VERSION}"
  pushGitTag
  createGithubRelease "${VERSION}"
  createGitContributors "${VERSION}"
  updateChangelogMd "${VERSION}"
  pushGit
}

function pullGit(){
  # Do a git pull
  echo "INFO - Pulling changes from Github."
  git pull origin "$(git rev-parse --abbrev-ref HEAD)" > /dev/null 2>&1
}

function pushGit() {
  # Push the changes to Github.
  echo "INFO - Pushing changes to Github."
  git push > /dev/null 2>&1
}

function pushGitTag() {
  # Push the just created git tag.
  echo "INFO - Push tag to Github."
  git push --tags > /dev/null 2>&1
}

function createGitContributors() {
  # Create/Update and commit file with git contributors.
  local VERSION=$1
  if [[ ! -f CONTRIBUTORS ]]
    then  touch CONTRIBUTORS
  fi
  git shortlog -s -n --all --no-merges | awk '{$1=""}1' | sort -u > CONTRIBUTORS
  if [[ $(git status | grep -c 'CONTRIBUTORS' || true) -gt 0 ]]
    then  echo "INFO - Updating CONTRIBUTORS file"
          git add CONTRIBUTORS
          git commit -m "Updating CONTRIBUTORS file for release ${VERSION}" CONTRIBUTORS
  fi
}

function updateChangelogMd() {
  # Update the CHANGELOG.md by running a generator command via Docker.
  local VERSION=${1:-null}
  echo "INFO - Writing CHANGELOG.md file."
  docker run --rm -e CHANGELOG_GITHUB_TOKEN="${GITHUB_TOKEN}" -v "$(pwd)":/usr/local/src/your-app ferrarimarco/github-changelog-generator -u "${GITHUB_USER}" -p "${GITHUB_PROJECT}"  > /dev/null 2>&1

  if [[ "${VERSION}" != "null" ]];then
    if [[ $(git status | grep -c 'CHANGELOG.md' || true) -gt 0 ]]
      then  echo "INFO - Updating CHANGELOG.md file"
            git add CHANGELOG.md
            git commit -m "Updating CHANGELOG.md file for release ${VERSION}" CHANGELOG.md
    fi
  fi
}

function createGitTag() {
  # Create a git tag locally.
  local VERSION=$1
  echo "INFO - Create the tag \"${VERSION}\" locally."
  git tag -a "${VERSION}" -m "${VERSION}"
}

function generateGithubReleaseData() {
  # Generate json data to be POST'ed to Github.
  local VERSION=$1

  cat <<EOF
{
  "tag_name": "${VERSION}",
  "target_commitish": "$(git rev-parse --abbrev-ref HEAD)",
  "name": "${VERSION}",
  "body": "",
  "draft": false,
  "prerelease": false
}
EOF

}

function createGithubRelease() {
  # Create release in Github.
  local VERSION=$1
  local JSON_DATA
  JSON_DATA=$(generateGithubReleaseData "${VERSION}")
  echo "INFO - Create release on Github"
  curl -s -H "Authorization: token ${GITHUB_TOKEN}" --data "${JSON_DATA}" "https://api.github.com/repos/${GITHUB_USER}/${GITHUB_PROJECT}/releases" > /dev/null
}

function getGithubUser() {
  # Find username
  local GITHUB_URL=$1

  if [[ $(echo "${GITHUB_URL}" | grep -c '^https:' ) -eq 1 ]]
    then  GITHUB_USER=$(echo "${GITHUB_URL}" | awk -F '/' '{print $4}')
    else  GITHUB_USER=$(echo "${GITHUB_URL}" | awk -F ':' '{print $2}' | awk -F '/' '{print $1}')
  fi

  echo "${GITHUB_USER}"
}


# Some checks we need to do to make sure we don't run into errors.
# We need at an argument, otherwise we just print help and stop working.
if [[ $# -eq 0 ]]
  then  help
fi

# Validate if we have a "CHANGELOG_GITHUB_TOKEN" environment variable already in our current env
if [[ -z $CHANGELOG_GITHUB_TOKEN ]]
  then  echo "ERROR - We don't have the environment \"CHANGELOG_GITHUB_TOKEN\" set."
        exit 1
fi

# Verify that Docker is runnig.
if [[ $(docker ps > /dev/null 2>&1;echo $?) -ne 0 ]]
  then  echo "ERROR - Docker is not running"
        exit 1
fi

# Get GIT related information
GITHUB_URL=$(git config --get remote.origin.url)
GITHUB_USER=$(getGithubUser "${GITHUB_URL}")
GITHUB_PROJECT=$(echo "${GITHUB_URL}" | xargs basename | sed 's/.git//g')
GITHUB_TOKEN="${CHANGELOG_GITHUB_TOKEN}"

while getopts 'c:dlh' OPTION; do
  case "$OPTION" in
    c)
      createRelease "${OPTARG}"
      ;;

    d)
      updateChangelogMd
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
shift "$(( OPTIND - 1))"
