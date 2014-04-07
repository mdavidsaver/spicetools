#!/usr/bin/env python

from distutils.core import setup

setup(name='spice2hdf',
      version='1.0',
      description='Convert spice output files to an hdf5 format',
      author='Michael Davidsaver',
      author_email='mdavidsaver@gmail.com',
      url='http://github.com/mdavidsaver/spice2hdf',
      classifiers = [
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Environment :: X11 Applications :: Qt",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2 :: Only",
          "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
      ],
      license='GPL3+',
      packages = ['spiceview'],
      py_modules = ['spice2hdf'],
      scripts = ['spice2hdf','spiceviewer'],
)
