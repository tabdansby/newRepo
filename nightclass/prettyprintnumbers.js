/**
 * Created by dansbyt on 5/16/2017.
 */

'use strict';
function reverseString(str){
    //Step 1 Use the split() method to return a new array
    var splitString = str.split(""); // var splitString = "hello".split
    //["h", "e", "l", "l", "o"]
    //Step 2. Use the reverse() method to reverse the new created array
    var reverseArray = splitString.reverse(); //var reverseArray = [olleh]
    //["o", "l", "l", "e", "h"]
    //Step 3. Use the join() method to join all elements og the array
    var joinArray = reverseArray.join(""); //
    //Step 4: Return the reversed string
    return joinArray;//"olleh"
}


document.getElementById('getNumber'.addEventListener('click', function() {
    var number = document.getElementById('number').value;
    var numberReversed = reverseString(number);
    var threeNumberArray = [];

    for (var i = 0; i < numberReversed.length; i+=3) {
        var threeNumber = '';

        if (numberReversed[i] !== undefined) {
            threeNumber += numberReversed[i];
        }
        if (numberReversed[i] !== undefined) {
            threeNumber += numberReversed[i+1];
        }

        if (numberReversed[i+2] !== undefined) {
            threeNumber += numberReversed[i+2];
        }

        threeNumberArray.push(threeNumber);

    }
    var threeNumberArrayJoined = threeNumberArray.join(',';)

//    var number = document.getElementById('getNumber').value;
//    var stringToNumber = parseInt(number);
//    var numberComma = parseInt(number).toLocaleString();
   document.getElementById('message').innerHTML = numberComma
})