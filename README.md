### Description
##### CREATE A 'RIDDLE-ME-THIS' GUESSING GAME
Build a web application game that asks players to guess the answer to a pictorial or text-based riddle.
The player is presented with an image or text that contains the riddle. Players enter their answer into a textarea and submit their answer using a form.
If a player guesses correctly, they are redirected to the next riddle.
If a player guesses incorrectly, their incorrect guess is stored and printed below the riddle. The textarea is cleared so they can guess again.
Multiple players can play an instance of the game at the same time. Users are identified by a unique username.
Create a leaderboard that ranks top scores for all users.

#### Scope
Scope 1 is simple and maps to the project brief and guidelines - this will be the project you submit for assessment so you can get certified
Scope 2 might include additional features that are 'cool-to-have' but not essential. 

#### Mockup
See the at **/assets/images/mockup-the-big-coffee-quiz.pdf**

#### Testing


#### Instructions for deployment


#### Bugs and/or issues


#### Sources
Background image: [pixabay.com](https://pixabay.com/en/coffee-coffee-beans-drink-caffeine-1324126/)

#### Material to go back to
[tutor example](https://github.com/ckz8780/ci-pp-milestone-riddlemethis)
[7 wonders example](http://radiusofcircle.blogspot.com/2016/03/making-quiz-website-with-python.html)
[flask quiz example](https://github.com/vgel/simple-quiz)

[Example of AJAX use](https://stackoverflow.com/questions/40963401/flask-dynamic-data-update-without-reload-page)
Answer by **furas** - you can copy and search for the whole example:
$.ajax({
      url: "/suggestions",
      type: "get",
      data: {jsdata: text},
      success: function(response) {
        $("#place_for_suggestions").html(response);
      },
      error: function(xhr) {
        //Do Something to handle error
      }
    });