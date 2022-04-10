// scroll handler
$(window).scroll(function () {
  let scroll = $(window).scrollTop();

  document.getElementById("myContent").style.marginTop =
    -100 - 0.2 * scroll + "px";

  if (scroll >= 300) {
    $("#myNav").addClass("bg-dark");
  } else {
    $("#myNav").removeClass("bg-dark");
  }
});
