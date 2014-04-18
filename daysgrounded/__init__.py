"""Manage child(s) grounded days."""

__all__ = [
    '__title__', '__version__',
    '__desc__', '__license__', '__url__',
    '__author__', '__email__',
    '__copyright__',
    '__keywords__', '__classifiers__',
    #'__packages__',
    '__entrypoints__', '__pkgdata__'
]

__title__ = 'daysgrounded'
__version__ = '0.0.7'

__desc__ = __doc__.strip()
__license__ = 'GNU General Public License v2 or later (GPLv2+)'
__url__ = 'https://github.com/jcrmatos/DaysGrounded'

__author__ = 'Joao Matos'
__email__ = 'jcrmatos@gmail.com'

__copyright__ = 'Copyright 2014 Joao Matos'

__keywords__ = 'days grounded'
__classifiers__ = [
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
        'Topic :: Other/Nonlisted Topic',
        # Use below to prevent any unwanted publishing
        #'Private :: Do Not Upload'
    ]

#__packages__ = ['daysgrounded']

__entrypoints__ = {
        'console_scripts': ['daysgrounded = daysgrounded.__main__:main'],
        #'gui_scripts': ['app_gui = daysgrounded.daysgrounded:start']
    }

__pkgdata__ = {'daysgrounded': ['*.txt']}
#__pkgdata__= {'': ['*.txt'], 'daysgrounded': ['*.txt']}
