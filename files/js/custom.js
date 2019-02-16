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
        $($(this).attr('href')).click();
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

    $('.carousel-primary').on('slid.bs.carousel', function (ev) {

        // make carousel lazy load

        var lazy = $(ev.relatedTarget).find("img[data-src]");

        lazy.attr("src", lazy.data('src'));
        lazy.removeAttr("data-src");

        // load data

        var curr = parseInt(($('.carousel-item.active').attr('href')));
        var num_entries = $('.carousel-item').length;

        for (var i = 0; i <= num_entries; i++) {
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
            $(this).html('<i class="fas fa-pause"></i>');
            $('.carousel-primary').carousel('cycle');
            $('.carousel-primary').carousel('next');

        } else {

            state = 'stop';
            $(this).html('<i class="fas fa-play" style="color:#fb6346;"></i>');
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
    //  interval: 3000
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

});

