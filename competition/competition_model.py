from pydantic import BaseModel
from competition.competition_schema import CompDetails

class CompTable(BaseModel):
    comp_id : int
    name :str
    status : str
    url : str
    is_deleted : bool
    created_at : str
    updated_at : str
    user_id : int
    class  Config:
        orm_mode= True