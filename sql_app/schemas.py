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
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    id: int


class User(UserBase):
    id: int
    name: str
    pet: str

    class Config:
        orm_mode = True