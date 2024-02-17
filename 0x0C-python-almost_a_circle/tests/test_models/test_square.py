#!/usr/bin/python3

from models.base import Base
from models.square import Square
import sys
from io import StringIO
import unittest


class TestPrintSquare_Andarea(unittest.TestCase):

    @classmethod
    def setUPClass(self):
        Base.reset_nb_objects()

    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        Base.reset_nb_objects()

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.captured_output.truncate(0)
        self.captured_output.seek(0)

    def test_print_with_1args(self):
        s = Square(5)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (1) 0/0 - 5\n"
        self.assertEqual(s.area(), 25)
        self.assertEqual(output, expected_output)

    def test_print_with_2args(self):
        s = Square(2, 2)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (1) 2/0 - 2\n"
        self.assertEqual(s.area(), 4)
        self.assertEqual(output, expected_output)

    def test_print_with_3args(self):
        s = Square(3, 1, 3)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (1) 1/3 - 3\n"
        self.assertEqual(s.area(), 9)
        self.assertEqual(output, expected_output)

    def test_print_with_4args(self):
        s = Square(3, 1, 3, 89)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (89) 1/3 - 3\n"
        self.assertEqual(s.area(), 9)
        self.assertEqual(output, expected_output)


class TestDisplay(unittest.TestCase):

    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.captured_output.truncate(0)
        self.captured_output.seek(0)

    def test_display_with_1args(self):
        s = Square(5)
        s.display()
        output = self.captured_output.getvalue()
        expected_output = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(output, expected_output)

    def test_display_with_2args(self):
        s = Square(2, 2)
        s.display()
        output = self.captured_output.getvalue()
        expected_output = "  ##\n  ##\n"
        self.assertEqual(output, expected_output)

    def test_display_with_3args(self):
        s = Square(3, 1, 3)
        s.display()
        output = self.captured_output.getvalue()
        expected_output = "\n\n\n ###\n ###\n ###\n"
        self.assertEqual(output, expected_output)
