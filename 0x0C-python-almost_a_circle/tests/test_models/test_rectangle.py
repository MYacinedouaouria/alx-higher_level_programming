import unittest
from models.rectangle import Rectangle, Base
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    def setUpClass(self):
        Base.reset_nb_objects()

    def test_rectangle(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(2, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, 3)

    def test_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)


class TestDisplay(unitest.TestCase):

    def setUp(self):
        captured_output = String_IO()
        sys.stdout = captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.captured_output.truncate(0)
        self.captured_output.seek(0)

    def test_display(self):
        r = Rectangle(3, 2)
        r.display()
        output = captured_output.getvalue()
        expected_output = "###\n###\n"
        self.assertEqual(output, expected_output)

    def test_display2(self):
        r = Rectangle(6, 4)
        r.display()
        output = captured_output.getvalue()
        expected_output = "######\n######\n######\n######\n"
        self.assertEqual(output, expected_output)


class TestRectangleInputsTypes(unittest.TestCase):

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError) as e:
            Rectangle("w", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(None, 2)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(None, 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(3, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(2, None)
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(3, 2, "x", 2)
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(2, 3, None, 2)
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(3, 2, 2, "y")
        self.assertEqual(str(e.exception), "y must be an integer")

        with self.assertRaises(TypeError) as e:
            Rectangle(2, 3, 2, None)
        self.assertEqual(str(e.exception), "y must be an integer")


class TestRectangleInputsValues(unittest.TestCase):

    def test_width_under_or_equal_zero(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(-5, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_under_or_equal_zero(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(2, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(5, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_under_zero(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(3, 2, -2, 5)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_under_zero(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(3, 2, 2, -5)
        self.assertEqual(str(e.exception), "y must be >= 0")
