from app.database_files.database import Base
from sqlalchemy import String, Boolean, Column, DateTime, ForeignKey
from app.competition.schema import CompDetails
import datetime
import uuid

class EntryDetails(Base):
    __tablename__ = "entry"
    entry_id = Column(String, default = uuid.uuid4(), primary_key = True)
    name = Column(String(255))
    status = Column(String(255))
    country = Column(String(255))
    state = Column(String(255))
    is_deleted = Column(Boolean, default = False)
    created_at = Column(DateTime, default = datetime.datetime.utcnow)
    updated_at = Column(DateTime, default = datetime.datetime.utcnow, onupdate = datetime.datetime.utcnow)
    comp_id = Column(ForeignKey(CompDetails.comp_id))

    def update(self, update:dict):
        for key, value in update.items():
            if value:
                setattr(self, key, value)