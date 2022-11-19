
from pydantic import BaseModel
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,DateTime,ForeignKey
from userModel import UserDetails
#from datetime import datetime



class CompTable(BaseModel):
    comp_id : int
    name :str
    status : str
    url : str
    is_deleted : bool
    created_at : str
    updated_at : str
    user_id : int
    class  Config:
        orm_mode= True



class CompDetails(Base):
    __tablename__ = "Competition"
    comp_id = Column(Integer,primary_key = True)
    name = Column(String(255),nullable=False)
    status = Column(String(255),nullable=False)
    url = Column(String(255),nullable=False)
    is_deleted = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    user_id = Column(Integer,ForeignKey(UserDetails.User_Id))

