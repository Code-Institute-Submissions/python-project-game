import os
import json
from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = "coffee_secret"
app.url_map.strict_slashes = False

# def quiz_menu():
#     """
#     Allows the user to begin the quiz
#     """
#     print("1. Start Quiz!")
#     print("2. Quit Game")
    
#     #Then we'll write an option variable that takes user's input
#     option = input("Enter option: ")
#     #Our function is going to return whathever option our user selects
#     return option


# def start_coffee_questions():
#     """
#     Gets the questions from our .json file
#     """
    
#     #We open our json file and name it coffee_quiz
#     with open("data/coffee_questions.json", "r") as file:
#         coffee_quiz = json.load(file)
#         # print(coffee_quiz["quiz_1"]["question"], coffee_quiz["quiz_2"]["question"])
#         # print(coffee_quiz)
#         for key, value in coffee_quiz.items():
#             print(value["question"])
#             print(value["answer"])

#     #Now we get the length of our list of questions, which will be needed to keep
#     #track of scores and let the user know how long is the quiz
#     number_of_coffee_questions = len(coffee_quiz)
#     print(number_of_coffee_questions)
    
#     #At this point, we need to iterate through our json file in order to get 
#     #our questions and answers, which we'll need for scoreing and guesses below
    
#     ##PENDING - GET Q & A - FOR LOOP ?
    
#     #We initialise an empty variable to keep track of the score
#     score = 0
    
#     #And we're ready to allow our user to input their guess
    
#     ##ANOTHER FOR LOOP FOR THE GUESSES OF EACH Q&A ?
      
#     return coffee_quiz
    
# def game_loop():
#     """Activates our game"""
#     while True:
#         option = quiz_menu()
#         if option == "1":
#             # print("You selected 'Start Quiz!'")
#             start_coffee_questions()
#             # ask_questions()
#         elif option == "2":
#             print("Thanks for Playing. Good Bye")
#             break
#         else:
#             print("Invalid option")
#         #After everything we'll print a blank line for aesthetic reasons
#         print("")

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/quiz", methods=["POST"])
# We create a var with a couple of question to get it to work on a simple level
def start_coffee_questions():

    riddles = [
        {"question": "short coffee?", "answer": "Espresso"},
        {"question": "Long coffee?", "answer": "Americano"},
        {"question": "Milky coffee?", "answer": "Latte"}
    ] 

    if request.form["username"]:
        username = request.form["username"]
        print(username)
        flash("Let's Start, {}!".format(username))
        
        #Trying to add questions - START
        
        first_question = riddles[0]["question"]
        print(first_question)
        first_answer = riddles[0]["answer"]
        print(first_answer)
        
        score = 0
        
        #Tryingto add questions - END
        
        return render_template("quiz.html", username=username)
    
    #PENDING - In order to render the questions in the same quiz.html we'll need ajax.
    #See the readme file for an example
    
   
    

    # session = 1
    
    # if request.method == "POST":
    #     if request.form["answer"].lower() == first_answer:
    #         score += 1
    #         flash("Correct!")
    
    #     return render_template("quiz.html", first_question=first_question)
    
    
    
    # #Logic example 
    # if request.method == "POST" and session["riddle_num"] < len(riddles):
    #     previous_riddle = riddles[session["riddle_num"]]
    #     if request.form["answer"].lower() == previous_riddle["answer"]:
    #         session["riddle_num"] += 1
    #         session["score"] += 1
    #         if session["riddle_num"] < len(riddles):
    #             flash("Correct answer, %s! Your score is %s." % (
    #                   session["player"], session["score"]))
        
# @app.route("/index/<quiz_number>", methods=["GET", "POST"])
# def start_coffee_questions(quiz_number):
#     coffee_question = {}
    
#     with open("data/coffee_questions.json", "r") as file:
#         quiz = json.load(file)
        
#         # print(quiz["quiz_1"]["question"], quiz["quiz_2"]["question"])
#         # print(quiz)
#         # for key, value in quiz.items():
#         #     print(value["question"])
#         #     print(value["answer"])

        
#         for question in quiz:
#             if question["url"] == quiz_number:
#                 coffee_question = question
                
#     return render_template("quiz.html", coffee_question=coffee_question)
    


#     #Now we get the length of our list of questions, which will be needed to keep
#     #track of scores and let the user know how long is the quiz
#     number_of_coffee_questions = len(coffee_quiz)
#     print(number_of_coffee_questions)
    
# PENDING - Changes need to be made as the program runs when testing which is 
#unwanted. Try moving the game_loop function later
# game_loop()

# start_coffee_questions()

if __name__ == "__main__":
    # game_loop()
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)