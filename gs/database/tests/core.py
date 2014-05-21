# -*- coding: utf-8 -*-
from mock import MagicMock
from unittest import TestCase
import gs.database.core


class FauxMetadata(object):
    "Ce n'est pas des metadata'"


class TestCoreFunctions(TestCase):

    def setUp(self):
        m = FauxMetadata()
        m.tables = {'faux': 'table'}
        d = {'metadata': m,
                'session': lambda: 'session'}
        gs.database.core.get_db = MagicMock(return_value=d)

    def test_getTable(self):
        'Test the getTable function'
        r = gs.database.core.getTable('faux')
        self.assertEqual('table', r)

    def test_getSession(self):
        'Test the getSession function'
        r = gs.database.core.getSession()
        self.assertEqual('session', r)
