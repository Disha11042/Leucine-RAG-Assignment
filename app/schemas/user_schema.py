from pydantic import BaseModel, EmailStr


# Data received during signup
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# Data returned after creating user
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


# Data received during login
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# JWT token response
class TokenResponse(BaseModel):
    access_token: str
    token_type: str