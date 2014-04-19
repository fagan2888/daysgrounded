#!/usr/bin/env python
# -*- coding: latin-1 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from setuptools import setup, find_packages
#import py2exe

#from daysgrounded import *
from daysgrounded import (__title__, __version__,
                          __desc__, __license__, __url__,
                          __author__, __email__,
                          __keywords__, __classifiers__,
                          #__packages__,
                          __entrypoints__, __pkgdata__)

setup(
    name=__title__,
    version=__version__,

    description=__desc__,
    long_description=open('README.txt').read(),
    #long_description=(read('README.txt') + '\n\n' +
    #                  read('CHANGES.txt') + '\n\n' +
    #                  read('AUTHORS.txt')),
    license=__license__,
    url=__url__,

    author=__author__,
    author_email=__email__,

    keywords=__keywords__,
    classifiers=__classifiers__,

    packages=find_packages(exclude=['tests*']),
    #packages=__packages__,

    entry_points=__entrypoints__,
    install_requires=open('requirements.txt').read(),
    #install_requires=open('requirements.txt').read().splitlines(),

    include_package_data=True,
    package_data=__pkgdata__,

    #console=['daysgrounded\\__main__.py']
)
