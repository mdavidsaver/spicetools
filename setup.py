#!/usr/bin/env python

from distutils.core import setup

setup(name='spicetools',
      version='1.0',
      description='Tools for working with spice simulation (ngspice mainly)',
      author='Michael Davidsaver',
      author_email='mdavidsaver@gmail.com',
      url='http://github.com/mdavidsaver/spicetools',
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
      packages = ['spicetools',
                  'spicetools.bench',
                  'spicetools.view',
                  'spicetools.test',
                  ],
      package_data={
          'spicetools.test':['*.raw']
          },
      scripts = ['spice2hdf',
                 'spicebench',
                 'spiceviewer',
                 'spicerunner'
                 ],
)
