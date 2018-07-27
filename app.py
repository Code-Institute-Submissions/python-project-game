import os
import json
from flask import Flask, render_template, request, flash, redirect, session, url_for
#PENDING find a way to get the images from the url in the json files and get the
#logic so they render when they're supossed to [maybe importing urllib2 as explained in:
#https://stackoverflow.com/questions/12511408/accepting-json-image-file-in-python]

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
# def get_coffee_images(placeholderForRiddles, i):
#     """
#     This function searches for and returns images for the quiz 
#     """
#     placeholderImage = placeholderForRiddles[i]["image"]
#     return placeholderImage
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
    
    #first ime page loads, sess num is 0, and takes q0 and a0 into coffee answer
    #then i post it, but it all runs again before it checks to see whether it was get or post
    #so sesion num is still zero at that point#
    i = session['quiz_num'] ############################## This isn't needed if you call get_coffee_questions(riddles, session['quiz_num']) as I did on line 96

    #Calling question and answer functions - START
    coffee_question = get_coffee_questions(riddles, i)
    #Trying to get image - START
    # coffee_image = get_coffee_images(riddles, i)
    #Trying to get image - END
    coffee_answer = get_coffee_answers(riddles, i).lower() #################### I'd actually put these in the GET request, noting the above ^^^ and get rid of "i"
    #Calling question and answer functions - END
    
    #Now we get the number of riddles in our quiz
    number_of_questions = len(riddles)

    if request.method == "GET":
        print("I am here in the 'if GET' statement")
        return render_template("quiz.html", coffee_question=coffee_question,
                                            # coffee_image=coffee_image,
                                            username=session["username"],
                                            score=session["score"],
                                            number_of_questions=number_of_questions)
    #Trying to pass the answer and check if correct - START
    elif request.method == "POST":
    #While this avoided questions twice, The problem with this was that now questions
    #would progress no matter if right or wring
        # session['quiz_num'] += 1
        # print("*****")
        # print(session['quiz_num'])
        # print("experiment")
        print("I am in here in the 'if POST' statement")
        if request.form:
            print(request.form)
            #The guess would equal the user's input
            coffee_guess = request.form["answer"].lower()
            print("correct answer: ", coffee_answer, "user's answer: ", coffee_guess)
            #We need to check that our answer is correct
            if coffee_guess == coffee_answer:
                if session['quiz_num'] < len(riddles):
                    #If it is correct, we add 1 to our score and print some feedback
                    print("right!")
                    #Add points to "score"
                    session['score'] += 1
                    print("before incrementing", session['quiz_num'])
                    session['quiz_num'] += 1
                    print("after incrementing", session['quiz_num'])
                    
                    # You incremented the question number in the session - now you need to remember to
                    # go get the question/answer it corresponds to before returning the template! Without doing that,
                    # the session var still gets incremented but you don't have the new question yet.
                    # Thus it returns the same question the first time, but then starts working properly
                    # after that point, it's just off by 1
                    coffee_question = get_coffee_questions(riddles, session['quiz_num'])
                    coffee_answer = get_coffee_answers(riddles, session['quiz_num']).lower()
                    
                    #PENDING - Get the Flash to work
                    flash("Correct!")
                    return render_template("quiz.html", username=session["username"], 
                                                coffee_question=coffee_question,
                                                # coffee_image=coffee_image,
                                                coffee_answer=coffee_answer,
                                                score=session["score"])
                elif session['quiz_num'] >= len(riddles):
                    session['score'] += 1
                    session['quiz_num'] += 0
                    print("game over")
                    # return redirect("gameover.html")
                    return render_template("gameover.html", username=session["username"], 
                                            score=session["score"])
            else:
                print("wrong!")
                return render_template("quiz.html", username=session["username"], 
                                            coffee_question=coffee_question,
                                            # coffee_image=coffee_image,
                                            coffee_answer=coffee_answer,
                                            score=session["score"])
                
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