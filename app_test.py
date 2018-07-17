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


#Now we start writing our routes
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
def get_coffee_quiz():
    i = session['quiz_num']
    coffee_question = get_coffee_questions(riddles, i)
    coffee_answer = get_coffee_answers(riddles, i).lower()
    number_of_questions = len(riddles)
    if request.method == "POST":
        if request.form:
            #The guess would equal the user's input
            coffee_guess = request.form["answer"].lower()
            
            #We need to check that our answer is correct
            if coffee_guess == coffee_answer:
                #If it is correct, we add 1 to our score and print some feedback
                #Add points to "score"
                session['score'] += 1
                session['quiz_num'] += 1
                coffee_question = get_coffee_questions(riddles, i+1)
                number_of_questions = len(riddles)
                
    return render_template("gameover.html", username=session["username"], 
                                            coffee_question=coffee_question,
                                            coffee_answer=coffee_answer,
                                            score=session["score"])

if __name__ == "__main__":
    # game_loop()
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)