# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
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
from mock import MagicMock
from unittest import TestCase
import gs.database.config


class TestConfigGetDB(TestCase):
    'Test the get_db function'
    def setUp(self):
        gs.database.config.databases = {'faux': 'A database'}
        self.oldInit = gs.database.config.init_db
        gs.database.config.init_db = MagicMock(return_value='Also a database')
        gs.database.config.Config = MagicMock(spec=gs.database.config.Config)

    def tearDown(self):
        gs.database.config.init_db = self.oldInit

    def test_get_db_instance(self):
        'Test get_db when an instance-ID is passed in, and the db exists'
        r = gs.database.config.get_db('faux')
        self.assertEqual('A database', r)

    def test_get_db_no_instance(self):
        'Test get_db when an instance-ID is missing from the databases'
        r = gs.database.config.get_db('missing')
        self.assertEqual('Also a database', r)
        gs.database.config.Config.assert_called_once_with('missing')


class TestConfigInitDB(TestCase):
    'Test the init_db function'
    def setUp(self):
        gs.database.config.create_engine = MagicMock()
        gs.database.config.scoped_session = MagicMock()
        gs.database.config.ThreadLocalMetaData = MagicMock()

    def test_init_db(self):
        'Test the init_db call'
        r = gs.database.config.init_db('faux')
        self.assertIn('engine', r)
        self.assertIn('session', r)
        self.assertIn('metadata', r)
        gs.database.config.create_engine.assert_called_once_with('faux')
