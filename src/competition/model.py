from sqlalchemy import Column, ForeignKey, String

from src.database_files.database import Base
from src.user.model import User
from src.utils.defaultcol import DefaultColumns


class Competition(DefaultColumns, Base):
    __tablename__ = "competition"
    name = Column(String(255))
    status = Column(String(255))
    url = Column(String(255))
    user_id = Column(ForeignKey(User.id))

    def update(self, update: dict):
        for key, value in update.items():
            if value:
                setattr(self, key, value)
