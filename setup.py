#!/usr/bin/env python
# -*- coding: latin-1 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from setuptools import setup, find_packages
#import py2exe

from daysgrounded.globalcfg import NAME, VERSION, DATA_FILES
from daysgrounded import (DESC, LICENSE, URL, KEYWORDS, CLASSIFIERS, #PACKAGES,
                          ENTRY_POINTS, PKG_DATA)

setup(name=NAME,
      version=VERSION,
      description=DESC,
      long_description=open('README.txt').read(),
      #long_description=(read('README.txt') + '\n\n' +
      #                  read('CHANGES.txt') + '\n\n' +
      #                  read('AUTHORS.txt')),
      license=LICENSE,
      url=URL,
      author='Joao Matos',
      author_email='jcrmatos@gmail.com',

      keywords=KEYWORDS,
      classifiers=CLASSIFIERS,

      packages=find_packages(exclude=['tests*']),
      #packages=PACKAGES,

      entry_points=ENTRY_POINTS,
      install_requires=open('requirements.txt').read(),
      #install_requires=open('requirements.txt').read().splitlines(),

      include_package_data=True,
      package_data=PKG_DATA,

      # py2exe config
      #console=[NAME + '\\__main__.py'],
      #data_files=DATA_FILES
      )
