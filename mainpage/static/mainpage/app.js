$(document).ready(function(){
	$('#loginBtn').click(function(){
		$('#loginModal').modal();
	});

 	$('#loginSubmit').submit(function(){
 		/* should shoot an ajax post request to server with email and password*/
 		window.alert('Sorry, login functionality is under construction');
 		console.log('you click it');
 		return false;
 	});


 	$('#csa-side-menu-button').click(function(){
 		$('.base-container').toggleClass('active');
 	});

 	$('body').click(function(e){
 		if ($('.base-container').hasClass('active')){
 			 var x = e.pageX;
 			 var width = document.documentElement.clientWidth;
 			 if (x < width - 275){
 			 	$('.base-container').toggleClass('active');
 			 }
 		}

 	});
});