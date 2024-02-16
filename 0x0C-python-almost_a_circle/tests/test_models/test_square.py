#!/usr/bin/python3

from models.base import Base
from models.rectangle import Rectangle
import sys
from io import stringIO
import unittest


class TestPrintSquare(unittest.TestCase):

    @classmethod
    def setUPClass(self):
        Base.reset_nb_objects()

    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.captured_output.truncate(0)
        self.captured_output.seek(0)

    def test_print_with_1args(self):
        s = Square(5)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (1) 0/0 - 5\n"
        self.assertEqual(output, expected_output)

    def test_print_with_2args(self):
        s = Square(2, 2)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (2) 2/0 - 2\n"
        self.assertEqual(output, expected_output)

    def test_print_with_3args(self):
        s = Square(3, 1, 3)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (3) 1/3 - 3\n"
        self.assertEqual(output, expected_output)

    def test_print_with_4args(self):
        s = Square(3, 1, 3, 89)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (89) 1/3 - 3\n"
        self.assertEqual(output, expected_output)
