#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of log_parser.
# https://github.com/adeelahmad/log_parser

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2022, Adeel Ahmad <230291+adeelahmad@users.noreply.github.com>

from setuptools import setup, find_packages
from log_parser import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='common_log_parser',
    version=__version__,
    description='Parse HTTP Common Log format file for top visited urls, top ips and number of uniq ips',
    long_description='''
Parse HTTP Common Log format file for top visited urls, top ips and number of uniq ips
''',
    keywords='http common-format log parsing',
    author='Adeel Ahmad',
    author_email='230291+adeelahmad@users.noreply.github.com',
    url='https://github.com/adeelahmad/log_parser',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            'log_parser=log_parser.cli:main',
        ],
    },
)
