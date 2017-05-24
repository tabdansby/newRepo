$('#addToDo').click(function () {
    event.preventDefault();
    $('#toDoInput').toggle('slow');
});

$('#enter').click(function () {
    event.preventDefault();
    var count = $('#toDoList tr').length;
    var item = $('#toDoInputText');
    var html = '<tr><td class="row0">' + count + '</td><td id="td_' + count + '"class="row1">' + item.val() + '</td><td id="done_' + count + '" class="row2"><a onclick="done(this)" href="#" id="done_' + count + '">Done</a></td></tr>';
    $('#toDoList').append(html);
    item.val('');
    $('#toDoInput').toggle('slow');

});
function done(el) {
    event.preventDefault();
    var id = el.id.replace ( /[^\d.]/g, '' );
    var itemId = '#td_' + id;
    $(itemId).css('text-decoration', 'line-through');
    //console.log(itemId);


}





//$('.input')