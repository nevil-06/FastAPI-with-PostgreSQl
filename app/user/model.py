from app.database_files.database import Base
from sqlalchemy import String, Boolean, Column, DateTime
import datetime
import uuid


class UserDetails(Base):
    __tablename__ = "user"
    user_id = Column(String, primary_key = True, default = uuid.uuid4())
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

