import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "coffee_secret"

def quiz_menu():
    """Allows the user to begin the quiz"""
    print("1. Start Quiz!")
    print("2. Quit Game")
    return("1. Start Quiz!", "2. Quit Game")

def get_coffee_questions():
    """
    Gets the questions from our .txt file
    """
    with open("coffee_questions.txt") as file:
        for question in file:
            return question
    
def game_loop():
    """Activates our game"""
    while True:
        option = quiz_menu()
        if option == "1":
            print("You selected 'Ask Questions'")
            # ask_questions()
        elif option == "2":
            print("Thanks for Playing. Good Bye")
            break
        else:
            print("Invalid option")
        #After everything we'll print a blank line for aesthetic reasons
        print("")

@app.route("/")
def index():
    return render_template("index.html")
print("this works!")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)