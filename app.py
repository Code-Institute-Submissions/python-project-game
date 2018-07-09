import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "coffee_secret"

def quiz_menu():
    """Allows the user to begin the quiz"""
    print("1. Start Quiz!")
    print("2. Quit Game")
    
    #Then we'll write an option variable that takes user's input
    option = input("Enter option: ")
    #Our function is going to return whathever option our user selects
    return option


def get_coffee_questions():
    """
    Gets the questions from our .json file
    """
    
    #We open our json file and name it coffee_quiz
    with open("data/coffee_questions.json", "r") as file:
        coffee_quiz = json.load(file)
        print(coffee_quiz["quiz_1"]["question"], coffee_quiz["quiz_2"]["question"])
        return coffee_quiz

    #Now we get the length of our list of questions, which will be needed to keep
    #track of scores and let the user know how long is the quiz
    
        
        
        
def game_loop():
    """Activates our game"""
    while True:
        option = quiz_menu()
        if option == "1":
            # print("You selected 'Start Quiz!'")
            get_coffee_questions()
            # ask_questions()
        elif option == "2":
            print("Thanks for Playing. Good Bye")
            break
        else:
            print("Invalid option")
        #After everything we'll print a blank line for aesthetic reasons
        print("")

# @app.route("/")
# def index():
#     return render_template("index.html")
# print("this works!")

# game_loop()

if __name__ == "__main__":
    game_loop()
    # app.run(host=os.environ.get("IP"),
    #         port=int(os.environ.get("PORT")),
    #         debug=True)