$(document).ready(function(){
	$('#loginBtn').click(function(){
		$('#loginModal').modal();
	});

 	$('#loginSubmit').submit(function(){
 		/* should shoot an ajax post request to server with email and password*/
 		window.alert('Sorry, login functionality is under construction');
 		console.log('you clikc it');
 		return false;
 	})





});