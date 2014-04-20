#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""Shared constants and funtions."""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date
import sys
import pickle
from pkg_resources import resource_filename

import globalcfg

# set correct path to all data files
try:
    DATA_PATH = resource_filename(__name__, globalcfg.USAGE_FILE)
    DATA_PATH = DATA_PATH.replace(globalcfg.USAGE_FILE, '')
except:
    # if current module is frozen, use library.zip path
    if hasattr(sys, 'frozen'):
        DATA_PATH = sys.prefix
        DATA_PATH.strip('/')
        DATA_PATH += '/'

USAGE_FILE = DATA_PATH + globalcfg.USAGE_FILE
BANNER_FILE = DATA_PATH + globalcfg.BANNER_FILE
LICENSE_FILE = DATA_PATH + globalcfg.LICENSE_FILE

DATA_FILE = DATA_PATH + 'daysgrounded.pkl'
LOG = True
LOG_FILE = DATA_PATH + 'daysgrounded_log.pkl'
MAX_DAYS = 99
MAX_DAYS_STR = str(MAX_DAYS)

def update_file(childs, last_upd):
    """
    Update data file and log file.

    The log file creates an history to be used in the future.
    """
    with open(DATA_FILE, 'wb') as f_out:
        pickle.dump(childs, f_out)
        pickle.dump(last_upd, f_out)
##        pickle.dump([childs, last_upd], f_out)
    if LOG:
        with open(LOG_FILE, 'ab') as f_out:
            pickle.dump([childs, last_upd], f_out)

def create_file():
    """Create new data file and log file."""
    # use lower case letters or names
    childs = {'t': 0, 's': 0}
    last_upd = date.today()
    update_file(childs, last_upd)
    return childs, last_upd

def read_file():
    """Reads and returns childs and last_upd from the data file."""
    with open(DATA_FILE, 'rb') as f_in:
        childs = pickle.load(f_in)
        last_upd = pickle.load(f_in)
##        [childs, last_upd] = pickle.load(f_in)
    return childs, last_upd

def usage():
    """Returns usage text, read from a file."""
    with open(USAGE_FILE) as f_in:
        return f_in.read()

def banner():
    """Returns banner text."""
    banner_txt = ('\n' + globalcfg.NAME + ' version ' + globalcfg.VERSION +
                  ', ' + globalcfg.COPYRIGHT + '\n')
    with open(BANNER_FILE) as f_in:
        return banner_txt + f_in.read()

def license_():
    """Returns license text, read from a file."""
    with open(LICENSE_FILE) as f_in:
        return f_in.read()
