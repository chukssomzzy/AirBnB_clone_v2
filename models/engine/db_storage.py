#!/usr/bin/python3

"""DB Storage Engine"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ contains definition of a MySQL power DB storage engine"""
    __engine = None
    __session = None
    classes = {
        'State': State, 'City': City, 'User': User
    }

    def __init__(self):
        """initialize the database with the correct session and engine"""
        engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                               format(os.getenv('HBNB_MYSQL_USER'),
                                      os.getenv('HBNB_MYSQL_PWD'), os.getenv(
                                          'HBNB_MYSQL_HOST'), os.getenv(
                                              'HBNB_MYSQL_DB')),
                               pool_pre_ping=True)
        self.__engine = engine

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session and returns all object
        depending on the cls and returns all if None
        """
        all_dict = {}
        if cls:
            if cls.__name__ in self.classes.keys() and self.__session:
                for cls_inst in self.__session.query(cls).all():
                    all_dict[cls_inst.__class__.
                             __name__ + "." + cls_inst.id] = cls_inst
                return all_dict
        elif self.__session:
            for cls_type in self.classes.values():
                for cls_inst in self.__session.query(cls_type).all():
                    all_dict[cls_inst.__class__.
                             __name__ + "." + cls_inst.id] = cls_inst
            return all_dict

    def new(self, obj):
        """add the object to the current database session"""
        if self.__session:
            self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        if self.__session:
            self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj and self.__session:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close all open resources"""
        if self.__session:
            self.__session.close()
