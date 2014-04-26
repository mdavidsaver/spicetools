# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import logging
_log = logging.getLogger(__name__)

import os, os.path
import tempfile, weakref

from PyQt4 import QtCore

# restriction on names of analyses and expression variables
svarname = QtCore.QRegExp("[A-Za-z_][A-Za-z0-9_]*")

def rmrf(dname):
    "Recursively remove a directory an all its contents"
    for path, dirs, files in os.walk(dname, topdown=False):
        for F in files:
            os.remove(os.path.join(path, F))
        for D in dirs:
            os.rmdir(os.path.join(path, D))
    os.rmdir(dname)

class TempDir(object):
    dirs = weakref.WeakKeyDictionary()

    def __init__(self, *args, **kws):
        self.dirname = tempfile.mkdtemp(*args, **kws)
        _log.info("Creating temp. directory: %s", self.dirname)
        self.dirs[self] = self.dirname
    def remove(self):
        if self.dirname is not None:
            _log.info("Removing temp. directory: %s", self.dirname)
            rmrf(self.dirname)
            self.dirname = None
    close = remove
    def __del__(self):
        self.remove()

    @classmethod
    def cleanup(cls):
        for D in cls.dirs.keys():
            D.remove()

    def join(self, *args):
        return os.path.join(self.dirname, *args)
