from database_files.database import Base
from sqlalchemy import String,Boolean,Integer,Column,DateTime,ForeignKey
from competition.competition_schema import CompDetails
import datetime


class EntryDetails(Base):
    __tablename__ = "Entry"
    entry_id = Column(Integer,primary_key = True)
    name = Column(String(50),nullable=False)
    status = Column(String(50),nullable=False)
    country = Column(String(50),nullable=False)
    state = Column(String(50),nullable=False)
    is_deleted = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    comp_id = Column(Integer,ForeignKey(CompDetails.comp_id))

    def update(self, update:dict):
        for key, value in update.items():
            if value:
                setattr(self, key, value)