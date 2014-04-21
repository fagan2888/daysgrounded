#!/usr/bin/env python
# -*- coding: latin-1 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

##import sys
from setuptools import setup, find_packages
#import py2exe
##from cx_Freeze import setup, Executable

from daysgrounded.globalcfg import NAME, VERSION, DATA_FILES
from daysgrounded import (DESC, LICENSE, URL, KEYWORDS, CLASSIFIERS, #PACKAGES,
                          ENTRY_POINTS, PKG_DATA)

AUTHOR = 'Joao Matos'
SCRIPT = NAME + '\\__main__.py'

### cx_Freeze config for bdist_msi
##bdist_msi_options = {
##    'upgrade_code': '{66620F3A-DC3A-11E2-B341-002219E9B01E}',
##    'add_to_path': False,
##    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (AUTHOR, NAME),
##    }
##build_exe_options = {'includes': ['atexit', 'PySide.QtNetwork']}
### GUI applications require a different base on Windows
##base = None
##if sys.platform == 'win32':
##    base = 'Win32GUI'
##exe = Executable(script=SCRIPT, base=base) #, icon='daysgrounded.ico')

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

      packages=find_packages(exclude=['tests*']),
      #packages=PACKAGES,

      # to create the Scripts exe using bdist_wininst build option
      entry_points=ENTRY_POINTS,

      install_requires=open('requirements.txt').read(),
      #install_requires=open('requirements.txt').read().splitlines(),

      # used only if the package is not in PyPI, but exists as an egg,
      # sdist format or as a single .py file
      # see http://peak.telecommunity.com/DevCenter/setuptools#dependencies-that-aren-t-in-pypi
      #dependency_links = ['http://host.domain.local/dir/'],

      include_package_data=True,
      package_data=PKG_DATA,

      # py2exe config
      #console=[SCRIPT],
      #data_files=DATA_FILES,

##      # cx_Freeze config for bdist_msi
##      executables=[exe],
##      options={'bdist_msi': bdist_msi_options, 'build_exe': build_exe_options}
     )
