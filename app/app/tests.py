"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(calc.add(1, 2), 3)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted from each other"""
        self.assertEqual(calc.subtract(3, 2), 1)

    def test_multiply_numbers(self):
        """Test that two numbers are multiplied together"""
        self.assertEqual(calc.multiply(3, 2), 6)

    def test_divide_numbers(self):
        """Test that two numbers are divided together"""
        self.assertEqual(calc.divide(6, 2), 3)
