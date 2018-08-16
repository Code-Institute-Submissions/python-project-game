// <script>
// $(document).on('show.bs.modal','#exampleModal', function () {
//     alert('hi');
// });
//     $(document).ready(function() {
        
//         // $('#exampleModal').modal();
        
        
//         var input = $('#answer-button');
        
//         input.on('click', function(event) {
            
//             <!--// event.preventDefault();
            
//             console.log($('#exampleModal').html());
            
//             var guess = $('#answer').val();
//             console.log(guess)-->
//             var answer = '{{ coffee_answer }}';
//             console.log(answer)-->
            
//             if (guess != answer) {
//                 alert('Hola');
//                 <!--// event.preventDefault();
//           }
//         });
        
//     });
// </script>


/* to handle form posting on button click:

1. preventDefault() - prevent the form from being POSTed
2. Remove action="/quiz" from <form> element
3. Check whether mistake is true
    if true:
        Pop up modal
    else:
        POST to quiz function w/ javascript
        $.post({
            data: {
                'guess': what's in the form,
                'url': '/quiz'
            }
        }).done(function(data){
           Handle what to do when the results come back 
           score.innerHTML(score)
        });
*/