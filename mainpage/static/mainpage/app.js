$(document).ready(function(){
	$('#loginBtn').click(function(){
		$('#loginModal').modal();
	});

 	$('#loginSubmit').submit(function(){
 		/* should shoot an ajax post request to server with email and password*/
 		window.alert('Sorry, login functionality is under construction');
 		console.log('you clikc it');
 		return false;
 	});


 	$('#side-menu-collapse').click(function(){
 		$('.csa-side-menu').toggleClass('active');
 	});

 	$('.body.click').click(function(event){
 		if ($('.csa-side-menu').hasClass('active')){
 			 var x = event.pageX;
 			 var width = document.documentElement.clientWidth;
 			 if (x < width - 275){
 			 	$('.csa-side-menu').toggleClass('active');
 			 }
 		}

 	});
});