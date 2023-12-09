from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, Sequence("pet_id_seq"), primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
