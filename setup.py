# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup

setup(
    name="python-dotenv",
    description="Add .env support to your django/flask apps in development and deployments",
    version="0.1.2",
    author="Saurabh Kumar",
    author_email="me+github@saurabh-kumar.com",
    url="http://github.com/theskumar/python-dotenv",
    keywords=['environment variables', 'deployments', 'settings', 'env', 'dotenv',
              'configurations', 'python'],
    py_modules=['dotenv'],
    install_requires=[
        'click>=3.0',
    ],
    entry_points='''
        [console_scripts]
        dotenv=dotenv:cli
    ''',
    classifiers=[
        # As from https://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.3',
        # 'Programming Language :: Python :: 2.4',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        # 'Framework :: Django',
    ]
)

# (*) Please direct queries to the discussion group, rather than to me directly
#     Doing so helps ensure your question is helpful to other users.
#     Queries directly to my email are likely to receive a canned response.
#
#     Many thanks for your understanding.
