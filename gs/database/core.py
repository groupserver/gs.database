from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relation
from sqlalchemy import create_engine, Table, MetaData, ThreadLocalMetaData
from zope.sqlalchemy import ZopeTransactionExtension
from gs.database.config import get_db

def getTable(tablename):
    database = get_db()
    return database['metadata'].tables[tablename]

def getSession():
    database = get_db() 
    return database['session']()
