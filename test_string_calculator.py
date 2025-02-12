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

    # Checking positive use case with string of nums
    def test_single_number(self):
        self.assertEqual(Add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(Add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(Add("1,2,3,4"), 10)

    # Checking negative numbers and throw error
    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            Add("1,-2,3,-4")
        self.assertEqual(str(context.exception),
                         "negatives not allowed: -2, -4")

    # Checking nums greater than 1000
    def test_ignore_numbers_greater_than_1000(self):
        self.assertEqual(Add("2,1001"), 2)

    # Omitting new line and get the result
    def test_newline_as_delimiter(self):
        self.assertEqual(Add("1\n2,3"), 6)
