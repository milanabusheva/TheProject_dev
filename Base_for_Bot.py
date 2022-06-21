from datetime import datetime

from sqlalchemy import String, Integer, Boolean, Column, ARRAY, ForeignKey, Text
from sqlalchemy.orm import relationship

import sqlalchemy.ext.declarative as dec
import sqlalchemy.orm as orm
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import Session

SQLAlchemyBase = dec.declarative_base()


class Users:

    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    phone = Column('phone', Integer)
    project_name = Column('project_name', String(200), nullable=False)
    project_desc = Column('project_desc', Text())
    taglist = Column('taglist', ARRAY(item_type=String(200)), nullable=True)
