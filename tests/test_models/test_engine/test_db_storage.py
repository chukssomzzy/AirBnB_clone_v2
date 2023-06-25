#!/usr/bin/python3
"""Test database Storage engine"""
import MySQLdb
from models import storage
from os import getenv
import unittest
from models.city import City

from models.state import State
from models.user import User


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db" and getenv(
    "HBNB_ENV") == "test", "skip if filestorage is in use")
class test_db_storage(unittest.TestCase):
    """defines test cases"""

    @classmethod
    def setUpClass(cls):
        """setup class"""
        if getenv("HBNB_TYPE_STORAGE"
                  ) == 'db' and getenv('HBNB_ENV') == 'test':
            cls._conn = MySQLdb.connect(host=getenv('HBNB_MYSQL_HOST'),
                                        passwd=getenv('HBNB_MYSQL_PWD'),
                                        user=getenv('HBNB_MYSQL_USER'),
                                        db=getenv('HBNB_MYSQL_DB'))
            cls._cur = cls._conn.cursor()

    @classmethod
    def tearDownClass(cls) -> None:
        """Close all connection"""
        cls._cur.close()
        cls._conn.close()

    def setUp(self):
        """Delete all content in storage"""
        storage.reload()
        user_ins = User(first_name="first_name", last_name="last_name",
                        email="first@email.com", password="passwoRD123#")
        user_ins.save()
        state_ins = State(name="lagos")
        state_ins.save()
        city_ins = City(name="ojo", state_id=state_ins.id)
        city_ins.save()
        storage.save()

        self.inst_list = [user_ins, state_ins, city_ins]

    def tearDown(self):
        """Defines tear down"""
        for obj in storage.all().values():
            obj.delete()
        storage.save()

    def test_Not_empty(self):
        """Test empty db"""
        self.assertNotEqual(len(storage.all()), 0)

    def test_new(self):
        """Test if new obj are correctly add ed to storage"""

        for ins in self.inst_list:
            sql = """SELECT id FROM {}
                        WHERE id = %s""".format(ins.__tablename__)
            obj_id = self._cur.execute(sql, (ins.id,))
            self.assertIsNotNone(obj_id)

    def test_all(self):
        """ Make sure all returns obj based  on the class passed"""

        for ins in self.inst_list:
            key = ins.__class__.__name__ + "." + ins.id
            dict_ins = storage.all(ins.__class__)
            self.assertEqual(len(dict_ins), 1)
            self.assertTrue(ins is dict_ins[key])

    def test_deletes(self):
        """Test deletion function on data"""
        for key, val in storage.all().items():
            val.delete()
            sql = """SELECT id FROM {}
                        WHERE id = %s
                              """.format(val.__tablename__)
            ins_t = self._cur.execute(sql, (val.id,))
            if not ins_t:
                self.assertEqual(ins_t, 0)
