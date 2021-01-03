#!/usr/bin/env python

import tempfile
import subprocess


def debugLog(debug=False, message=None):
    if debug:
        print(message)


def compareDictsInLists(source1=None, source2=None):
    # pairs = zip(source1, source2)
    return [i for i in source1 if i not in source2]


def makeTempDir():
    """ Make a temporary directory.

    :rtype: str
    :return: The path to the temporary directory.
    """
    return tempfile.mkdtemp()


def executeCommand(command=None):
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    return proc.communicate()[0].decode().strip('\n')
