# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import unittest

import os.path

from .. import io
from ..util import TempDir

# test data directory
_dir = os.path.dirname(__file__)

class TestSpice(unittest.TestCase):
    def test_read(self):
        F = os.path.join(_dir, 'opsim-real-bin.raw')

        D = io.loadspice(F)
        self.assertEqual(1, len(D))

        V = D['default']
        self.assertEqual(32, len(V))

if __name__=='__main__':
    unittest.main()
