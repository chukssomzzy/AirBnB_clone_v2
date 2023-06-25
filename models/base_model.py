#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Column
from sqlalchemy.types import DateTime
import models
import os

if os.getenv('HBNB_TYPE_STORAGE') == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel():
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False,
                primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(
        DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
            Attributes:
                id: unique id generated
                created_at: creation date
                updated_at: updated date
            """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                if "id" not in kwargs:
                    self.id = str(uuid.uuid4())
                if "created_at" not in kwargs:
                    self.created_at = datetime.now()
                if "updated_at" not in kwargs:
                    self.updated_at = datetime.now()
            else:
                self.id = str(uuid.uuid4())
                self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__.copy())
        dictionary.update({'__class__':
                           (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary.get("_sa_instance_state"):
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        models.storage.delete(self)
