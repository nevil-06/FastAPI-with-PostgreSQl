from pydantic import BaseModel
from competition.competition_schema import CompDetails
from typing import Optional


class CompTable(BaseModel):
    comp_id : Optional[str]
    name :Optional[str]
    status : Optional[str]
    url : Optional[str]
    is_deleted : Optional[bool]
    created_at : Optional[str]
    updated_at : Optional[str]
    user_id : Optional[str]
    class  Config:
        orm_mode= True