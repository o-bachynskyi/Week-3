import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 1), 1)
        self.assertEqual(add(-1, 1), -2)
        self.assertEqual(add(0, 0), 0)
