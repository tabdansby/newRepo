// $(document).ready(function() {
// 	$('.toggle, .toggle2, .toggle3, .toggle4').hide();
// });
//
// 	$(document).ready(function() {
// 		$('.click1').click(function() {
//
// 			$('.toggle').toggle(250);
// 		});
// 	});
//
// 	$(document).ready(function() {
// 		$('.click2').click(function() {
//
// 			$('.toggle2').toggle(250);
// 		});
// 	});
//
// 	$(document).ready(function() {
// 		$('.click3').click(function() {
//
// 			$('.toggle3').toggle(250);
// 		});
// 	});
//
// 	$(document).ready(function() {
// 		$('.click4').click(function() {
//
// 			$('.toggle4').toggle(250);
// 		});
// 	});
//
// function display_random_image()
// {
//      var theImages = [{
//         src: "http://farm4.staticflickr.com/3691/11268502654_f28f05966c_m.jpg",
//         width: "240",
//         height: "160"
//     }, {
//         src: "http://farm1.staticflickr.com/33/45336904_1aef569b30_n.jpg",
//         width: "320",
//         height: "195"
//     }, {
//         src: "http://farm6.staticflickr.com/5211/5384592886_80a512e2c9.jpg",
//         width: "500",
//         height: "343"
//     }];
//
//     var preBuffer = [];
//     for (var i = 0, j = theImages.length; i < j; i++) {
//         preBuffer[i] = new Image();
//         preBuffer[i].src = theImages[i].src;
//         preBuffer[i].width = theImages[i].width;
//         preBuffer[i].height = theImages[i].height;
//     }
//
// create random image number
//   function getRandomInt(min,max)
//     {
//       //  return Math.floor(Math.random() * (max - min + 1)) + min;
//
// imn = Math.floor(Math.random() * (max - min + 1)) + min;
//     return preBuffer[imn];
//     }
//
// // 0 is first image,   preBuffer.length - 1) is  last image
//
// var newImage = getRandomInt(0, preBuffer.length - 1);
//
// // remove the previous images
// var images = document.getElementsByTagName('img');
// var l = images.length;
// for (var p = 0; p < l; p++) {
//     images[0].parentNode.removeChild(images[0]);
// }
// // display the image
// document.body.appendChild(newImage);
// }

$(document).ready(function(){
	$(".toggler").click(function() {
        $(this).find("img").toggle(this);
        console.log(this)
    });
//setInterval(function(){ alert("Hello"); }, 1000);
	$(".toggler").click(function() {

     // Reset images//
    $('.toggler img.alt').hide();
    $(".toggler img.orig").show();

    //toggle the images in this .toggler
		setInterval.click(function(){ $("img", this).toggle("img"); }, 1000);

})});

// $(document).ready(function() {
// $(".toggler").click(function() {
//
//     // Reset images//
//     $('.toggler img.alt').hide();
//     $(".toggler img.orig").show();
//
//     // toggle the images in this .toggler
//     $("img", this).toggle("img");
// })
// })});