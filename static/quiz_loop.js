$( document ).ready(function() {
    console.log( "ready!" );
    
    if (coffee_guess !== coffee_answer) {
        $("#discover-answer").css("visibility", "visible");
    }
    
});