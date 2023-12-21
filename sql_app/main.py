from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="BAD_REQUEST")
    return crud.create_user(db=db, user=user)


@app.post("/create-pet/", response_model=schemas.Pet)
async def create_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    return crud.create_pet(db=db, pet=pet)


@app.get("/get-user/{id_user}", response_model=schemas.User)
async def get_user(id_user: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, id=id_user)
    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=404, detail="NOT_FOUND")


@app.get("/get-pet/{id_pet}", response_model=schemas.Pet)
async def get_pet(id_pet: int, db: Session = Depends(get_db)):
    return crud.get_pet(db, pet_id=id_pet)
