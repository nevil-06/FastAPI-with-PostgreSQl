from pydantic import BaseModel
from app.entry.model import EntryDetails
from typing import Optional
from uuid import UUID


class EntryResponse(BaseModel):
    name : Optional[str]
    status : Optional[str]
    country : Optional[str]
    state : Optional[str]
    
    class  Config:
        orm_mode= True

class EntryTable(EntryResponse):
    entry_id : Optional[UUID]
    is_deleted : Optional[bool]
    created_at : Optional[str]
    updated_at : Optional[str]
    comp_id : Optional[str]
    
    class  Config:
        orm_mode= True
