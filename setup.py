# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.database',
    version=version,
    description="Core GS database bindings.",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Zope Public License',
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux"
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='groupserver option options',
    author='Richard Waid',
    author_email='richard@onlinegroups.net',
    url='http://groupserver.org/',
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'psycopg2',
        'setuptools',
        'sqlalchemy',
        'zope.sqlalchemy',
        'gs.config[zope]',  # Note: With Zope support
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
