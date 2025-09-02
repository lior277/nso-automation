# src/api/models/user_models.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List

class User(BaseModel):
    id: int
    username: str
    email: Optional[EmailStr] = None
    firstName: str
    lastName: str
    gender: Optional[str] = None
    image: Optional[str] = None

class UsersResponse(BaseModel):
    users: List[User]
    total: int
    skip: int
    limit: int
