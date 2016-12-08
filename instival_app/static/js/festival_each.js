tabSlide();

$('.nav-tabs li').on('shown.bs.tab', function() {
  $('#magic-line').remove();
  tabSlide();
});

function tabSlide() {
  $("#example-one").append("<li id='magic-line'></li>");
  var $magicLine = $("#magic-line");
  $magicLine
    .width($(".active").width())
    .css("left", $(".active a").position().left)
    .data("origLeft", $magicLine.position().left)
    .data("origWidth", $magicLine.width());
  $("#example-one li").find("a").hover(function() {
    $el = $(this);
    leftPos = $el.position().left;
    newWidth = $el.parent().width();
    $magicLine.stop().animate({
      left: leftPos,
      width: newWidth
    });
  }, function() {
    $magicLine.stop().animate({
      left: $magicLine.data("origLeft"),
      width: $magicLine.data("origWidth")
    });
  });

}