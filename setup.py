#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function

import os
import sys
from os import path

try:
    from setuptools import setup, convert_path, find_packages
    SETUPTOOLS_USED = True
except ImportError:
    from distutils.core import setup, find_packages
    from distutils.util import convert_path
    SETUPTOOLS_USED = False

isWindows = os.name is 'nt'
ranWithPy3 = sys.version_info >= (3, 0)


# Terminal colors on *nix systems
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if not isWindows:
    if ranWithPy3:
        pass
    else:
        print("After installing, run with command:\n")
        print("\tPixivUtil2\n")


if isWindows:
    import py2exe

console = [{"script": "PixivUtil2.py",              # Main Python script
            "icon_resources": [(0, "icon2.ico")]}]  # Icon to embed into the PE file.
requires = ['BeautifulSoup']
options = {'py2exe': {'compressed': 1, 'excludes': ['Tkconstants', 'Tkinter']}, }

setup_kwargs = dict(console=console, requires=requires, options=options)

if not isWindows:
    setup_kwargs = dict(entry_points={'console_scripts': [
        'PixivUtil2 = PixivUtil2:main',
        'PixivUtil2-server = pixiv_util2.server:cli',
    ]})

if SETUPTOOLS_USED:
    setup_kwargs['project_urls'] = {
        'Bug Reports': 'https://github.com/Nandaka/PixivUtil2/issues',
        'Funding': 'https://bit.ly/PixivUtilDonation',
        'Source': 'https://github.com/Nandaka/PixivUtil2',
    }

# get install_requires
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'requirements.txt')) as f:
    install_requires = f.read().split('\n')
install_requires = [x.strip() for x in install_requires]
if ranWithPy3:
    install_requires = [
        'beautifulsoup4>=4.6.0',
        'imageio>=2.1.2',
        'numpy>=1.12.1',
        'Pillow>=4.3.0',
        'socksipy-branch>=1.01',
        'win_unicode_console>=0.5',
        # python3&linux only
        'MechanicalSoup>=0.10.0',
        'six>=1.11.0',
    ]
    setup_kwargs['extras_require'] = {
        'server': [
            'appdirs>=1.4.3',
            'Flask-Admin>=1.5.0',
            'flask-paginate==0.5.1',
            'Flask-SQLAlchemy>=2.3.1',
            'Flask-WTF>=0.14.2',
            'Flask>=0.12.2',
            'humanize>=0.5.1',
            'SQLAlchemy-Utils>=0.32.18',
            'structlog>=17.2.0',
        ],
    }
# get program version
main_ns = {}
ver_path = convert_path('PixivConstant.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)
version = main_ns['PIXIVUTIL_VERSION']
v_parts = version.split('-', 1)
main_version = '{0}.{1}.{2}'.format(v_parts[0][0:4], int(v_parts[0][4:6]), int(v_parts[0][6:7]))
if '-' in version:
    version = main_version + '.{}'.format(v_parts[1])
else:
    version = main_version
# get long_description
readme_path = convert_path('readme.txt')
with open(readme_path) as readme_file:
    long_description = readme_file.read()

setup(
    name='PixivUtil2',  # Required
    version=version,
    description='Download images from Pixiv and more',
    long_description=long_description,
    url='https://github.com/Nandaka/PixivUtil2',
    author='Nandaka',
    # author_email='<>@<>.com',
    classifiers=[  # Optional
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='pixiv downloader',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=install_requires,
    **setup_kwargs
)
