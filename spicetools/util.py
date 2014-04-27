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
    """Temporary directory manager.
    
    Can function either as a standalone object,
    or as a Context Manager.  In the second role
    the directory is deleted at the end of the context.
    
    Otherwise, either the remove() method must be called
    for each instance, or the cleanup() class method
    must be called (typically in a finally statement).
    
    TempDir(...)
    
    Ctor arguments are passed to tempfile.mkdtemp
    """
    dirs = weakref.WeakKeyDictionary()

    def __init__(self, *args, **kws):
        self._args, self.dirname = (args, kws), None
        self.dirs[self] = None

    def create(self):
        self.remove()
        args, kws = self._args
        self.dirname = tempfile.mkdtemp(*args, **kws)
        _log.info("Creating temp. directory: %s", self.dirname)
        return self
    open = create

    def remove(self):
        if self.dirname is not None:
            _log.info("Removing temp. directory: %s", self.dirname)
            rmrf(self.dirname)
            self.dirname = None
    close = remove

    def __enter__(self):
        if self.dirname is None:
            self.create()
        return self.dirname
    def __exit__(self, A, B, C):
        self.remove()

    @classmethod
    def cleanup(cls):
        for D in cls.dirs.keys():
            D.remove()

    def join(self, *args):
        return os.path.join(self.dirname, *args)
