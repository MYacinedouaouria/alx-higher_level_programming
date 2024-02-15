""" this is  a test file to test  the Base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ test   Base"""

    def test_base_asign_auto_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_base_asign_auto_id_plus1(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)
