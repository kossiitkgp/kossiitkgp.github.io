$( document ).ready(function() {

    var slidePosition=0;
    var numOfSlide = $("#slide-holder > div").size();

    $("#slide-holder").css("width",(numOfSlide*100)+"%");
    $(".slide").css("width",(100/numOfSlide)+"%");

    for (var a = 0; a < numOfSlide; a++) {
        $('#slide-nav').append(' <a href="javascript: void(0)" class="slide-nav-bt'+(a===0?' active':'')+'">  </a> ');
    }

    $('.slide-nav-bt').click(function() {
        moveSlide($(this));
        clearInterval(autoPlaySlideInter);
    });

    function moveSlide(thisa) {
        var thisindex = $('#slide-nav a').index(thisa);
        $('#slide-holder').css("margin-left", '-'+thisindex +'00%');
        $('#slide-nav a').removeClass('active');
        thisa.addClass('active');
    }

    function autoPlaySlide() {
        slidePosition++;
        if (slidePosition == numOfSlide) { slidePosition = 0; }
        moveSlide($("#slide-nav").children(".slide-nav-bt:eq("+slidePosition+")"));
    }

    var autoPlaySlideInter = setInterval(autoPlaySlide,3000);
});
