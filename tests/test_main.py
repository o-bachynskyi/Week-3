import unittest
from Calculator import subtract

class TestMain(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)
