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
import time
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, ThreadLocalMetaData
from zope.sqlalchemy import ZopeTransactionExtension
from gs.config import Config, getInstanceId

import logging
log = logging.getLogger('gs.database')

databases = {}


def init_db(dsn):
    engine = create_engine(dsn)
    Session = scoped_session(sessionmaker(bind=engine, twophase=True,
                        extension=ZopeTransactionExtension()))
    metadata = ThreadLocalMetaData()
    metadata.bind = engine
    metadata.reflect()

    return {'engine': engine,
            'session': Session,
            'metadata': metadata}


def get_db(instance_id=None):
    if not instance_id:
        instance_id = getInstanceId()
    # FIXME: USE LOCKING!
    if instance_id not in databases:
        config = Config(instance_id)
        config.set_schema('database', {'dsn': str})
        dsn = config.get('database')['dsn']

        top = time.time()
        databases[instance_id] = init_db(dsn)
        bottom = time.time()
        log.info("Initialised database for instance %s in %.2fs" %
                 (instance_id, (bottom - top)))
    return databases[instance_id]
