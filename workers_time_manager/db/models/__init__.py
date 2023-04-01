from sqlalchemy import Column, Boolean


class Deletable():
    deleted = Column(Boolean, default=False, nullable=False)
    
    
from .user import *