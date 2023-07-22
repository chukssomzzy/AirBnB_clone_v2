#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Float, ForeignKey, String, Integer, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
import os
from models.amenity import Amenity

storage_type = os.getenv("HBNB_TYPE_STORAGE")
if storage_type == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60), ForeignKey(
                              "places.id"), primary_key=True),
                          Column("amenity_id", String(60), ForeignKey(
                              "amenities.id"), primary_key=True)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    if storage_type == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        user = relationship("User", back_populates="places")
        city = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship(
            "Amenity", secondary="place_amenity", viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @ property
        def reviews(self):
            """Return reviews instance in a list"""
            return [review for review in models.storage.all(self.__class__) if
                    review.id == self.id]

        @ property
        def amenities(self):
            """Return amenity in place"""
            return [inst for inst in models.storage.
                    all(Amenity).values() if inst.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            if obj.__class__.__name__ == Amenity.__name__:
                self.amenity_ids.append(obj.id)

    def __init__(self, *args, **kwargs):
        """ Passing down """
        super().__init__(*args, **kwargs)
