#! /usr/bin/env python2.7

from sqlalchemy.dialects.sqlite import \
            BLOB, BOOLEAN, CHAR, DATE, DATETIME, DECIMAL, FLOAT, \
            INTEGER, NUMERIC, SMALLINT, TEXT, TIME, TIMESTAMP, \
            VARCHAR

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

dbpath = 'testdb'
dbconnect = 'sqlite+pysqlite:///' + dbpath


e = create_engine(dbconnect)

Base = declarative_base() # because the tutorial said to

class Gismu(Base):
    __tablename__ = 'gismu'
    name =  Column(String, primary_key = True)
    rafsi1 = Column(String)
    rafsi2 = Column(String)
    rafsi3 = Column(String)
    mneumonic = Column(String)
    definition = Column(String)
    n1 = Column(String)
    n2 = Column(Int)
    notes = Column(String)
    #cflist http://docs.sqlalchemy.org/en/rel_0_7/orm/relationships.html
