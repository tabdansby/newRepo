/**
 * Created by dansbyt on 5/15/2017.
 */

'use strict';

var names = ['Chris', 'Katie', 'Chelsea'];

var greet = function (n) {
    var color;
    if (n === 'Chris') {
        color = '#3723e0'

    } else if (n === 'Katie') {
        color = '#E0200D'
    } else {
        color = "#24e016"
    }
    var message = document.getElementById('message');
    message.innerHTML = "hello " + n + '!';
    message.style.color = color;
}

document.getElementById('getName').addEventListener('click', function() {
    var name = document.getElementById('name').value;
    greet(name);
});