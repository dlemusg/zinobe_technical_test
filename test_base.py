from importlib.resources import path
import unittest
from unittest.mock import patch, MagicMock,Mock
import sqlite3
from core_app import get_all_countries, get_coutries_by_region, encode_language, table_to_json
from database import sql_connection
import os.path


class TestApp(unittest.TestCase):


    def test_get_all_countries(self):

        """
        Description
        ---------
        Test get_all_countries()
        Prueba de conexión al api
        """


        with patch('requests.get') as patched_get:
            get_all_countries()
            patched_get.assert_called_once_with('https://restcountries.com/v3.1/all')


    def test_get_countries_by_region(self):
        """
        
        Description
        ---------
        Test get_countries_by_region()
        Prueba de conexión al api
        """
        with patch('requests.get') as patched_get:
            get_coutries_by_region(['africa'])

            patched_get.assert_called_once_with('https://restcountries.com/v3.1/region/africa')

       
    def test_sql_connection(self):

        """
        Description
        ---------
        Test sql_connection()
        Prueba de conexión a la base de datos
        """
        sqlite3.connect = MagicMock(return_value='connection succeeded')
        dbc = sql_connection()
        sqlite3.connect.assert_called_with('database.db')
        self.assertEqual(dbc,'connection succeeded')



    def test_encode_num(self):
        """
        Description
        ---------
        Test encode_language()
        Prueba de encriptación de cadenas de texto
        Evalua si la cadena es texto o numero
        """
        result = encode_language(1)
        self.assertEqual(result,'Error')

    def test_json(self):
        """
        Description
        ---------
        Test table_to_json()
        Evalua que se genere el archivo json bajo el nombre data.json
        """
        test = ['a','b','c']
        table_to_json(test)
        os.path.exists('data.json') == True

        
            
if __name__ == "__main__":
    unittest.main
