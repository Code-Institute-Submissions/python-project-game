# Your Project's Name

The Big Coffee Quiz

An easy to use app with questions about coffee, ideal to test and improve the 
level of knowledge of baristas and employees required to make coffee 
with professional quality.
 
## UX
#### Scope
Scope 1 - Twelve selected coffee related questions. At this point, the project
will be able to get username and tell you your score as well as the highest scores.
The questions combine text-based and pictorial questions.

Scope 2 - Twenty one questions. Users can save their progress and come back to the
quiz later. The can also share their results on social media.

#### Mockup
See the at **/assets/images/mockup-the-big-coffee-quiz.pdf**

## Features
As requested in the project's brief:
A form that takes the user's USERNAME and takes them to the starting point of the quiz - Build a web application game that asks players to guess the answer to a pictorial or text-based riddle.

A quiz.html page that refreshes itself after each question, so the user can progress to the next
and keeps track of the scoring - The player is presented with an image or text that contains the riddle. 
Players enter their answer into a textarea and submit their answer using a form.

It recognises whether a question was answered correctly and if so, they are redirected to the next riddle.
Otherwise,the incorrect guess is stored and printed below the riddle. 

More than one user can play the same instance of the game at the same time.
 

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [StartBootstrap](https://startbootstrap.com/)
    - The project uses a **StartBootstrap** template for consistency or design and UX.

- [Font Awesome](https://fontawesome.com/)
    - The project uses **Font Awesome** for better design and styling.
    
- [Flask](http://flask.pocoo.org/)
    - The project uses **Flask** to bring the backend and frontend together 

## Testing

Manual testing included numerous uses of the print() method to confirm that the 
correct question/answer/image was being passed to the page.
The program was also tested and adjusted as new functionalities were added.

Examples of user stories I aimed to comply with follow:

##### As a < coffee lover >, I want < to find out more about coffee > so that < I can understand it better >.
The level of dificulty and nature of the questions is very varied. from general to professional.

##### As a < barista in training >, I want < to keep track of my progress and compare with my coworkers > so that < I can improve with time >.
Users high scores are stored and the top 5 players are displayed at the end of the game. The whole list
is stored in a .txt file that shows all the different scoring from different users.

##### As a < person taking the quiz >, I want < to be able to see the solution > so that < I don't get stuck in a question I don't know the answer to >.
After every failed question, a button with the opportunity to see the solution will appear.
It will clearly state that no points will be awarded if you look at the solution, so use it wisely!

Another way this project was tested was by acting like a user and moving around
the quiz. Below, some of the activities underwent:

- Introducing a username: The app's homepage clearly has a space to input your username and start the quiz.
- Answering a question incorrectly: Once the quiz begins, I answered questions incorrectly, expecting to
see a message with the wrong guess appear, along with the button allowing you to see the solution.
- Answering a question correctly after a failed attempt but without looking at the solution: This lead
to the normal success response, the score was incremented by 1 point and we moved to the next question.
- Answering a question correctly after a failed attempt and after looking at the solution: This lead
to the progression to the next question, but no points were added to the score.
- Answering a question incorrectly after a failed attempt: this lead to the same scenario as the first time
and that didn't changed until the qustion was answered correctly.
- Answering a question correctly the first time: This lead to the score being incremented by 1 and we
moved to the next question.


##### Different screen sizes:

- The quiz is responsive and works best on a large to medium screen, horizontally displayed.
- On smaller screens, it works well enough, but there is a small amount of scrolling.
- The look and feel remains the same in different sizes, trying to evoke the theme, which is coffee.
- In very small screens, elements that are displayed horizontally (such as top scores), change to vertical, for ease of read.

##### Bugs and Issues
- At an early stage, there was an issue getting the quiz to recognise the most recent guess.</br> 
It was taking the one before it instead. By fixing the order in which the functions were called, this was eventually sorted.
- Cheating at the end: After testing, it was clear that a user could finish the game and go back to the</br>
last question of the quiz to harvest points. This was solved by adding the boolean session['end'] that redirected attempts</br>
to go back to the quiz to the gameover page once the session had ended.
- Cheating the button: As it was originally written, a user that clicked the button for a clue would get zero</br>
point for answering the question. However, users could see the clue, answer incorrectly for zero points</br>
and then answer correctly on a fresh question (same question!), therefore seeing the solution with no penalty.</by>
This was fixed by giving a cost of one point off your score if you click to see the solution.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits
The approach and structure of the functionality to get and render the high scores was 
adapted from code shared with me by my mentor [git repo here](https://github.com/ckz8780/ci-pp-milestone-riddlemethis/blob/master/run.py).</br>
While the names and details are different, and we work to write them together, </br>
it's worth noting that the code was used as a guide after several attempts to </br>
different, failed approaches.</br>
I also received help via slack through the practical-python chat.</br>
User Andrew Carton suggested a way to redirect users once the session is over, to prevent cheating by hitting back after the game is over.


### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
Background image: [pixabay.com](https://pixabay.com/en/coffee-coffee-beans-drink-caffeine-1324126/)

### Acknowledgements
Code Institute Tutors Nakita and Niel
Mentor Chris Zielinski
Code Insitute Alumni Andres Correa


#### Material to go back to
[tutor example](https://github.com/ckz8780/ci-pp-milestone-riddlemethis)
[7 wonders example](http://radiusofcircle.blogspot.com/2016/03/making-quiz-website-with-python.html)
[flask quiz example](https://github.com/vgel/simple-quiz)