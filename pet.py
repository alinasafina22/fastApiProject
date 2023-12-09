from pydantic import BaseModel
from uuid import UUID, uuid4


class Pet(BaseModel):
    id: UUID = uuid4()
    name: str
    age: int
    breed: str | None = None
    photo_url: str | None = None