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

Manual testing included numerous uses of the print() methos to confirm that the 
correct question/answer/image was being passed to the page.
The program was also tested and adjusted as new functionalities were added.

For any scenarios that have not been automated, test the user stories manually 
and provide as much detail as is relevant. 
A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

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