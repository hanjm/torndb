# coding=utf-8

import unittest
import torndb


class TestTorndb(unittest.TestCase):
    def setUp(self):
        self.conn = torndb.Connection(host="127.0.0.1", database="solobookmovies")

    def test_get(self):
        res = self.conn.get("select 2017")
        self.assertEqual(res, {'2017': 2017})

    def test_query(self):
        res = self.conn.get("select 1,2")
        self.assertEqual(res, {'1': 1, '2': 2})

    def tearDown(self):
        self.conn.close()


if __name__ == '__main__':
    unittest.main()
