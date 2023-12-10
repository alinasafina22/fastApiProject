from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Sequence
from sqlalchemy.orm import relationship
from .database import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, Sequence("pet_id_seq"), primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)

    user = relationship("User", back_populates="pet")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence("pet_id_seq"), primary_key=True, index=True)
    name = Column(String)

    pet = relationship("Pet", back_populates="user")