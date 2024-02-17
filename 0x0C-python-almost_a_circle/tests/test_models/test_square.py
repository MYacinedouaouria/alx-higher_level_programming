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


class TestSquareInputsTypes(unittest.TestCase):

    def test_invalid_size_type(self):
        with self.assertRaises(TypeError) as e:
            Square(None)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            Square("s")
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError) as e:
            Square(2, None)
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(TypeError) as e:
            Square(2, "s")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError) as e:
            Square(2, 3, None)
        self.assertEqual(str(e.exception), "y must be an integer")

        with self.assertRaises(TypeError) as e:
            Square(2, 2, "y")
        self.assertEqual(str(e.exception), "y must be an integer")


class TestSquareInvalidValues(unittest.TestCase):

    def test_size_under_or_equal_zero(self):
        with self.assertRaises(ValueError) as e:
            Square(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Square(-5, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_x_under_zero(self):
        with self.assertRaises(ValueError) as e:
            Square(3, -2, 2)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_under_zero(self):
        with self.assertRaises(ValueError) as e:
            Square(3, 2, -5)
        self.assertEqual(str(e.exception), "y must be >= 0")


class TestUpdateSquare(unittest.TestCase):

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

    def test_update_with_1args(self):
        s = Square(5)
        s.update(10)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (10) 0/0 - 5\n"
        self.assertEqual(output, expected_output)

    def test_update_with_2args(self):
        s = Square(5)
        s.update(1, 2)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (1) 0/0 - 2\n"
        self.assertEqual(output, expected_output)

    def test_update_with_3args(self):
        s = Square(5)
        s.update(1, 2, 3)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (1) 3/0 - 2\n"
        self.assertEqual(output, expected_output)

    def test_update_with_4args(self):
        s = Square(5)
        s.update(1, 2, 3, 4)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (1) 3/4 - 2\n"
        self.assertEqual(output, expected_output)

    def test_update_with_0args(self):
        Base.reset_nb_objects()
        s = Square(5)
        s.update()
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (1) 0/0 - 5\n"
        self.assertEqual(output, expected_output)

    def test_update_with_1kwargs(self):
        s = Square(5)
        s.update(id=10)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (10) 0/0 - 5\n"
        self.assertEqual(output, expected_output)

    def test_update_with_2kwargs(self):
        s = Square(5)
        s.update(id=1, size=2)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (1) 0/0 - 2\n"
        self.assertEqual(output, expected_output)

    def test_update_with_3kwargs(self):
        s = Square(5)
        s.update(id=1, size=2, x=3)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (1) 3/0 - 2\n"
        self.assertEqual(output, expected_output)

    def test_update_with_4kwargs(self):
        s = Square(5)
        s.update(id=1, size=2, x=3, y=4)
        print(s)
        output = self.captured_output.getvalue()
        expected_output = "[Square] (1) 3/4 - 2\n"
        self.assertEqual(output, expected_output)


class TestSquareToDictionry(unittest.TestCase):

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

    def test_square_to_dictionary(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        print(s1_dictionary)
        output = self.captured_output.getvalue()
        expected_output = "{'id': 1, 'x': 2, 'size': 10, 'y': 1}"
        self.assertEqual(output, expected_output)
