from pydantic import BaseModel, EmailStr
from typing import Optional
class UserCreate(BaseModel):
    email: EmailStr
    api_key : str
    password : str
    user_name : str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UpdateUser(BaseModel):
    email: Optional[EmailStr] = None
    api_key : Optional[str] = None
    user_name : Optional[str] = None

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"