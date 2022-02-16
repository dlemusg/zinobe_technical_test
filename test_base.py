from importlib.resources import path
import unittest
from unittest.mock import patch, MagicMock,Mock

import sqlite3

from joblib import parallel_backend

from core_app import get_all_countries, get_coutries_by_region, encode_language
from database import sql_connection


class TestApp(unittest.TestCase):


    def test_get_all_countries(self):
        with patch('requests.get') as patched_get:
            get_all_countries()
            patched_get.assert_called_once_with('https://restcountries.com/v3.1/all')


    def test_get_countries_by_region(self):
        with patch('requests.get') as patched_get:
            get_coutries_by_region(['africa'])

            patched_get.assert_called_once_with('https://restcountries.com/v3.1/region/africa')

       
    def test_sql_connection(self):
        sqlite3.connect = MagicMock(return_value='connection succeeded')
        dbc = sql_connection()
        sqlite3.connect.assert_called_with('database.db')
        self.assertEqual(dbc,'connection succeeded')



    def test_encode_num(self):
        result = encode_language(1)
        self.assertEqual(result,'Error')
        
            

#    def test_get():

 #       pass

  #  def test_insert_bd():
   #     pass


if __name__ == "__main__":
    unittest.main
