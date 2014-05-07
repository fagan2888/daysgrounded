#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Manage child(s) grounded days."""

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        #unicode_literals
                       )
# The above unicode_literals import prevents setup.py from working.
# It seems to be a bug in setuptools.

import sys
from os import path

sys.path.insert(1, path.dirname(__file__)) # add path to PYTHONPATH

__all__ = ['DESC', 'LICENSE', 'URL', 'KEYWORDS', 'CLASSIFIERS', #'PACKAGES',
           'ENTRY_POINTS', 'PKG_DATA']

DESC = __doc__.strip()
LICENSE = 'GNU General Public License v2 or later (GPLv2+)'
URL = 'https://github.com/jcrmatos/DaysGrounded'
KEYWORDS = 'days grounded'
CLASSIFIERS = [# Use below to prevent any unwanted publishing
               #'Private :: Do Not Upload'
               'Development Status :: 4 - Beta',
               'Environment :: Console',
               'Environment :: Win32 (MS Windows)',
               'Intended Audience :: End Users/Desktop',
               'Intended Audience :: Developers',
               'Natural Language :: English',
               'Natural Language :: Portuguese',
               'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.4',
               'Topic :: Other/Nonlisted Topic']

#PACKAGES = ['daysgrounded']

ENTRY_POINTS = dict(console_scripts=['daysgrounded=daysgrounded.__main__:main'],
                    #gui_scripts=['app_gui=daysgrounded.daysgrounded:start']
                   )

PKG_DATA = dict(daysgrounded=['usage.txt', 'LICENSE.txt', 'banner.txt'])
#PKG_DATA = {'': ['*.txt'], 'daysgrounded': ['*.txt']}
