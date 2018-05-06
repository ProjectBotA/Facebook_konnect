from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import pymysql
 
engine = create_engine('mysql+pymysql://root:root123@localhost/ProjDB', convert_unicode=True, echo=False)
Base = declarative_base()
Base.metadata.reflect(engine)

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True} 
 
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(20))

    def __init__(self, username=None, email=None, password=None):
        if username:
            self.username = username
        else:
            self.username = email
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
    
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)

class NGO(Base):
     __table__ = Base.metadata.tables['ngo_details']
 
 
# create tables
#Base.metadata.create_all(engine)