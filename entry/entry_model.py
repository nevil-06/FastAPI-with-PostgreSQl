from database_files.database import Base
from sqlalchemy import String, Boolean, Column, DateTime, ForeignKey
from competition.schema import CompDetails
import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

class EntryDetails(Base):
    __tablename__ = "Entry"
    entry_id = Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key = True)
    name = Column(String(50))
    status = Column(String(50))
    country = Column(String(50))
    state = Column(String(50))
    is_deleted = Column(Boolean,default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    comp_id = Column(ForeignKey(CompDetails.comp_id))

    def update(self, update:dict):
        for key, value in update.items():
            if value:
                setattr(self, key, value)