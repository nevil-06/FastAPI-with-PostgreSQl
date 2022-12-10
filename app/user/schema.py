from pydantic import BaseModel
from app.user.model import UserDetails
from typing import Optional
from uuid import UUID


class UserResponse(BaseModel):
    name: Optional[str]
    email: Optional[str]

    class Config:
        orm_mode = True



class UserCreate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password : Optional[str]

    class Config:
        orm_mode = True



class UserTable(UserResponse):
    user_id : Optional[UUID]
    password: Optional[str]
    is_deleted: Optional[bool]
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True
    
