/*
 * Custom scripts
 * --------------------------------------------------
 */

// document ready 
$(document).ready(function () {

	// method :: custom fonts for twitter timeline 
	window.setTimeout(function(){
		$(".twitter-timeline").contents().find(".timeline-Tweet-text").css("font-size","12");
		$(".twitter-timeline").contents().find(".timeline-Header-title").css("font-size","20");
	}, 2000);

	// method :: re-focus on load
	if(window.location.hash) {
		$("html, body").animate({scrollTop:$(window.location.hash).offset().top-50 }, 500);
	}

	// method :: toggle visibility of off-canvas panel	
	$('[data-toggle="offcanvas"]').click( function () {
		$('.row-offcanvas').toggleClass('active');
	});

	// method :: toggle visibility of navbar in small screens 
	$('.nav-item a').click( function(){

		if (!$(this).hasClass('dropdown-toggle')) {
			$('.navbar-collapse').removeClass('show');
		}

	});

	// method :: toggle focus on pull up button 
	$('.offcanvas-toggle-button').click( function(){
		$('.offcanvas-toggle-button:not(.caret)').toggleClass('toggle-focus');
	});

	// method :: custom animation for accordion click
	$('#accordionCFP .card-header').click( function(){

        offset = $('#accordionCFP .collapse.show').height();

        if ( $(this).offset().top < $('#accordionCFP .collapse.show').offset().top ) {
            offset = $('#accordionCFP .collapse.show').offset().top - $(this).offset().top;
        }

        $('html,body').animate({scrollTop: $(this).offset().top - offset - 60}, 'slow');

	});

	// method :: trigger CFP card header click
	$('.click-to-go').click( function(){
		// $($(this).attr('data-target')).click();

		// $('.collapse').each( function() {
		// 	$(this).removeClass('show');
		// });

		$($(this).attr('href')).click();
// event.preventDefault();
		// $($(this).attr('href')).collapse('show')

	});

	// method :: custom animation for icaps nav header 
	$('#icapsButton').click( function(){
		$('html,body').animate({scrollTop: $("body").offset().top}, 'slow');
	});

	// method :: re-focus on collapse of inverse nav bar 
	$('.close-bg').click( function(){
		$('html,body').animate({scrollTop: $("body").offset().top}, 'slow');
	});

	// method :: re-focus on pull over 
	$('.offcanvas-toggle-button').click( function(){
		$('html,body').animate({scrollTop: $("body").offset().top}, 'slow');
	});

	// method :: set default primary carousel speed 
	$('.carousel-primary').carousel({
		interval: 5000,
		pause: 'hover'
	});

	$('.carousel-primary').carousel(Math.floor(Math.random() * 6));

	$('.carousel-primary').on('slid.bs.carousel', function () {

		var curr = parseInt(($('.carousel-item.active').attr('href')));

		for (var i = 0; i<6; i++) {
		    $('#item-' + i.toString()).css('display', 'none');
		}
	    $('#rem-icaps-slide').remove();

		$('#item-' + curr.toString()).fadeIn( "slow", function() {
		    $('#item-' + curr.toString()).css('display', 'block');
		});

	})

	var state = 'play';

	$('#button_fbw').click( function(){
	    $('.carousel-primary').carousel(0);
	});

	$('#button_bw').click( function(){
	    $('.carousel-primary').carousel('prev');
	});

	$('#button_stop').click( function(){
	    $('.carousel-primary').carousel('next');
	});

	$('#button_ffw').click( function(){
	    $('.carousel-primary').carousel(5);
	});

	$('#button_play').click( function(){

	    if(state == 'stop'){

			state='play';
	    	$(this).html('<span class="oi oi-media-pause"></span>');
			$('.carousel-primary').carousel('cycle');
			$('.carousel-primary').carousel('next');

	    } else {

	    	state = 'stop';
	    	$(this).html('<span class="oi oi-media-play" style="color:#fb6346;"></span>');
			$('.carousel-primary').carousel('pause');

		}

	});

	$('.sidebar-offcanvas > .info-card').mouseenter(function(){
		// $('.carousel-primary').carousel('pause');
	});

	$('.sidebar-offcanvas > .info-card').mouseleave(function(){
		// $('.carousel-primary').carousel('cycle');
		// $('.carousel-primary').carousel('next');
	});

	// method :: pause or restart carousel 
	$('#toggle-carousel').click( function(){

		if($(this).is(':checked')) {
			$('.carousel-primary').carousel('cycle');
			$('.carousel-primary').carousel('next');
		} else {
			$('.carousel-primary').carousel('pause');
		}
	});

	// method :: set default secondary carousel speed 
	// $('.carousel-secondary').carousel({
	// 	interval: 3000
	// });

	// method :: scroll-spy on entire body, only anchor tags with class 'spy-enabled'
	$('a[class*="spy-enabled"]:not([href="#"])').click(function() {

		if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {

			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) +']');

			if (target.length) {

				$('html, body').animate({
					scrollTop: target.offset().top - 60
				}, 1000);
				
				return false;

			}

		}
	});

	// // method :: on badge click 

	// $('.badge-click').click( function() {
	// 	event.preventDefault();
	// 	location.href = $(this).attr('href');
	// });

	// // methods :: carousel logic

	// // on click on primary carousel entries

	// $( ".fade-to-black" ).click( function() {

	// 	// pause primary carousel
	// 	$('.carousel-primary').carousel('pause');

	// 	// activate highlights on primary carousel 
	// 	$('.active > a > img', '.carousel-primary').addClass('fade-to-black-primary-img');
	// 	$('.active > a > div > p', '.carousel-primary').addClass('fade-to-black-primary-p');

	// });

	// // on hover on primary carousel entries

	// $( "#carouselIndicators" ).hover( 

	// 	// mouse entry 
	// 	function() {

	// 		// check if primary carousel is currently frozen
	// 		var check_freeze = false;
	// 		check_freeze = $('.active > a > img', '.carousel-primary').hasClass('fade-to-black-primary-img');

	// 		// remove highlights on primary carousel, i.e. reset to default state 
	// 		$('.active > a > img', '.carousel-primary').removeClass('fade-to-black-primary-img');
	// 		$('.active > a > div > p', '.carousel-primary').removeClass('fade-to-black-primary-p');

	// 		// collapse entire accordion on mouse entry on primary carousel
	// 		$("a[aria-expanded='true']").click();

	// 		// resume primary carousel cycle on mouse entry
	// 		$('.carousel-primary').carousel('cycle');

	// 		// switch to next slide if current one was already frozen
	// 		if ( check_freeze ) {
	// 			$('.carousel-primary').carousel('next');
	// 		}

	// 	},

	// 	// mouse exit
	// 	function() {}

	// );

	// // on click on accordion card headers

	// $("a[class*='card-header'][data-toggle='collapse']").click( function() {

	// 	// remove freeze on current carousel
	// 	$('.active > a > img', '.carousel-primary').removeClass('fade-to-black-primary-img');
	// 	$('.active > a > div > p', '.carousel-primary').removeClass('fade-to-black-primary-p');

	// 	// switch to this slide on the primary carousel 
	// 	$('.carousel-primary').carousel(parseInt($(this).attr('id').match("collapse(.*)Control")[1]));

	// 	// pause primary carousel
	// 	$('.carousel-primary').carousel('pause');

	// 	// activate highlights on primary carousel 
	// 	$('a[href="#' + $(this).attr('id') + '"] > img', '.carousel-primary').addClass('fade-to-black-primary-img');
	// 	$('a[href="#' + $(this).attr('id') + '"] > div > p', '.carousel-primary').addClass('fade-to-black-primary-p');

	// 	// if clidked on card already open, causes accordion to collapse
	// 	// switch to default primary carousel then
	// 	if ( $(this).attr('aria-expanded') === 'true' ) {

	// 		// remove highlights on primary carousel, i.e. reset to default state 

	// 		$('.active > a > img', '.carousel-primary').removeClass('fade-to-black-primary-img');
	// 		$('.active > a > div > p', '.carousel-primary').removeClass('fade-to-black-primary-p');

	// 		// resume primary carousel cycle 

	// 		$('.carousel-primary').carousel('cycle');
	// 		$('.carousel-primary').carousel('next');

	// 	}


	// });

});

