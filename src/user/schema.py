from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from src.user.model import UserDetails


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


class UserLogin(UserCreate):
    email: Optional[str]
    password : Optional[str]

    class Config:
        orm_mode = True


class UserTable(UserResponse):
    id : Optional[UUID]
    password: Optional[str]
    is_deleted: Optional[bool]
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True
    
