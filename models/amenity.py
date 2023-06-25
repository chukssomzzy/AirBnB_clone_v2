#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
storage_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """Defines Amenity"""
    if storage_type == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenitites = relationship(
            "Place", secondary="place_amenity", back_populates="amenities")
    else:
        name = ""
