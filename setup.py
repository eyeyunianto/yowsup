#!/usr/bin/env python

from distutils.core import setup
from pkgutil import walk_packages

setup(name='yowsup',
      version='1.0',
      packages=['Yowsup', 'Yowsup.Auth', 'Yowsup.Common', 'Yowsup.ConnectionIO', 'Yowsup.Contacts', 'Yowsup.Interfaces', 'Yowsup.Registration',
                 'Yowsup.Interfaces.DBus', 'Yowsup.Interfaces.Lib', 'Yowsup.Auth.mechanisms', 'Yowsup.Common.Http',
                 'Yowsup.Registration.v1', 'Yowsup.Registration.v2'],
      package_dir = {'': 'src'},
      data_files = [('/usr/share/yowsup',['src/countries.csv']),],
      )
