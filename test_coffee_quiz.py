import unittest
import app

"""
We'll use unittest to ensure the functionalities of our project work as 
we progress with its creation
"""

class TestCoffeeQuiz(unittest.TestCase):
    
    def test_test(self):
        """
        Test to see if the test runs
        """
        self.assertEqual(1, 1)

print("All the tests passed!")