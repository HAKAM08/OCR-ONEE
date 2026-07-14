from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    fullname: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    role: str

    model_config = ConfigDict(from_attributes=True)