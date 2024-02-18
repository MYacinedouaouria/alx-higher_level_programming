""" this is  a test file to test  the Base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys


class TestBase(unittest.TestCase):
    """ test   Base"""

    def setUp(self):
        Base.reset_nb_objects()

    def test_base_asign_auto_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_base_asign_auto_id_plus1(self):
        b2 = Base()
        self.assertEqual(b2.id, 1)


class TestDictionaryToJSONString(unittest.TestCase):

    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        Base.reset_nb_objects()

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.captured_output.truncate(0)
        self.captured_output.truncate(0)

    def test_list_of_dictionary_empty(self):
        json_dictionary = Base.to_json_string([])
        print(json_dictionary)
        output = self.captured_output.getvalue()
        expected_output = "[]\n"
        self.assertEqual(output, expected_output)

    def test_list_of_dictionary_None(self):
        json_dictionary = Base.to_json_string(None)
        print(json_dictionary)
        output = self.captured_output.getvalue()
        expected_output = "[]\n"
        self.assertEqual(output, expected_output)

    def test_list_of_dictionary(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        print(json_dictionary)
        output = self.captured_output.getvalue()
        expected_o = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]\n'
        self.assertEqual(output, expected_o)


class TestSaveSquareToFile(unittest.TestCase):

    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        Base.reset_nb_objects()

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.captured_output.truncate(0)
        self.captured_output.truncate(0)

    def test_save_None_list_square(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            print(file.read())
        output = self.captured_output.getvalue()
        expected_output = "[]\n"
        self.assertEqual(output, expected_output)

    def test_save_empty_list_square(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            print(file.read())
        output = self.captured_output.getvalue()
        expected_output = "[]\n"
        self.assertEqual(output, expected_output)

    def test_save_list_square(self):
        r1 = Square(10, 2, 1)
        Square.save_to_file([r1])
        with open("Square.json", "r") as file:
            print(file.read())
        output = self.captured_output.getvalue()
        expected_output = '[{"id": 1, "x": 2, "size": 10, "y": 1}]\n'
        self.assertEqual(output, expected_output)
