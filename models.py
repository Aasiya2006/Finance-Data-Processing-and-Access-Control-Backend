from sqlalchemy import Column,Integer,String,Float,Date,ForeignKey
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    role = Column(String)
    status = Column(String, default = "active")

class Record(Base):
    __tablename__ = "records"

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    amount = Column(Float)
    type = Column(String)
    category = Column(String)
    date = Column(String)
    description = Column(String)