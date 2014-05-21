# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2012, 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import absolute_import
from .config import get_db


def getTable(tablename):
    '''Get a database table for the database for the current instance

:param str tablename: The name of the table.
:return: A database table.
:rtype: ``sqlalchemy.Table``'''
    database = get_db()
    return database['metadata'].tables[tablename]


def getSession():
    '''Get a SQLAlchemy session for the current instance

:return: The database session for the current GroupServer instance.
:rtype: `SQLAlchemy session.`__

.. __: http://docs.sqlalchemy.org/en/rel_0_7/orm/session.html'''
    database = get_db()
    return database['session']()
