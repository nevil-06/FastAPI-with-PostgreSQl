from database_files.database import Base
from sqlalchemy import String, Boolean, Column, DateTime, ForeignKey
from user.user_schema import UserDetails
import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

class CompDetails(Base):
    __tablename__ = "Competition"
    comp_id = Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key = True)
    name = Column(String(255))
    status = Column(String(255))
    url = Column(String(255))
    is_deleted = Column(Boolean,default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    user_id = Column(ForeignKey(UserDetails.User_Id))

    def update(self, update:dict):
        for key, value in update.items():
            if value:
                setattr(self, key, value)