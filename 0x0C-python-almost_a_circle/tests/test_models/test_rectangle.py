import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys


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

    def test_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)


class TestPrintRectangle(unittest.TestCase):

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

    def test_print_with_id_provided(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (12) 2/1 - 4/6\n"

    def test_print_withid_increment(self):
        r2 = Rectangle(5, 5, 1)
        print(r2)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (1) 1/0 - 5/5\n"


class TestDisplay(unittest.TestCase):

    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.captured_output.truncate(0)
        self.captured_output.seek(0)

    def test_display(self):
        r = Rectangle(3, 2)
        r.display()
        output = self.captured_output.getvalue()
        expected_output = "###\n###\n"
        self.assertEqual(output, expected_output)

    def test_display2(self):
        r = Rectangle(6, 4, 2)
        r.display()
        output = self.captured_output.getvalue()
        expected_output = "  ######\n  ######\n  ######\n  ######\n"
        self.assertEqual(output, expected_output)


class TestDisplay_Position(unittest.TestCase):

    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.captured_output.truncate(0)
        self.captured_output.truncate(0)

    def test_display_position(self):
        r = Rectangle(2, 3, 2, 2)
        r.display()
        output = self.captured_output.getvalue()
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output, expected_output)

    def test_display_position2(self):
        r = Rectangle(3, 2, 1, 0)
        r.display()
        output = self.captured_output.getvalue()
        expected_output = " ###\n ###\n"
        self.assertEqual(output, expected_output)


class TestUpdate_argv(unittest.TestCase):

    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        Base.reset_nb_objects()

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.captured_output.truncate(0)
        self.captured_output.truncate(0)

    def test_update_with_one_arg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        print(r)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (89) 10/10 - 10/10\n"
        self.assertEqual(output, expected_output)

    def test_update_with_two_arg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        print(r)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (89) 10/10 - 2/10\n"
        self.assertEqual(output, expected_output)

    def test_update_with_three_arg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3)
        print(r)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (89) 10/10 - 2/3\n"
        self.assertEqual(output, expected_output)

    def test_update_with_four_arg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        print(r)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (89) 4/10 - 2/3\n"
        self.assertEqual(output, expected_output)

    def test_update_with_five_arg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        print(r)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (89) 4/5 - 2/3\n"
        self.assertEqual(output, expected_output)

    def test_update_with_zero_arg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update()
        print(r)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (1) 10/10 - 10/10\n"
        self.assertEqual(output, expected_output)


class TestUpdate_KWargs(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        Base.reset_nb_objects()

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.captured_output.truncate(0)
        self.captured_output.truncate(0)

    def test_update_with_one_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        print(r)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (1) 10/10 - 10/1\n"
        self.assertEqual(output, expected_output)

    def test_update_with_two_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=1, x=2)
        print(r)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (1) 2/10 - 1/10\n"
        self.assertEqual(output, expected_output)

    def test_update_with_four1_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        print(r)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (89) 3/1 - 2/10\n"
        self.assertEqual(output, expected_output)

    def test_update_with_four_arg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(x=1, height=2, y=3, width=4)
        print(r)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (1) 1/3 - 4/2\n"
        self.assertEqual(output, expected_output)

    def test_update_with_five_arg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(x=1, height=2, y=3, width=4, id=89)
        print(r)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (89) 1/3 - 4/2\n"
        self.assertEqual(output, expected_output)

    def test_update_with_zero_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update()
        print(r)
        output = self.captured_output.getvalue()
        expected_output = "[Rectangle] (1) 10/10 - 10/10\n"
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


class TestRectangleToDictionary(unittest.TestCase):

    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        Base.reset_nb_objects()

    def tearDown(self):
        sys.stdout = sys.__stdout__
        self.captured_output.truncate(0)
        self.captured_output.truncate(0)

    def test_rectangle_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        print(r1_dictionary)
        output = self.captured_output.getvalue()
        expected_output = "{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}\n"
        self.assertEqual(output, expected_output)
