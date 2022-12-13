import uuid
import datetime
from src.database_files.database import Base
from sqlalchemy import String, Boolean, Column, DateTime

def get_id():
    return str(uuid.uuid4())

class UserDetails(Base):
    __tablename__ = "user"
    id = Column(String, primary_key = True, default = get_id)
    name = Column(String(255))
    password = Column(String(255))
    email = Column(String(255), unique = True)
    is_deleted = Column(Boolean, default = False)
    created_at = Column(DateTime, default = datetime.datetime.utcnow)
    updated_at = Column(DateTime, default = datetime.datetime.utcnow,
                        onupdate = datetime.datetime.utcnow)

    def update(self, update: dict):
        for key, value in update.items():
            if value:
                setattr(self, key, value)

