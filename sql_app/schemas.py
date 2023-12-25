from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4
from typing import Annotated, List, Optional


class PetBase(BaseModel):
    # аннотация ограничивает длину строки до 50 символов
    name: Annotated[str, Field(..., max_length=50, pattern="[A-Za-zА-Яа-я]*")]
    age: Annotated[int, Field(..., gt=0)]


class PetCreate(PetBase):
    user: int


class Pet(PetBase):
    id: int
    user: int
    name: str
    age: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    email: EmailStr


class User(UserBase):
    id: int
    name: str
    email: str
    pets: Optional[List[Pet]] = None

    class Config:
        from_attributes = True
