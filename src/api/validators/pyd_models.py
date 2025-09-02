from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional

class UserModel(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: Optional[HttpUrl]

class UsersPageModel(BaseModel):
    page: int
    per_page: int
    total: int
    data: List[UserModel]
