#!/usr/bin/env python

from setuptools import setup

with open('README.txt') as file:
    long_description = file.read()    

setup(name='gnp',
      version='0.0.1',
      description='Google News Parser',
      author='Manuel David Pandian',
      author_email='manueldavidpandian@gmail.com',
      url='tbd',
      py_modules=['gnp'],
      install_requires=['lxml'],
      classifiers=['Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License'],
      long_description=long_description
      )