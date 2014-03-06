#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup
import bbshighlighter

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
VERSION = bbshighlighter.__version__

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pygments-bbshighlighter',
    version=VERSION,
    packages=['bbshighlighter'],
    include_package_data=True,
    install_requires=['pygments'],
    license='BSD License',
    description='BBS formatter for Pygments.',
    long_description=README,
    url='http://github.com/uranusjr/bbsformatter',
    author='Tzu-ping Chung',
    author_email='uranusjr@gmail.com',
    entry_points={
        'pygments.formatters': 'bbs = bbshighlighter.formatters:BBSFormatter',
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
