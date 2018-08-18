import os
import json
from flask import Flask, render_template, request, flash, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "coffee_secret"
app.url_map.strict_slashes = False

# Opening my JSON to get the questions and answers for the riddles
riddles = []
with open("data/coffee_questions.json", "r") as json_file:
    riddles = json.load(json_file)


def get_coffee_questions(placeholderForRiddles, i):
    """
    This function searches for and returns questions for the quiz
    """
    placeholderQuestion = placeholderForRiddles[i]["question"]
    return placeholderQuestion


def get_coffee_images(placeholderForRiddles, i):
    """
    This function searches for and returns images for the quiz
    """
    placeholderImage = placeholderForRiddles[i]["image"]
    return placeholderImage


def get_coffee_answers(placeholderForRiddles, i):
    """
    This function searches for and returns answers for the quiz
    """
    placeholderAnswer = placeholderForRiddles[i]["answer"]
    return placeholderAnswer


# Getting the top scores - START
def add_top_score(username, total_score):
    """This function will open the top-scores file and add a player's username
    and score if they reached the top 5 highest scores"""
    top_players = get_top_players()
    with open('data/top_scores.txt', 'a+') as top_scores:
        if not (username, total_score) in top_players:
            top_scores.write('\n{}:{}'.format(str(username), str(total_score)))


def get_top_players():
    # you should be able to access this here: print(session['score'])
    # Append this player's score to the file with add_top_score()
    with open('data/top_scores.txt', 'r') as top_scores:
        top_players = []
        for line in top_scores.readlines()[1:]:
            top_players.append(line)

        sorted_top_players = []
        for player in top_players:
            tupe = (player.split(':')[0].strip(), int(player.split(':')[1].strip()))
            sorted_top_players.append(tupe)

        # Sort top_players on the 2nd elem of the tuple, reverse the sort,
        # then return the top 5
        # Another way:
        # sorted_final = sorted(sorted_top_players, key=lambda x: x[1])
        # key = def function(x): return x[1]

        return sorted(sorted_top_players, key=lambda x: x[1])[::-1][:5]
# Getting the top scores - END


