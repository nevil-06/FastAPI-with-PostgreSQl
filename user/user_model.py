from pydantic import BaseModel
from user.user_schema import UserDetails
from typing import Optional

class UserTable(BaseModel):
    User_Id:Optional[int]
    Name: Optional[str]
    Password : Optional[str]
    Email : Optional[str]
    is_Deleted : Optional[bool]
    created_at : Optional[str]
    updated_at :Optional[str]

    class Config:
        orm_mode = True