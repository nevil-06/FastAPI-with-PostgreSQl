from database_files.database import Base
from sqlalchemy import String,Boolean,Integer,Column,DateTime,ForeignKey
from user.user_schema import UserDetails
import datetime


class CompDetails(Base):
    __tablename__ = "Competition"
    comp_id = Column(Integer,primary_key = True)
    name = Column(String(255),nullable=False)
    status = Column(String(255),nullable=False)
    url = Column(String(255),nullable=False)
    is_deleted = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    user_id = Column(Integer,ForeignKey(UserDetails.User_Id))

    def update(self, update:dict):
        for key, value in update.items():
            if value:
                setattr(self, key, value)