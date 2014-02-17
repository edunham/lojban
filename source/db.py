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

    def __init__(name, dfn, n1, n2, r1=None, r2=None, r3=None, mn=None,
            notes=None)
        pass

    def slurp(path):
        f = open(path)
        for l in f.readlines():
            name = l[1:6]
            r1 = l[7:10].strip()
            r2 = l[11:14].strip()
            r3 = l[15:19].strip()
            tr = l[20:41].strip()               # translation
            mn = l[41:62].strip().strip("'")    # mneumonic
            dfn = l[63:159].strip()
            n1 = t[159:162].strip()
            n2 = int(t[162:165].strip())
            
