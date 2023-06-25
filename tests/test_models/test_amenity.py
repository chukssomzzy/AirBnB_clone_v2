#!/usr/bin/python3
""" """
from os import getenv
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "db")
    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "db")
    def test_db_insert(self):
        pass
