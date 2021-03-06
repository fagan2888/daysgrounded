#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2009-2015 Joao Carlos Roseta Matos
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Processes command line arguments and updates child's records."""

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime as dt
# import io  # Python 3 compatibility
import sys

# from builtins import input  # Python 3 compatibility
import colorama as clrm

import common
import localization as lcl
import shared as shrd


def print_state(childs, last_upd):
    """Prints current state for each child."""
    for child in childs:
        print(child, childs[child])
    print(str(last_upd))


def man_upd(argv, childs, last_upd):
    """Manual update based on args.

    First it checks all args and only if all are correct are they processed.
    """
    arg_nok = ''
    args_ok = False

    # check args
    for arg in argv:
        if '-' in arg:
            child, days = str.lower(arg).split('-')
        elif '+' in arg:
            child, days = str.lower(arg).split('+')
        else:
            arg_nok = arg
            args_ok = False
            break

        try:
            days = int(days)
        except ValueError:  # as error:
            arg_nok = arg
            args_ok = False
            break

        if ((child in childs) and
           (-shrd.MAX_DAYS <= days <= shrd.MAX_DAYS)):
            args_ok = True
        else:
            arg_nok = arg
            args_ok = False
            break

    if args_ok:  # process args
        print_state(childs, last_upd)
        for arg in argv:
            if '-' in arg:
                child, days = str.lower(arg).split('-')
                days = -int(days)
            elif '+' in arg:
                child, days = str.lower(arg).split('+')
                days = int(days)

            childs[child] += days
            if childs[child] > 0:
                childs[child] = min(shrd.MAX_DAYS, childs[child])
            else:
                childs[child] = max(0, childs[child])
        last_upd = dt.date.today()
        shrd.update_file(childs, last_upd)
        print_state(childs, last_upd)
    else:
        print(clrm.Fore.RED + lcl.WRONG_ARG + arg_nok + '\n')
        print(clrm.Fore.RESET + common.usage())


def auto_upd(childs, last_upd):
    """Automatic update based on current date vs last update date."""
    print_state(childs, last_upd)
    last_upd = shrd.auto_upd_datafile(childs, last_upd)
    print_state(childs, last_upd)


def start(argv):
    """Print banner, read/create data & log file and process args."""
    clrm.init()

    print(common.banner())
    childs, last_upd = shrd.open_create_datafile()

    arg0 = argv[0]
    if arg0 in ['-a', '--auto']:
        auto_upd(childs, last_upd)
    elif arg0 in ['-h', '--help']:
        print(common.usage())
    elif arg0 in ['-l', '--license']:
        print(common.license_())
    elif arg0 in ['-V', '--version']:
        print(lcl.VERSION, common.version())
    else:
        man_upd(argv, childs, last_upd)

    sys.exit(0)  # ToDo: other return codes


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    pass
