from database_files.database import Base, engine
from user.model import UserDetails
from competition.schema import CompDetails
from entry.entry_schema import EntryDetails

print("Creating Database")


Base.metadata.create_all(engine)
