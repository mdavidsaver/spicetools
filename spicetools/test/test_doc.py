# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import unittest, doctest

def load_tests(loader, tests, ignore):
    from .. import run
    tests.addTests(doctest.DocTestSuite(run))
    return tests
