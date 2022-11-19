
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,DateTime#,ForeignKey
from pydantic import BaseModel
#from datetime import datetime

class UserTable(BaseModel):
    User_Id:int
    Name: str
    Password : str
    Email : str 
    is_Deleted : bool
    created_at : str 
    updated_at :str

    class Config:
        orm_mode = True

class UserDetails(Base):
    __tablename__ =  "User"
    User_Id = Column(Integer,primary_key=True)
    Name = Column(String(255),nullable=False)
    Password = Column(String(255),nullable=False)
    Email = Column(String(255))
    is_Deleted = Column(Boolean, default=False)
    created_at = Column(DateTime)
    updated_at  = Column(DateTime)

