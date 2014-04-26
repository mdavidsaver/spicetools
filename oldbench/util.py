# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import os, os.path
import tempfile

def rmrf(dname):
    "Recursively remove a directory an all its contents"
    for path, dirs, files in os.walk(dname, topdown=False):
        for F in files:
            os.remove(os.path.join(path, F))
        for D in dirs:
            os.rmdir(os.path.join(path, D))
    os.rmdir(dname)

class TempDir(object):
    def __init__(self, *args, **kws):
        self._A = (args, kws)
    def __enter__(self):
        args, kws = self._A
        self.dirname = tempfile.mkdtemp(*args, **kws)
        return self.dirname
    def __exit__(self, A, B, C):
        if os.path.isdir(self.dirname):
            rmrf(self.dirname)
