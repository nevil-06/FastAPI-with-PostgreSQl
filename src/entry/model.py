from sqlalchemy import Column, ForeignKey, String

from src.competition.model import Competition
from src.database_files.database import Base
from src.utils.defaultcol import DefaultColumns


class Entry(DefaultColumns, Base):
    __tablename__ = "entry"
    name = Column(String(255))
    status = Column(String(255))
    country = Column(String(255))
    state = Column(String(255))
    comp_id = Column(ForeignKey(Competition.id))

    def update(self, update: dict):
        for key, value in update.items():
            if value:
                setattr(self, key, value)
