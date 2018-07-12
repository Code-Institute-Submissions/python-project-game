$( document ).ready(function() {
    console.log( "ready!" );
    $('#submit_answer').on('click', function() {
    preventDefault();
    var answer = $('#answer_input').val();
    var username = '{{ username }}';
    $.post({
    url: "/quiz",
    data: {
        username: username,
        answer: answer
    },
    success: function(data) {
        $('#answer_box').html(data);
    },
    traditional: true
    }).done();
});
});