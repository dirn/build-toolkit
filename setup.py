#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

deps = [
    'boto',
    'docopt',
    'envoy'
]

setup(
    name='bob',
    version='0.0.1',
    install_requires=deps,
    description='Binary Build Toolkit.',
    # long_description='Meh.',/
    author='Kenneth Reitz',
    author_email='kenneth@heroku.com',
    url='https://github.com/heroku/build-toolkit',
    packages=['bob'],
    # license='MIT',
    entry_points={
        'console_scripts': [
            'bob = bob:cli.dispatch',
        ],
    }
)
