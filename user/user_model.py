from database_files.database import Base
from sqlalchemy import String, Boolean, Column, DateTime
from pydantic import BaseModel
import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID


class UserDetails(Base):
    __tablename__ = "User"
    User_Id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    Name = Column(String(255))
    Password = Column(String(255))
    Email = Column(String(255))
    is_Deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)

    def update(self, update: dict):
        for key, value in update.items():
            if value:
                setattr(self, key, value)

        # self.updated_at= datetime.datetime.utc
