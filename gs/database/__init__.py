# coding=utf-8
import os
from App.config import getConfiguration
import ConfigParser

from core import *

import config

config.init()

path = config.__file__
dirpath = os.path.dirname(path)

cfg = getConfiguration()

# we don't use the live reload service.
#service = ConfigurationService(watch=False)
#service.registerModel(os.path.join(dirpath, 'database.model'))
parser = ConfigParser.SafeConfigParser()
parser.read(os.path.join(cfg.instancehome, 'etc/database.ini'))
print parser.sections()

databases = {}

def init_db(dsn):
    engine = create_engine()
    Session = scoped_session(sessionmaker(bind=engine, twophase=True,
                        extension=ZopeTransactionExtension()))
    metadata = ThreadLocalMetaData()
    metadata.bind = engine
    metadata.reflect()

    return {'engine': engine,
            'session': session,
            'metadata': metadata}

for section in parser.sections():
    if section.find('database-') == 0:
        assert parser.has_option(section, 'instance_id'),\
                   "No instance ID specified in section '%s'" % section
        assert parser.has_option(section, 'dsn'),\
                   "No dsn specified in section '%s'" % section        
        instance_id = parser.get(section, 'instance_id')
        dsn = parser.get(section, 'dsn')

        databases[instance_id] = dsn 
