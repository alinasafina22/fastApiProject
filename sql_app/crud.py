from sqlalchemy.orm import Session, joinedload
import models
import schemas
from fastapi import HTTPException


def create_pet(db: Session, pet: schemas.PetCreate):
    db_pet = models.Pet(name=pet.name, age=pet.age, user=pet.user)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_id(db: Session, id: int):
    # query = (db.query(models.User)
    #         .outerjoin(models.Pet, models.User.id == models.Pet.user)
    #         .filter(models.User.id == id)
    #         .all())
    query = db.query(models.User, models.Pet).filter(models.User.id == id)
    query = query.join(models.Pet, models.Pet.user == models.User.id)
    query = query.all()
    result = []
    pets_info = []
    user_info = None
    for user, pet in query:
        # user_info = {
        #     "id": user.id,
        #     "name": user.name,
        #     "email": user.email,
        #     "pets": {
        #         "id": pet.id,
        #         "user": pet.user,
        #         "name": pet.name,
        #         "age": pet.age
        #     }
        # }
        # result.append(user_info)
        if user_info is None:
            # Create user_info dictionary only once
            user_info = {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "pets": []
            }

            # Add pet information to the pets list
        pets_info.append({
            "id": pet.id,
            "user": pet.user,
            "name": pet.name,
            "age": pet.age
        })

        # Assign the pets_info list to the "pets" field in user_info
        user_info["pets"] = pets_info
    return user_info


def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()


def delete_pet(db: Session, pet_id: int):
    pet_for_delete = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if pet_for_delete is None:
        # Если питомец не найден, поднимаем HTTPException с кодом состояния 404 (Not Found)
        raise HTTPException(status_code=404)
    return db.delete(pet_for_delete)
