
desc = """# JustWatchAPI

JustWatch.com Python 3 API

How To 
----------------------------------------------------------
search for an item
----------------------------------------------------------
from justwatchapi import JustWatch

just_watch = JustWatch()

results = just_watch.search_for_item(query='the matrix')
----------------------------------------------------------
or search for combination of genres
----------------------------------------------------------
just_watch = JustWatch(genres=['act', 'scf', 'hrr'])

results_by_genres = just_watch.search_for_item()
----------------------------------------------------------
or maybe search by provider
----------------------------------------------------------
just_watch = JustWatch()

results_by_providers = just_watch.search_for_item(providers=['nfx', 'stn'])
----------------------------------------------------------
or possibly a combination of the above 
----------------------------------------------------------
just_watch = JustWatch()

results_by_multiple = just_watch.search_for_item(
    providers=['nfx', 'stn'], 
    content_types=['movie'], 
    monetization_types=['free'])
----------------------------------------------------------
Read api_payload.txt for more information"""

import os
from setuptools import setup


setup(
    name = "JustWatch",
    version = "0.5.1",
    author = "Dawoud Tabboush",
    author_email = "dtabboush@gmail.com",
    description = ("A simple api for justwatch.com"),
    license = "MIT",
    keywords = "movies tv api",
    url = "https://github.com/dawoudt/JustWatchAPI",
    packages=['justwatch'],
    long_description=desc,
    platforms='any',
    install_requires=[
        'requests>=2.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
