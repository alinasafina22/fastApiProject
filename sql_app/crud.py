from sqlalchemy.orm import Session, joinedload
import models
import schemas


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
    query = db.query(models.User, models.Pet)
    query = query.join(models.Pet, models.Pet.user == models.User.id)
    query = query.all()
    result = []
    for user, pet in query:
        user_info = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "pets": {
                "id": pet.id,
                "user": pet.user,
                "name": pet.name,
                "age": pet.age
            }
        }
        result.append(user_info)
    print(result)
    return{"data": result}


def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()
