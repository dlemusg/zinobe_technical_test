from importlib.resources import path
import unittest
from unittest.mock import patch
from urllib import response

from joblib import parallel_backend

from app import get_all_countries


class TestApp(unittest.TestCase):


    def test_get_all_countries(self):
        with patch():

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main
