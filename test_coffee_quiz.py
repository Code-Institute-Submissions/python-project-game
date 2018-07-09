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
        
    def test_quiz_menu(self):
        """
        Test to ensure the button contains the message to start the quiz
        """
        menu = app.quiz_menu()
        self.assertTrue("1. Start Quiz!" in menu)
    
    def test_load_questions(self):
        """
        Test to ensure that questions are being loaded
        """
        coffee_questions = app.get_coffee_questions("coffee_questions.txt")
        self.assertGreater(len(coffee_questions), 0)
        
print("All the tests passed!")