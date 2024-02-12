import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    r1 = Rectangle(10, 2)
    r2 = Rectangle(2, 10)
    r3 = Rectangle(10, 2, 0, 0, 12)
    r4 = Rectangle(2, 10)

    def test_rectangle(self):
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, 3)
