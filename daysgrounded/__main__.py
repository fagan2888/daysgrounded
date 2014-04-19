#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""Manage child(s) grounded days."""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys

import cli

def main():
    """Calls dispatch to process args."""
    return cli.dispatch(sys.argv[1:])

if __name__ == '__main__':
    sys.exit(main())
