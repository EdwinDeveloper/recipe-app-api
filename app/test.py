from django.test import TestCase

from calc import add

class CalcTest(TestCase):
    
    def test_add_numbers(self):
        """Test that two numbers are added toguether"""
        self.assertEqual(add(3,8),11)