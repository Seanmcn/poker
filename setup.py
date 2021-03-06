# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


install_requires = [
    'pytz',
    'requests',
    'lxml',
    'python-dateutil',
    'parsedatetime',
    'cached-property',
    'click',
    'enum34',   # backported versions from Python3
    'pathlib',
    'configparser',
]


console_scripts = [
    'poker = poker.commands:poker',
]


classifiers = [
    "Intended Audience :: Developers",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
]


setup(
    name = 'poker',
    version = '0.22.2',
    description = 'Poker Framework',
    classifiers = classifiers,
    keywords = 'poker',
    author = u'Kiss György',
    author_email = "kissgyorgy@me.com",
    url = "https://github.com/pokerregion/poker",
    license = "MIT",
    packages = find_packages(),
    install_requires = install_requires,
    entry_points = {'console_scripts': console_scripts},
    tests_require = ['pytest', 'coverage', 'coveralls'],
)
