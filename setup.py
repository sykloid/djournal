#! /usr/bin/env python

from distutils.core import setup

from djournal import __VERSION__

setup(
    name = 'djournal',
    version = __VERSION__,
    description = 'Djournal is a blog application for Django.',
    author = 'P.C. Shyamshankar',
    author_email = 'sykora@lucentbeing.com',

    packages = ['djournal', 'djournal.migrations'],

    url = 'http://github.com/sykora/djournal/',
    license = 'GNU General Public License v3.0',

    classifiers = (
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
    )
)
