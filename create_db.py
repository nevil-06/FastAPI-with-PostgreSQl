from database_files.database import Base, engine
from user.user_schema import UserDetails
from competition.competition_schema import CompDetails
from entry.entry_schema import EntryDetails
#import UserModel
print("Creating Database")
#Base.metadata.remove(engine)
Base.metadata.create_all(engine)
