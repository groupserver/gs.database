import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relation
from sqlalchemy import create_engine, Table, MetaData, ThreadLocalMetaData
from zope.sqlalchemy import ZopeTransactionExtension
from App.config import getConfiguration
import ConfigParser
import core

path = core.__file__
dirpath = os.path.dirname(path)

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

def init():
    cfg = getConfiguration()
    parser = ConfigParser.SafeConfigParser()
    parser.read(os.path.join(cfg.instancehome, 'etc/database.ini'))
    for section in parser.sections():
        print section
        if section.find('database-') == 0:
            assert parser.has_option(section, 'instance_id'),\
                    "No instance ID specified in section '%s'" % section
            assert parser.has_option(section, 'dsn'),\
                    "No dsn specified in section '%s'" % section         
            instance_id = parser.get(section, 'instance_id')
            dsn = parser.get(section, 'dsn')
            
            databases[instance_id] = init_db(dsn)

print databases 
