from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Sequence
from sqlalchemy.orm import relationship
from database import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, Sequence("pet_id_seq"), primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)

    user = Column(Integer, ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence("pet_id_seq"), primary_key=True, index=True, autoincrement=True)
    email = Column(String)
    name = Column(String)
