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

#Trying to get image - START
def get_coffee_images(placeholderForRiddles, i):
    """
    This function searches for and returns images for the quiz 
    """
    placeholderImage = placeholderForRiddles[i]["image"]
    return placeholderImage
#Trying to get image - END

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
    
    #first time page loads, sess num is 0, and takes q0 and a0 into coffee answer
    #then i post it, but it all runs again before it checks to see whether it was get or post
    #so sesion num is still zero at that point#

    #Calling question and answer functions - START
    coffee_question = get_coffee_questions(riddles, session['quiz_num'])
    #Trying to get image - START
    coffee_image = get_coffee_images(riddles, session['quiz_num'])
    #Trying to get image - END
    coffee_answer = get_coffee_answers(riddles, session['quiz_num']).lower() # I'd actually put these in the GET request, noting the above ^^^ and get rid of "i"
    #Calling question and answer functions - END
    
    #Now we get the number of riddles in our quiz
    number_of_questions = len(riddles)
    
    if request.method == "GET":
        # print("I am here in the 'if GET' statement")
        return render_template("quiz.html", coffee_question=coffee_question,
                                            coffee_image=coffee_image,
                                            coffee_answer=coffee_answer,
                                            username=session["username"],
                                            score=session["score"],
                                            session=session["quiz_num"],
                                            number_of_questions=number_of_questions)
    #Trying to pass the answer and check if correct - START
    elif request.method == "POST":
        if request.form:
            print('request.form is:', request.form)
            #The guess would equal the user's input
            coffee_guess = request.form["answer"].lower()
            mistake = False
            print("coffee_answer: ", coffee_answer, "coffee_guess:  ", coffee_guess)
            print("session num:", session['quiz_num'])
            #We need to check that our answer is correct
            if coffee_guess == coffee_answer:
                if session['quiz_num'] < len(riddles) - 1:
                    #If it is correct, we add 1 to our score and print some feedback
                    print("right!")
                    #Add points to "score"
                    session['score'] += 1
                    session['quiz_num'] += 1
                    
                    #Now we need to get the next question and its answer, 
                    #remember the session has increased by one
                    coffee_question = get_coffee_questions(riddles, session['quiz_num'])
                    coffee_image = get_coffee_images(riddles, session['quiz_num'])
                    coffee_answer = get_coffee_answers(riddles, session['quiz_num']).lower()
                    
                    print("session['quiz_num'] is: ", session['quiz_num'])
                    
                    #PENDING - Get the Flash to work
                    flash("Correct!")
                    return render_template("quiz.html", username=session["username"], 
                                                coffee_question=coffee_question,
                                                coffee_image=coffee_image,
                                                coffee_answer=coffee_answer,
                                                coffee_guess=coffee_guess,
                                                score=session["score"], 
                                                session=session["quiz_num"],
                                                number_of_questions=number_of_questions,
                                                mistake=mistake)
                
                elif session['quiz_num'] == len(riddles) - 1:
                    #If it is correct, we add 1 to our score and print some feedback
                    print("right!")
                    #Add points to "score"
                    session['score'] += 1
                    # Because we don't want to be out of range, we don't increment session
                    session['quiz_num'] += 0
                    
                    # We get the last question and its answer
                    coffee_question = get_coffee_questions(riddles, session['quiz_num'])
                    coffee_image = get_coffee_images(riddles, session['quiz_num'])
                    coffee_answer = get_coffee_answers(riddles, session['quiz_num']).lower()
                    print("Last question, we now go to game over page")
                    
                    #PENDING - Get the Flash to work
                    flash("Correct!")

                    return render_template("gameover.html", username=session["username"],
                                            coffee_question=coffee_question,
                                            coffee_image=coffee_image,
                                            coffee_answer=coffee_answer,
                                            coffee_guess=coffee_guess,
                                            score=session["score"],
                                            mistake=mistake)

            else:
                print("wrong!")
                print("coffee_guess: ", coffee_guess)
                mistake = True
                flash("Wrong!")
                return render_template("quiz.html", username=session["username"], 
                                            coffee_question=coffee_question,
                                            coffee_image=coffee_image,
                                            coffee_answer=coffee_answer,
                                            coffee_guess=coffee_guess,
                                            score=session["score"],
                                            session=session["quiz_num"],
                                            number_of_questions=number_of_questions,
                                            mistake=mistake)
                
        #Trying to pass the answer and check if correct - END

    
    #PENDING - When a guess is wrong, create a collapse that lets the user 
    #choose to see the correct answer or keep trying. Link to the Bootstrap 
    #Collapse in the readme
    
    
# PENDING - Changes need to be made as the program runs when testing which is 
#unwanted. 

if __name__ == "__main__":
    # game_loop()
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)