# Now we start writing our routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session['username'] = request.form["username"]
        # Initialising a "score" variable to keep track of points
        session['score'] = 0
        # Initialising a session that will keep track of  number of questions
        session['quiz_num'] = 0
        # Keeping track of whether the session has ended (game over) or not
        session['end'] = False
        return redirect(url_for("get_coffee_quiz"))
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def get_coffee_quiz():

    # 1st time page loads, sess num is 0 and takes q0 and a0 into coffee answer
    # then i post it, but it all runs again before it checks
    # to see whether it was get or post
    # so sesion num is still zero at that point#

    # Calling question and answer functions - START
    coffee_question = get_coffee_questions(riddles, session['quiz_num'])
    # Trying to get image - START
    coffee_image = get_coffee_images(riddles, session['quiz_num'])
    # Trying to get image - END
    coffee_answer = get_coffee_answers(riddles, session['quiz_num']).lower()
    # I'd actually put these in the GET request, and get rid of "i"
    # Calling question and answer functions - END

    # Now we get the number of riddles in our quiz
    number_of_questions = len(riddles)

    # If the session is over to avoid cheating by coming back to the quiz we'll
    # redirect to the gameover page
    if session['end']:
        top_players = get_top_players()
        return render_template("gameover.html",
                               username=session["username"],
                               score=session["score"],
                               top_players=top_players)

    if request.method == "GET":

        # print("I am here in the 'if GET' statement")
        return render_template("quiz.html",
                               coffee_question=coffee_question,
                               coffee_image=coffee_image,
                               coffee_answer=coffee_answer,
                               username=session["username"],
                               score=session["score"],
                               session=session["quiz_num"],
                               number_of_questions=number_of_questions,
                               end=session['end'])

    # Trying to pass the answer and check if correct - START
    elif request.method == "POST":
        if request.form:
            flag = request.form.keys()
            if request.form.keys()[0] == 'answer':
                print('The request was answer')
                # print('request.form is:', request.form)
                # The guess would equal the user's input
                coffee_guess = request.form['answer'].lower()
                mistake = False
                # print("answer: ", coffee_answer, "guess:  ", coffee_guess)
                # print("session num:", session['quiz_num'])
                # We need to check that our answer is correct
                if coffee_guess == coffee_answer:
                    if session['quiz_num'] < len(riddles) - 1:
                        # If it is correct, we add 1 to our score
                        print("right!")
                        #  points to "score"
                        session['score'] += 1
                        session['quiz_num'] += 1

                        # Now we need to get the next question and its answer,
                        # remember the session has increased by one
                        coffee_question = get_coffee_questions(riddles, session['quiz_num'])
                        coffee_image = get_coffee_images(riddles, session['quiz_num'])
                        coffee_answer = get_coffee_answers(riddles, session['quiz_num']).lower()

                        print("session['quiz_num'] is: ", session['quiz_num'])

                        # PENDING - Get the Flash to work
                        flash("Correct!")
                        return render_template("quiz.html",
                                               username=session["username"],
                                               coffee_question=coffee_question,
                                               coffee_image=coffee_image,
                                               coffee_answer=coffee_answer,
                                               coffee_guess=coffee_guess,
                                               score=session["score"],
                                               session=session["quiz_num"],
                                               number_of_questions=number_of_questions,
                                               mistake=mistake,
                                               end=session['end'])

                    elif session['quiz_num'] == len(riddles) - 1:
                        # If it is correct, we add 1 to our score
                        print("right!")
                        # Add points to "score"
                        session['score'] += 1
                        # We don't want to be out of range, we don't =+ session
                        # session['quiz_num'] += 0
                        # We get the last question and its answer
                        coffee_question = get_coffee_questions(riddles, session['quiz_num'])
                        coffee_image = get_coffee_images(riddles, session['quiz_num'])
                        coffee_answer = get_coffee_answers(riddles, session['quiz_num']).lower()
                        print("Last question, we now go to game over page")
                        # PENDING - Get the Flash to work
                        flash("Correct!")
                        return redirect(url_for('gameover'))

                else:
                    print("wrong!")
                    print("coffee_guess: ", coffee_guess)
                    mistake = True
                    flash("Wrong!")
                    return render_template("quiz.html",
                                           username=session["username"],
                                           coffee_question=coffee_question,
                                           coffee_image=coffee_image,
                                           coffee_answer=coffee_answer,
                                           coffee_guess=coffee_guess,
                                           score=session["score"],
                                           session=session["quiz_num"],
                                           number_of_questions=number_of_questions,
                                           mistake=mistake,
                                           end=session['end'])

        # Trying to pass the answer and check if correct - END
            if request.form.keys()[0] == 'solution':
                coffee_guess = request.form['solution'].lower()
                mistake = False
                # We'll substract one point if 'paid' to see the solution
                # but we won't allow score to become negative
                if session['score'] > 0:
                    session['score'] -= 1
                else:
                    session['score'] += 0
                if coffee_guess == coffee_answer:
                    if session['quiz_num'] < len(riddles) - 1:
                        # If it is correct, we add 1 to our score
                        print("right!")
                        # Add points to "score"
                        session['score'] += 1
                        session['quiz_num'] += 1

                        # Now we need to get the next question and its answer,
                        # remember the session has increased by one
                        coffee_question = get_coffee_questions(riddles, session['quiz_num'])
                        coffee_image = get_coffee_images(riddles, session['quiz_num'])
                        coffee_answer = get_coffee_answers(riddles, session['quiz_num']).lower()

                        print("session['quiz_num'] is: ", session['quiz_num'])

                        # PENDING - Get the Flash to work
                        flash("Correct!")
                        return render_template("quiz.html",
                                               username=session["username"],
                                               coffee_question=coffee_question,
                                               coffee_image=coffee_image,
                                               coffee_answer=coffee_answer,
                                               coffee_guess=coffee_guess,
                                               score=session["score"],
                                               session=session["quiz_num"],
                                               number_of_questions=number_of_questions,
                                               mistake=mistake,
                                               end=session['end'])

                    elif session['quiz_num'] == len(riddles) - 1:
                        # If it is correct, we add 1 to our score
                        print("right!")
                        # Add points to "score"
                        session['score'] += 1
                        # We don't want to be out of range, we don't =+ session
                        # session['quiz_num'] += 0

                        # We get the last question and its answer
                        coffee_question = get_coffee_questions(riddles, session['quiz_num'])
                        coffee_image = get_coffee_images(riddles, session['quiz_num'])
                        coffee_answer = get_coffee_answers(riddles, session['quiz_num']).lower()
                        print("Last question, we now go to game over page")

                        # PENDING - Get the Flash to work
                        flash("Correct!")
                        return redirect(url_for('gameover'))

                else:
                    print("wrong!")
                    print("coffee_guess: ", coffee_guess)
                    mistake = True
                    flash("Wrong!")
                    return render_template("quiz.html",
                                           username=session["username"],
                                           coffee_question=coffee_question,
                                           coffee_image=coffee_image,
                                           coffee_answer=coffee_answer,
                                           coffee_guess=coffee_guess,
                                           score=session["score"],
                                           session=session["quiz_num"],
                                           number_of_questions=number_of_questions,
                                           mistake=mistake,
                                           end=session['end'])

# PENDING - Changes need to be made as the program runs when testing which is
# unwanted.


@app.route('/gameover')
def gameover():
    # No more points to "score"
    session['score'] += 0
    # Because we don't want to be out of range, we don't increment session
    # session['quiz_num'] += 0
    # Because that means the game has ended and we'll go to gameover.html,
    # we changed the session['end'] to True
    session['end'] = True
    add_top_score(session['username'], session['score'])
    top_players = get_top_players()
    return render_template("gameover.html",
                           username=session["username"],
                           score=session["score"],
                           top_players=top_players,
                           end=session['end'])


if __name__ == "__main__":
    # game_loop()
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
