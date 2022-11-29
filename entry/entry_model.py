from pydantic import BaseModel
from entry.entry_schema import EntryDetails

class EntryTable(BaseModel):
    entry_id : int
    name :str
    status : str
    country : str
    state :  str
    is_deleted : bool
    created_at : str
    updated_at : str
    comp_id : int
    
    class  Config:
        orm_mode= True