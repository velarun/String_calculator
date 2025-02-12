import unittest
from string_calculator import Add


class TestStringCalculator(unittest.TestCase):
    # Checking Empty string
    def test_empty_string(self):
        self.assertEqual(Add(""), 0)

    # Checking Empty block
    def test_empty_block(self):
        self.assertEqual(Add({}), 0)

    # Checking zero
    def test_zero(self):
        self.assertEqual(Add(0), 0)
