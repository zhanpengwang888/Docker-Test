$(".play-button").on("click", function () {
    var audio = new Audio($(this).attr('data-url'));
    if ($(this).hasClass('playing')) {
        $(this).removeClass('playing');
        audio.pause();
    } else {
        $(this).addClass('playing');
        audio.play();
    }
    var thisButton = $(this);
    audio.onended = function () {
        thisButton.removeClass('playing');
    };
});
