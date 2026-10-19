from pydantic import BaseModel, Field, EmailStr

class ProjectCreate(BaseModel):
    name: str
    description: str = ''
    
class ProjectRead(BaseModel):
    id: int
    name: str
    description: str
    
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    
class UserRead(BaseModel):
    id: int
    email: EmailStr
    
class LoginRequest(BaseModel):
    email: EmailStr
    password: str    
    
class Token(BaseModel):
    access_token: str
    token_type: str