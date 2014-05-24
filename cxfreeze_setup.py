#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys
from cx_Freeze import setup, Executable

from daysgrounded.globalcfg import NAME, VERSION, DATA_FILES
from daysgrounded import (DESC, LICENSE, URL, KEYWORDS, CLASSIFIERS)

AUTHOR = 'Joao Matos'
SCRIPT = NAME + '/__main__.py'
TARGET_NAME = NAME + '.exe'

base = None
# GUI applications require a different base on Windows
if sys.platform == 'win32':
    base = 'Win32GUI'

##if 'bdist_msi' in sys.argv:
##    sys.argv += ['--install-script', 'install.py']

##bdist_msi_options = {
##    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (AUTHOR, NAME),
##    #'upgrade_code': '{66620F3A-DC3A-11E2-B341-002219E9B01E}',
##    #'add_to_path': False,
##    }

build_exe_options = dict(compressed=True,
                         #excludes=["macpath", "PyQt4"],
                         #includes=['atexit', 'PySide.QtNetwork'],
                         include_files=['AUTHORS.txt',
                                        'CHANGES.txt',
                                        'LICENSE.txt',
                                        'README.txt',
                                        'README.rst',
                                        NAME],
                         # append any extra module by extending the list below -
                         # "contributed_modules+["lxml"]"
                         #packages=contributed_modules
                        )

setup(name=NAME,
      version=VERSION,
      description=DESC,
      long_description=open('README.txt').read(),
      #long_description=(read('README.txt') + '\n\n' +
      #                  read('CHANGES.txt') + '\n\n' +
      #                  read('AUTHORS.txt')),
      license=LICENSE,
      url=URL,
      author=AUTHOR,
      author_email='jcrmatos@gmail.com',

      keywords=KEYWORDS,
      classifiers=CLASSIFIERS,

      executables=[Executable(script=SCRIPT,
                              base=base,
                              compress=True,
                              #icon="web2py.ico",
                              targetName=TARGET_NAME,
                              #copyDependentFiles=True
                             )],

      options=dict(build_exe=build_exe_options),
##      options=dict(bdist_msi=bdist_msi_options,
##                   build_exe=build_exe_options}),
##      scripts=['install.py']
     )
