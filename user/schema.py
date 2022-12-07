from pydantic import BaseModel
from user.model import UserDetails
from typing import Optional
from uuid import UUID


class UserResponse(BaseModel):
    user_id: UUID
    name: str
    email: str

    class Config:
        orm_mode = True


class UserTable(UserResponse):
    user_id: Optional[str]
    name: Optional[str]
    password: Optional[str]
    email: Optional[str]
    is_deleted: Optional[bool]
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True
    
