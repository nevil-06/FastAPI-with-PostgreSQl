
from pydantic import BaseModel
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,DateTime,ForeignKey
#from userModel import UserDetails
from compModel import CompDetails
#from datetime import datetime



class EntryTable(BaseModel):
    entry_id : int
    name :str
    status : str
    country : str
    state :  str
    is_deleted : bool
    created_at : str
    updated_at : str
    comp_id : int
    
    class  Config:
        orm_mode= True



class EntryDetails(Base):
    __tablename__ = "Entry"
#    __table_args__ = {'extend_existing': True}
    entry_id = Column(Integer,primary_key = True)
    name = Column(String(255),nullable=False)
    status = Column(String(255),nullable=False)
    country = Column(String(255),nullable=False)
    state = Column(String(255),nullable=False)
    is_deleted = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    comp_id = Column(Integer,ForeignKey(CompDetails.comp_id))

