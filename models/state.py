#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import String
from models.base_model import Base, BaseModel
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """ returns cities in current state """
        obj_cities = [city for city in storage.all(self).values()
                      if city.state_id == self.id]
        return obj_cities
