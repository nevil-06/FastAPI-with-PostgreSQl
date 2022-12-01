from pydantic import BaseModel
from entry.entry_model import EntryDetails
from typing import Optional


class EntryTable(BaseModel):
    entry_id : Optional[str]
    name :Optional[str]
    status : Optional[str]
    country : Optional[str]
    state :  Optional[str]
    is_deleted : Optional[bool]
    created_at : Optional[str]
    updated_at : Optional[str]
    comp_id : Optional[str]
    
    class  Config:
        orm_mode= True


'''
class EntryTableUpdateRequest(BaseModel):
    name: Optional[str]
    status: Optional[str]
    country: Optional[str]
    state:  Optional[str]

class EntryTableCreateRequest(EntryTableUpdateRequest):
    name: str
    status: str

class EntryResponse(EntryTableCreateRequest):
    pass
'''