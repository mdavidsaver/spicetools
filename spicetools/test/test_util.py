# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import unittest

import os, os.path

from .. import util


class TestTempDir(unittest.TestCase):
    def tearDown(self):
        util.TempDir.cleanup()

    def test_noop(self):
        D = util.TempDir()
        self.assertIsNone(D.dirname)

    def test_standalone(self):
        D = util.TempDir().create()
        self.assertIsNotNone(D)
        self.assertIsInstance(D, util.TempDir)
        self.assertIsNotNone(D.dirname)

        DD = D.dirname
        self.assertTrue(os.path.exists(DD))
        self.assertTrue(os.path.isdir(DD))

        D.remove()

        self.assertFalse(os.path.exists(DD))
        self.assertFalse(os.path.isdir(DD))

    def test_global(self):
        A = util.TempDir().create()
        B = util.TempDir().create()

        DA, DB = A.dirname, B.dirname
        self.assertTrue(os.path.isdir(DA))
        self.assertTrue(os.path.isdir(DB))

        util.TempDir.cleanup()

        self.assertFalse(os.path.isdir(DA))
        self.assertFalse(os.path.isdir(DB))

    def test_context(self):
        D = util.TempDir()
        self.assertIsNone(D.dirname)

        with D as DD:
            self.assertIsNotNone(D.dirname)
            self.assertEqual(DD, D.dirname)
            self.assertTrue(os.path.exists(DD))
            self.assertTrue(os.path.isdir(DD))

        self.assertIsNone(D.dirname)
        self.assertFalse(os.path.exists(DD))
        self.assertFalse(os.path.isdir(DD))

    def test_rmrf(self):

        with util.TempDir() as DD:
            F1 = os.path.join(DD,'file1')
            with open(F1, 'w') as FD:
                FD.write(F1)
            D1 = os.path.join(DD,'dir1')
            os.mkdir(D1)
            F2 = os.path.join(DD,'dir1','file2')
            with open(F2, 'w') as FD:
                FD.write(F2)

            self.assertTrue(os.path.isdir(D1))
            self.assertTrue(os.path.isfile(F1))
            self.assertTrue(os.path.isfile(F2))

        self.assertFalse(os.path.isdir(D1))
        self.assertFalse(os.path.isfile(F1))
        self.assertFalse(os.path.isfile(F2))


if __name__=='__main__':
    unittest.main()
