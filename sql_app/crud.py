from sqlalchemy.orm import Session

import models
import schemas


def create_pet(db: Session, pet: schemas.PetCreate):
    db_pet = models.Pet(name=pet.name, age=pet.age)
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
    return db.query(models.User).filter(models.User.id == id).first()


def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()
