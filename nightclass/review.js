/**
 * Created by dansbyt on 5/22/2017.
 */
'use strict';

$('getColor').click(function() {
    event.preventDefault();
    var color = $('#color').val();
    $('body').css('background-color', color);
    $('message').html(color);


});

//var input = prompt('Enter an item:');

$('#addToDo').click(function() {
    event.preventDefault();
    var input = prompt('enter an item');
    $('#items').append('<li>' + input + '</li>');
    });

