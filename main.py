from fastapi import FastAPI
from typing import List
from pet import Pet
from pet_breed import PetBreed

app = FastAPI()

# list[Pet] - это аннотация типа 
pets_db: List[Pet] = []


@app.post("/add_pet")
async def create_pet(pet: Pet):
    pets_db.append(pet)
    return pet


# enum for query params
@app.get("/get/pet_name/{pet_breed}")
async def get_pet_name_by_breed(pet_breed: PetBreed):
    if pet_breed is PetBreed.frenchi:
        return {"pet_breed": pet_breed, "name": "Harley"}
    if pet_breed is PetBreed.amstaff:
        return {"pet_breed": pet_breed, "name": "Ozzy"}
    return {"pet_breed": pet_breed, "name": "Batman"}


# offset is optional, page_limit has default value, and sort is boolean query
@app.get("/get/pets")
async def get_pets(offset: int | None = None, page_limit: int = 10, sort: bool = False):
    if sort:
        if offset:
            return pets_db[offset:offset + page_limit], "сортировочка"
        return pets_db, "сортировочка"
    else:
        if offset:
            return pets_db[offset:offset + page_limit]
        return pets_db


# required query
@app.get("/get/{pet_id}")
async def get_pet_by_id(pet_id: int):
    return {"pet_id": pet_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


