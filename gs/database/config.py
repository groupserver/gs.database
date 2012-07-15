# coding=utf-8
import os
from os.path import isfile
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relation
from sqlalchemy import create_engine, Table, MetaData, ThreadLocalMetaData
from zope.sqlalchemy import ZopeTransactionExtension
from gs.config import Config, getInstanceId
import logging
import time

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
    # XXX: USE LOCKING!
    if not databases.has_key(instance_id):
        config = Config(instance_id)
        config.set_schema('database', {'dsn': str})
        dsn = config.get('database')['dsn']
        
        top = time.time()        
        databases[instance_id] = init_db(dsn)
        bottom = time.time()
        log.info("Initialised database for instance %s in %.2fs" % 
                 (instance_id, (bottom-top)))

    return databases[instance_id]
