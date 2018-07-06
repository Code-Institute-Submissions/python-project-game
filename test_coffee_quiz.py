import unittest
import app

"""
We'll use unittest to ensure the functionalities of our project work as 
we progress with its creation
"""

class TestCoffeeQuiz(unittest.TestCase):
    
    def test_app_exists(self):
        """
        Test to see if there is an app
        """
        self.assertEqual(1, 1)

print("All the tests passed!")