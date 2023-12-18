from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Annotated


class PetBase(BaseModel):
    # аннотация ограничивает длину строки до 50 символов
    name: Annotated[str, Field(..., max_length=50, pattern="[A-Za-zА-Яа-я]*")]
    age: Annotated[int, Field(..., gt=0)]


class PetCreate(PetBase):
    pass


class Pet(PetBase):
    id: int
    name: str
    age: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    name: str
    email: str
    pet: str

    class Config:
        from_attributes = True
