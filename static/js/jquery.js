$(document).ready(function(){
	$('.preloader').delay(2300).fadeOut(1000);
	$("a").on('click', function(event) {
    	if (this.hash !== "") {
      		event.preventDefault();
     	 	var hash = this.hash;
      		$('html, body').animate({
        		scrollTop: $(hash).offset().top
      		}, 1500, function(){
           		window.location.hash = hash;
      		});
    	}
  	});    
})
