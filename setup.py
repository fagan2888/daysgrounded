from days_grounded import __version__

##import os
##import sys

from setuptools import setup, find_packages

##def publish():
##    os.system('python setup.py sdist upload')
##
##if sys.argv[-1] == 'publish':
##    publish()
##    sys.exit()
##
setup(
    name='days_grounded',
    version=__version__,
    description='Days grounded description',
    long_description='README.txt',
    author='Joao Matos',
    author_email='jcrmatos@gmail.com',
    url='http://www.github.com/jcrmatos/days_grounded',
    license='LICENSE.txt',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'app_con = days_grounded.days_grounded:main'
        ],
        'gui_scripts': [
            'app_gui = days_grounded_gui.days_grounded:main'
        ]
    },
    keywords='days grounded',
    classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Natural language :: Portuguese',
    'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Topic :: Other/Nonlisted Topic'
    ]
)
