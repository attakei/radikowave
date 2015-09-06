#!/usr/bin/env python
# -*- coding:utf8 -*-
"""Setup Script
"""
from __future__ import unicode_literals
__author__ = 'attakei'


import os
import sys
import codecs
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
sys.path.append(here)


with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    README = f.read()

requires = [
    # For runnning in Pyramid
]

setup(
    name='radikowave',
    version='0.1.0',
    description=__doc__,
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
    ],
    author='attakei',
    author_email='attakei@gmail.com',
    url='https://github.com/attakei/radikowave',
    keywords='',
    packages=find_packages(exclude=['tests', 'implements', 'docs']),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
    },
)
