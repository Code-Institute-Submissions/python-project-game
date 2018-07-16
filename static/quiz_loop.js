$( document ).ready(function() {
    console.log( "ready!" );
//     $('#submit_answer').on('click', function() {
//     preventDefault();
//     var answer = $('#answer_input').val();
//     var username = '{{ username }}';
//     $.post({
//     url: "/quiz",
//     data: {
//         username: username,
//         answer: answer
//     },
//     success: function(data) {
//         $('#answer_box').html(data);
//     },
//     traditional: true
//     }).done();
// });

    // We need a function to cnage the CSS of the #discover-answer button when the 
    // answer is incorrect
    
    if (coffee_guess !== coffee_answer) {
        $("#discover-answer").css("visibility", "visible");
    }
    
});