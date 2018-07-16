import os
import json
from flask import Flask, render_template, request, flash, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "coffee_secret"
app.url_map.strict_slashes = False


#Opening my JSON to get the questions and answers for the riddles
riddles = []
with open("data/coffee_questions.json", "r") as json_file:
    riddles = json.load(json_file)
    
# i = 0


def get_coffee_questions(placeholderForRiddles, i):
    """
    This function searches for and returns questions for the quiz 
    """
    placeholderQuestion = placeholderForRiddles[i]["question"]
    return placeholderQuestion


def get_coffee_answers(placeholderForRiddles, i):
    """
    This function searches for and returns answers for the quiz 
    """
    placeholderAnswer = placeholderForRiddles[i]["answer"]
    return placeholderAnswer

    
#EXAMPLE: example of strategy to get all questions:
# def get_question(index):
    # question = questions_list[index]["question"]
    # return question

#EXAMPLE: example of strategy to get all questions:
# question = get_question(session["question"])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session['username'] = request.form["username"]
        # Initialising a "score" variable to keep track of points
        session['score'] = 0
        session['quiz_num'] = 0
        return redirect(url_for("get_coffee_quiz"))
    return render_template("index.html")
    

@app.route("/quiz", methods=["GET", "POST"])
# We create a var with a couple of question to get it to work on a simple level
def get_coffee_quiz():

    i = session['quiz_num']

    #Adding first question - START
    #To avoid having nested functions, the get_coffee_questions function was
    #moved to upper lines and just called here
    coffee_question = get_coffee_questions(riddles, i)
    
    #Adding first question - END
    
    #Now we get the number of riddles in our quiz
    number_of_questions = len(riddles)
    print(number_of_questions)
    
    #EXAMPLE: example of strategy to get all questions:
    # question = get_question(session["question"])
    
    if request.method == "GET":
        #EXAMPLE: example of strategy to get all questions:
        #question = get_question(session["question"])
        print("En el 'if GET', la variable coffee_question es: " + coffee_question)
        return render_template("quiz.html", coffee_question=coffee_question,
                                            username=session["username"],
                                            score=session["score"])
    
    
    #Trying to pass the answer and check if correct - START
    coffee_answer = get_coffee_answers(riddles, i).lower()
    
    if request.method == "POST":
        if request.form:
            print(request.form)
            #The guess would equal the user's input
            first_guess = request.form["answer"].lower()
            print(coffee_answer, first_guess)
            
            #We need to check that our answer is correct
            if first_guess == coffee_answer:
                #If it is correct, we add 1 to our score and print some feedback
                print("right!")
                #Add points to "score"
                session['score'] += 1
                print(session['score'])
                session['quiz_num'] += 1
                print(session['quiz_num'])
                #PENDING - Get the Flash to work
                flash("Correct!")
            else:
                print("wrong!")
            
        #Trying to pass the answer and check if correct - END

        return render_template("quiz.html", username=session["username"], 
                                            coffee_question=coffee_question,
                                            coffee_answer=coffee_answer,
                                            first_guess=first_guess,
                                            score=session["score"])
    
    #PENDING - When a guess is wrong, create a collapse that lets the user 
    #choose to see the correct answer or keep trying. Link to the Bootstrap 
    #Collapse in the readme
    
    #PENDING - Add "Question" to session. Initialise in 0, this will store
    #the question's index and we'll be able to move from 1 to 12 without
    #refreshing, using ajax or lots of URLs
 
    
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
# def get_coffee_quiz(quiz_number):
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

# get_coffee_quiz()

if __name__ == "__main__":
    # game_loop()
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)