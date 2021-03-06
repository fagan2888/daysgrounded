daysgrounded
============

Allows you to manage your kid's grounded days (simple app for trying Python programming and testing procedures).

Description and features
------------------------

**Description**

Allows you to manage your kid's grounded days (simple app for trying Python programming and testing procedures).

Although the code is OS independent, I'm only able to test it in console (Windows Cmd) and Windows GUI.

You shouldn't use this because it's just a fake app for allowing me to try Python programming and testing procedures.

**Features:**

* Saves a log file with all changes.
* Saves grounded days total per child and last update date.
* Allows changes in CLI and GUI (this last one has different widgets for the same function).

Installation, usage and options
-------------------------------

**Installation**

.. code:: bash

    $ pip install daysgrounded

**Usage**

.. code:: bash

    $ daysgrounded

**Options**

.. code:: bash

    $ daysgrounded -h
	
    usage: daysgrounded [-option | child+/-days...]

    optional arguments:
      -a, --auto            auto update based on date
      -h, --help            show this help message and exit
      -l, --license         show license
      -V, --version         show version
      child+/-days          eg. t+1 s-1

    No arguments starts GUI (Graphical User Interface).
    Maximum of 99 days.

Resources and contributing
--------------------------

**Resources**

* `Repository PyPI <https://pypi.python.org/pypi/daysgrounded>`_
* `Documentation PyPI <http://pythonhosted.org/daysgrounded>`_
* `Repository Github <https://github.com/jcrmatos/daysgrounded>`_
* `Documentation Read the Docs <http://daysgrounded.readthedocs.org>`_

**Contributing**

If Other repository above is Github or compatible, follow these guidelines for contributing:

1. Fork the `repository`_ .
2. Make a branch of master and commit your changes to it.
3. Ensure that your name is added to the end of the AUTHORS.rst file using the format:
   ``Name <email@domain.com>``
4. Submit a Pull Request to the master branch.

.. _repository: https://github.com/jcrmatos/daysgrounded

Copyright 2009-2015 Joao Carlos Roseta Matos. Licensed under the GNU General Public License v2 or later (GPLv2+).
