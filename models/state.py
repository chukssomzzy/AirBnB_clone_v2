#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import String
from models.base_model import Base, BaseModel
import models


class State(BaseModel, Base):
    """ State class """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ returns cities in current state """
            obj_cities = [city for city in models.storage.all(self).values()
                          if city.state_id == self.id]
            return obj_cities

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
