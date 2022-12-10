from pydantic import BaseModel
from app.competition.model import CompDetails
from typing import Optional
from uuid import UUID


class CompResponse(BaseModel):
    name: Optional[str]
    status: Optional[str]
    url: Optional[str]

    class  Config:
        orm_mode = True


class CompTable(CompResponse):
    comp_id: Optional[UUID]
    is_deleted: Optional[bool]
    created_at: Optional[str]
    updated_at: Optional[str]
    user_id: Optional[str]
    
    class  Config:
        orm_mode = True