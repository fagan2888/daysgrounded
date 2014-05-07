#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Global configuration."""

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        #unicode_literals # must be removed for py2exe setup
                       )

USAGE_FILE = 'usage.txt'
#USAGE_FILE = 'usage_en.txt'
BANNER_FILE = 'banner.txt'
#BANNER_FILE = 'banner_en.txt'
LICENSE_FILE = 'LICENSE.txt'

NAME = 'daysgrounded'
VERSION = '0.0.13'
COPYRIGHT = 'Copyright 2014 Joao Matos'

DATA_FILES = [('', [NAME + '\\' + USAGE_FILE]),
              ('', [NAME + '\\' + BANNER_FILE]),
              ('', [NAME + '\\' + LICENSE_FILE])]
