'use strict';

$('#animateButton').click(function() {
    $('#animate').effect("bounce", {times:50}, "slow");});
    /*({
        opacity: 0.25,
        left: "+=50",
        height: "toggle"

}, 5000, function () {
    console.log('Done')
    });
});
*/


/*

document.getElementById('animateButton').addEventListener('click', function () {
    var icon = document.getElementById('animate');
    var id = setInterval(frame, 5);
    var pos = 0;

    function frame() {
        if (pos == 100) {
            icon.style.left = '';
            clearInterval(id);
        } else {
            pos++;
            console.log(pos);
            if (pos % 2 === 0) {
                icon.style.left = '50px';
            } else {
                icon.style.left = '0';
            }
        }
    }
    });*/
