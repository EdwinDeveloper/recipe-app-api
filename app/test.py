from django.test import TestCase

from calc import add, substract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added toguether"""
        self.assertEqual(add(3,8),11)

    def test_substract_numbers(self):
        """Substract number"""
        self.assertEqual(substract(8,4),4)