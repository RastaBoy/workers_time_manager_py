from sqlalchemy import Column, Boolean, String, Integer

from . import Deletable

from .. import DeclarativeBase as Base

class User(Deletable, Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(length=64), nullable=False)
    password = Column(String(length=256), nullable=False)
    
    name = Column(String(length=256))
    surname = Column(String(length=256))
    
    
    is_admin = Column(Boolean, default=False)
