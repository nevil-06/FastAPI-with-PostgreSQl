from database import Base,engine
from models.userModel import UserDetails
from models.compModel import CompDetails
from models.entryModel import EntryDetails
#import UserModel
print("Creating Database")
#Base.metadata.remove(engine)
Base.metadata.create_all(engine)


