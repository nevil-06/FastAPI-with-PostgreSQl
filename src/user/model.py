from sqlalchemy import Column, String

from src.database_files.database import Base
from src.utils.defaultcol import DefaultColumns


class User(DefaultColumns, Base):
    __tablename__ = "user"
    name = Column(String(255))
    password = Column(String(255))
    email = Column(String(255), unique=True)

    def update_fields(self, update: dict):
        for key, value in update.items():
            if value:
                setattr(self, key, value)
