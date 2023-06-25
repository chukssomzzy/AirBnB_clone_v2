#!/usr/bin/python3
""" """
from os import getenv
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models import storage


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    if getenv("HBNB_TYPE_STORAGE") == "db":
        def tearDown(self):
            """specialized clean up"""
            sql = "DROP TABLE IF EXISTS {};".format(self.value.__tablename__)
            self._cur.execute(sql)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        def setUp(self):
            storage.reload()
            self.i = self.value(
                password="password", email="email@airbnb.com",
                first_name="first", last_name="last")
            self.i.save()
            storage.save()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "filestorage")
    def test_db_save(self):
        """test if object are correctly save in db"""
        sql = """SELECT id FROM {} WHERE id = %s;
                                """.format(self.value.__tablename__)
        id = self._cur.execute(sql, (self.i.id, ))
        self.assertIsNotNone(id)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", 'db')
    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "db")
    def test_first_name_db(self):
        """skip test if storage type is fs"""
        self.assertEqual(type(self.i.first_name), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "db")
    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "fs")
    def test_last_name_db(self):
        """ test if last name is a string"""
        self.assertEqual(type(self.i.last_name), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "db")
    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "fs")
    def test_email_db(self):
        """TEST db init"""
        self.assertEqual(type(self.i.email), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "db")
    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "fs")
    def test_password_db(self):
        """ test password for db storage """
        self.assertEqual(type(self.i.password), str)
