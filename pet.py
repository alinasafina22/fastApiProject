from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Annotated


class Pet(BaseModel):
    id: UUID = uuid4()
    # аннотация ограничивает длину строки до 50 символов
    name: Annotated[str, Field(..., max_length=50, pattern="[A-Za-zА-Яа-я]*")]
    age: Annotated[int, Field(..., gt=0)]
    breed: str | None = None
    photo_url: str | None = None