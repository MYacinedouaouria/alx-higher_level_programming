import unittest
from models.rectangle import Rectangle, Base


class TestRectangle(unittest.TestCase):
    def setUp(self):
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

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError) as e:
            Rectangle("w", 2)
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