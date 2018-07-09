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
    
    def test_load_questions(self):
        """
        Test to ensure that questions are being loaded
        """
        dictionary = app.get_coffee_questions()
        self.assertGreater(len(dictionary), 0)
        
    def test_right_number_of_coffee_questions(self):
        """
        Checks that we have the right amount of questions in our quiz
        """
        quiz_length = app.get_coffee_questions()
        print(quiz_length)
        self.assertEqual(quiz_length, 12)
        
print("All the tests passed!")