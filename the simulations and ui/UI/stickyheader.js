//JS to fix header on scroll
window.onscroll = function() {myFunction()};

var header = document.getElementById("canstick");

var headerY = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > headerY) {
    header.classList.add("stick");
  } else {
    header.classList.remove("stick");
  }
}