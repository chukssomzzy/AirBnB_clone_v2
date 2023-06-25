#!/usr/bin/python3
""" """
from os import getenv
import unittest

from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models import storage


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    if getenv("HBNB_TYPE_STORAGE") == "db":
        def setUp(self):
            storage.reload()
            self.i = self.value(name="Lagos")
            self.i.save()
            storage.save()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "db")
    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "fs")
    def test_name3_db(self):
        """ """
        self.assertEqual(type(self.i.name), str)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        def tearDown(self):
            """specialized clean up"""
            self.i.delete()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "filestorage")
    def test_db_save(self):
        """test if object are correctly save in db"""
        self.i.save()
        sql = """SELECT id FROM {} WHERE id = %s;""".format(
            self.value.__tablename__)
        id = self._cur.execute(sql, (self.i.id, ))
        self.assertIsNotNone(id)
