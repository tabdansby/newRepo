/**
 * Created by dansbyt on 5/22/2017.
 */
$('#addToDo').click(function () {
    event.preventDefault();
    $('#toDoInput').toggle('slow');

});

$('#enter').click(function() {
    event.preventDefault();
    var item = $('#toDoInput').val();
    var html = '<tr><td class="row1">' + item.val() + '<tr><td class="row2">Done</td></tr>'
    $('#toDoList'.append(html);
    item.val('');
    $('#toDoInput').toggle('slow');




    }




)