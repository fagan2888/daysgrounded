#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""Blablabla."""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import date
import sys
from os import path

import colorama

import shared
import gui

def print_state(childs, last_upd):
    """Prints current state for each child."""
##    for child in childs:
##        print child, childs[child],
    for child, days in enumerate(childs):
        print(child, days,)
    print(str(last_upd))

def man_upd_days(argv, childs, last_upd):
    """
    Manual update based on args.

    First it checks all args and only if all are correct are they processed.
    """
    # check args
    for arg in argv:
        if '-' in arg:
            child, days = str.lower(arg).split('-')
        elif '+' in arg:
            child, days = str.lower(arg).split('+')
        else:
            args_ok = False
            break

        try:
            days = int(days)
        except ValueError:
            args_ok = False
            break

        if ((child in childs) and
           (-shared.MAX_DAYS <= days <= shared.MAX_DAYS)):
            args_ok = True
        else:
            args_ok = False
            break

    if args_ok: # process args
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
                childs[child] = min(shared.MAX_DAYS, childs[child])
            else:
                childs[child] = max(0, childs[child])
        last_upd = date.today()
        shared.update_file(childs, last_upd)
        print_state(childs, last_upd)
    else:
        print(colorama.Fore.RED + 'Erro: argumento incorreto ' + arg + '\n')
        print(colorama.Fore.RESET + shared.usage())

def auto_upd_days(childs, last_upd):
    """Automatic update based on current date vs last update date."""
    print_state(childs, last_upd)
    right_now = date.today()
    days_to_remove = (right_now - last_upd).days # convert to days and assign
    for child in childs:
        childs[child] -= days_to_remove
        childs[child] = max(0, childs[child])
    last_upd = right_now
    shared.update_file(childs, last_upd)
    print_state(childs, last_upd)

def dispatch(argv):
    """Print banner, read/create data & log file and process args."""
    colorama.init()

    print(shared.banner())

    if path.isfile(shared.DATA_FILE): # if file exists
        childs, last_upd = shared.read_file()
    else:
        childs, last_upd = shared.create_file()

    if argv: # any args?
        arg0 = str.lower(argv[0])
        if arg0 in ['-h', '--help']:
            print(shared.usage())
        elif arg0 in ['-v', '--version']:
            print('Vers�o', shared.__version__)
        elif arg0 in ['-l', '--license']:
            print(shared.license_())
        elif arg0 in ['-a', '--auto']:
            auto_upd_days(childs, last_upd)
        else:
            man_upd_days(argv, childs, last_upd)
    else:
        gui.start(childs, last_upd)
    sys.exit(0) # ToDo: other return codes
