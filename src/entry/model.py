import uuid
import datetime
from src.database_files.database import Base
from src.competition.schema import CompetitionDetails
from sqlalchemy import String, Boolean, Column, DateTime, ForeignKey


def get_id():
    return str(uuid.uuid4())


class EntryDetails(Base):
    __tablename__ = "entry"
    id = Column(String, default = get_id, primary_key = True)
    name = Column(String(255))
    status = Column(String(255))
    country = Column(String(255))
    state = Column(String(255))
    is_deleted = Column(Boolean, default = False)
    created_at = Column(DateTime, default = datetime.datetime.utcnow)
    updated_at = Column(DateTime, default = datetime.datetime.utcnow, onupdate = datetime.datetime.utcnow)
    comp_id = Column(ForeignKey(CompetitionDetails.id))

    def update(self, update:dict):
        for key, value in update.items():
            if value:
                setattr(self, key, value)