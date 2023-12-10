from sqlalchemy.orm import Session

from . import models, schemas


def create_pet(db: Session, pet: schemas.PetCreate):
    db_pet = models.Pet(id=pet.id, name=pet.name, age=pet.age)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(id=user.id, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()