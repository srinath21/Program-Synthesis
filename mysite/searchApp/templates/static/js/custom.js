$(document).ready(function(){
  $('#Edit').toggleClass('hidden');
  $(".Python").toggleClass('hidden');
  $('.feedbackForm').toggleClass('hidden');
  $('#C').addClass('active');
  $('.edit').on('click',function() {
    $('#unEdit').toggleClass('hidden');
    $('#Edit').toggleClass('hidden');
    $('.edit').toggleClass('hidden');
  });
  $('#close').on('click', function(){
    $('#unEdit').toggleClass('hidden');
    $('#Edit').toggleClass('hidden');
    $('.edit').toggleClass('hidden');
  });
  $('.feedbackbtn').on('click', function(){
    $('.feedbackbtn').toggleClass('hidden');
    $('.feedbackForm').toggleClass('hidden');
  });
  $('#closeFeedback').on('click',function(){
    $('.feedbackbtn').toggleClass('hidden');
    $('.feedbackForm').toggleClass('hidden');
  });
  $("#loginButton").click(function(){
    $("#loginModal").modal('show');
  });
  $("#Python").click(function(){
    $(".C").addClass('hidden');
    $("#Python").addClass('active');
    $("#C").removeClass('active');
    $(".Python").removeClass('hidden');
  });
  $("#C").click(function(){
    $(".C").removeClass('hidden');
    $("#C").addClass('active');
    $("#Python").removeClass('active');
    $(".Python").addClass('hidden');
  });

});
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Chrome, Safari and Opera
    document.documentElement.scrollTop = 0; // For IE and Firefox
}
