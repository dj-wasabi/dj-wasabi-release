#!/usr/bin/env python
"""This script will checkout each git repository and execute the provided script, based on configuration found in 'dj-wasabi.yml'."""

import os
import sys
import argparse
import shutil
import subprocess
currentPath = os.path.dirname(os.path.realpath(__file__))
libraryDir = os.path.join(currentPath, "lib")
sys.path.append(libraryDir)
from djWasabi import djWasabi


def get_args():
    """Support the command-line arguments listed below."""
    parser = argparse.ArgumentParser(description="""This script will checkout each git repository
    and execute the provided script, based on configuration found in 'dj-wasabi.yml'.""")
    parser.add_argument('-D', '--debug', required=False, action='store_true', help="""Print some
    debug information""")
    parser.add_argument('-s', '--script', required=False, action='store',
                        help='The script we want to execute on all repositories.', type=str)
    return parser.parse_args()


def getConfigScript(scripts: list = None, script: str = None) -> dict:
    """ Get the configuration for provided script.
    """
    for entry in scripts:
        name = entry['name']
        if name == script:
            return entry
    return None


def main():
    global is_debug
    args = get_args()
    is_debug = args.debug
    script = args.script
    yamlConfig = djWasabi.config.readConfig(rootPath=currentPath)

    repositories = yamlConfig['repositories']
    scripts = yamlConfig['scripts']
    tmpDir = djWasabi.generic.makeTempDir()
    djWasabi.generic.debugLog(debug=is_debug, message="TMP directory: {r}".format(r=tmpDir))

    # Get configuration for the provided script.
    owner, _ = djWasabi.git.readRepository(debug=is_debug)
    scriptConfig = getConfigScript(scripts=scripts, script=script)
    djWasabi.generic.debugLog(debug=is_debug, message="Script config: {r}".format(r=scriptConfig))
    if scriptConfig is None:
        sys.exit('Script is not configured to run.')

    # Loop thru the repositories
    for repo in repositories:
        djWasabi.generic.debugLog(debug=is_debug, message="Repo: {r}".format(r=repo))
        script_execution = []
        script_path = ""
        _name = repo['name']
        _repo = djWasabi.generic.getRepoUrl(owner=owner, repository=_name)

        os.chdir(tmpDir)
        if scriptConfig['clone']:
            djWasabi.git.clone(name=_name, repositorie=_repo)
            gitCloneDir = os.path.join(tmpDir, _name)
            os.chdir(gitCloneDir)
            djWasabi.generic.debugLog(debug=is_debug, message="Repo tmpdir {r}".format(r=gitCloneDir))

        # Create
        script_path = os.path.join(currentPath, scriptConfig['name'])
        script_execution.append(script_path)
        if is_debug:
            script_execution.append("-D")
        for _arg in scriptConfig['args']:
            # TODO should be way more better than this!
            if _arg == "-r":
                script_execution.append("-r")
                script_execution.append("\"{r}\"".format(r=_repo))
                continue
        djWasabi.generic.debugLog(debug=is_debug, message="Executing script {r}".format(r=script_execution))
        proc = subprocess.Popen(script_execution, shell=False, stdout=subprocess.PIPE)
        output = proc.communicate()[0].decode().strip('\n')
        if is_debug:
            print(output)

    shutil.rmtree(tmpDir)


if __name__ == "__main__":
    main()
