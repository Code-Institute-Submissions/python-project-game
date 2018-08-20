import os
import json
from flask import Flask, render_template, request, redirect, session, url_for

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
    """
    This function creates a list with the username and score of players, then
    it appends it to out .txt file and sorts it in reverse order, returning
    the first five players
    """
    with open('data/top_scores.txt', 'r') as top_scores:
        top_players = []
        for line in top_scores.readlines()[1:]:
            top_players.append(line)

        sorted_top_players = []
        for player in top_players:
            tupe = (player.split(':')[0].strip(), int(player.split(':')[1].strip()))
            sorted_top_players.append(tupe)

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

    """
    This function contains the logic of our quiz
    """

    # Calling question, images and answer functions - START
    coffee_question = get_coffee_questions(riddles, session['quiz_num'])
    coffee_image = get_coffee_images(riddles, session['quiz_num'])
    coffee_answer = get_coffee_answers(riddles, session['quiz_num']).lower()
    # Calling question, images and answer functions - END

    # We get the number of riddles in our quiz (to recognise the last question)
    number_of_questions = len(riddles)

    # If the session is over, to avoid cheating by coming back to the quiz we'll
    # redirect to the gameover page
    if session['end']:
        top_players = get_top_players()
        return render_template("gameover.html",
                               username=session["username"],
                               score=session["score"],
                               top_players=top_players)

    if request.method == "GET":
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
            flag = list(request.form.keys())
            if flag[0] == 'answer':
                coffee_guess = request.form['answer'].lower()
                mistake = False
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
                        # We get the last question and its answer
                        coffee_question = get_coffee_questions(riddles, session['quiz_num'])
                        coffee_image = get_coffee_images(riddles, session['quiz_num'])
                        coffee_answer = get_coffee_answers(riddles, session['quiz_num']).lower()
                        return redirect(url_for('gameover'))
                
                else:
                    print("wrong!")
                    mistake = True
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
        
            flag = list(request.form.keys())
            if flag[0] == 'solution':
                print('The request was solution')
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
                        return redirect(url_for('gameover'))

                else:
                    print("wrong!")
                    mistake = True
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


@app.route('/gameover')
def gameover():
    # No more points to "score"
    session['score'] += 0
    # We changed the session['end'] to True
    session['end'] = True
    add_top_score(session['username'], session['score'])
    top_players = get_top_players()
    return render_template("gameover.html",
                           username=session["username"],
                           score=session["score"],
                           top_players=top_players,
                           end=session['end'])


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
