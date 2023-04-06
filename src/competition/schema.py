from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CompetitionResponse(BaseModel):
    name: Optional[str]
    status: Optional[str]
    url: Optional[str]

    class Config:
        orm_mode = True


class CompetitionTable(CompetitionResponse):
    id: Optional[UUID]
    is_deleted: Optional[bool]
    created_at: Optional[str]
    updated_at: Optional[str]
    user_id: Optional[str]

    class Config:
        orm_mode = True
