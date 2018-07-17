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
        #Initialising a session that will keep track of the number of questions
        session['quiz_num'] = 0
        return redirect(url_for("get_coffee_quiz"))
    return render_template("index.html")
    

@app.route("/quiz", methods=["GET", "POST"])
def get_coffee_quiz():

    i = session['quiz_num']

    #Calling question and answer functions - START
    coffee_question = get_coffee_questions(riddles, i)
    coffee_answer = get_coffee_answers(riddles, i).lower()
    #Calling question and answer functions - END
    
    #Now we get the number of riddles in our quiz
    number_of_questions = len(riddles)

    if request.method == "GET":
        # print("En el 'if GET', la variable coffee_question es: " + coffee_question)
        return render_template("quiz.html", coffee_question=coffee_question,
                                            username=session["username"],
                                            score=session["score"],
                                            number_of_questions=number_of_questions)
    
    if request.method == "POST":
        if request.form:
            print(request.form)
            #The guess would equal the user's input
            coffee_guess = request.form["answer"].lower()
            print(coffee_answer, coffee_guess)
            #We need to check that our answer is correct
            if coffee_guess == coffee_answer:
                if session['quiz_num'] < 12:
                    #If it is correct, we add 1 to our score and print some feedback
                    print("right!")
                    #Add points to "score"
                    session['score'] += 1
                    session['quiz_num'] += 1
                    print(session['quiz_num'])
                    #PENDING - Get the Flash to work
                    flash("Correct!")
                    return render_template("quiz.html", username=session["username"], 
                                                coffee_question=coffee_question,
                                                coffee_answer=coffee_answer,
                                                score=session["score"])
                else:
                    session['score'] += 1
                    return render_template("gameover.html", username=session["username"], 
                                                coffee_question=coffee_question,
                                                coffee_answer=coffee_answer,
                                                score=session["score"])
            else:
                print("wrong!")
                return render_template("quiz.html", username=session["username"], 
                                            coffee_question=coffee_question,
                                            coffee_answer=coffee_answer,
                                            score=session["score"])
                                            
                # PENDING - Get the collapsible button to render when wrong
                # answer is given (see html for attempt)
                
            
        #Trying to pass the answer and check if correct - END

    
    #PENDING - When a guess is wrong, create a collapse that lets the user 
    #choose to see the correct answer or keep trying. Link to the Bootstrap 
    #Collapse in the readme
    
 
    
    # #Logic example 
    # if request.method == "POST" and session["riddle_num"] < len(riddles):
    #     previous_riddle = riddles[session["riddle_num"]]
    #     if request.form["answer"].lower() == previous_riddle["answer"]:
    #         session["riddle_num"] += 1
    #         session["score"] += 1
    #         if session["riddle_num"] < len(riddles):
    #             flash("Correct answer, %s! Your score is %s." % (
    #                   session["player"], session["score"]))
        
    
# PENDING - Changes need to be made as the program runs when testing which is 
#unwanted. 


if __name__ == "__main__":
    # game_loop()
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)