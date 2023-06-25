#!/usr/bin/python3
""" """
from os import getenv
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
from models import storage


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
    if getenv("HBNB_TYPE_STORAGE") == "db":
        def setUp(self):
            """Set up instance """
            self.newState = State(name="Lagos")
            self.newState.save()
            self.i = self.value(name="ojo", state_id=self.newState.id)
            storage.reload()
            self.i.save()

    if getenv("HBNB_TYPE_STORAGE") == "db":
        def tearDown(self):
            """specialized clean up"""
            self.newState.delete()
            storage.save()
            sql = "DROP TABLE IF EXISTS {};".format(self.value.__tablename__)
            self._cur.execute(sql)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "filestorage")
    def test_db_save(self):
        """test if object are correctly save in db"""
        sql = """SELECT id FROM {} WHERE id = %s""".format(
            self.value.__tablename__)
        id = self._cur.execute(sql, (self.i.id, ))
        self.assertIsNotNone(id)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "database storage ")
    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "storage engine")
    def test_state_id_db(self):
        """test id """
        self.assertEqual(type(self.i.id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "db")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", 'fs')
    def test_name_db(self):
        """Test name"""
        self.assertEqual(type(self.i.name), str)
