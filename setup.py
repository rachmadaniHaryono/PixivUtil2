#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from distutils.core import setup

import os
import sys

isWindows = os.name is 'nt'
ranWithPy3 = sys.version_info >= (3, 0)


if isWindows:
    import py2exe
else:
    py2exe = None

if isWindows:
    requires = ['BeautifulSoup']
    options = {'py2exe': {'compressed': 1, 'excludes': ['Tkconstants', 'Tkinter']}, }
    console = [{"script": "PixivUtil2.py",              # Main Python script
                "icon_resources": [(0, "icon2.ico")]}]  # Icon to embed into the PE file.
    setup(console=console, requires=requires, options=options, )
else:
    requires = [
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
    setup(
        install_requires=requires,
        entry_points={'console_scripts': ['PixivUtil2 = PixivUtil2:main', ]}
    )
