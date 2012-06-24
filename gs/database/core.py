from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relation
from sqlalchemy import create_engine, Table, MetaData, ThreadLocalMetaData
from zope.sqlalchemy import ZopeTransactionExtension
from zope.globalrequest import getRequest
from gs.database.config import databases

def getInstanceId():
    instance_id = getRequest().get('HTTP_INSTANCEID','default')
    return instance_id

def getTable(tablename):
    instance_id = getInstanceId()
    return databases[instance_id]['metadata'].tables[tablename]

def getSession():
    instance_id = getInstanceId()
    return databases[instance_id]['session']()
    
