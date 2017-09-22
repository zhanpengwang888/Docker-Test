$(document).ready(function() {
  stretchArrow();
});

$(window).resize(function(){
  stretchArrow();
});

function stretchArrow(){
  _width = Math.floor($(window).width() / 2);

  $('.footer-arrow').css('border-width', '0 ' + _width + 'px 100px ' + _width + 'px');
}