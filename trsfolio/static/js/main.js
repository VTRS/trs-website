$(document).ready(function() {
  checkform()
  var csrftoken = $.cookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
});

// Modal 
$(function () {
  
    $('.md-trigger').on('click', function() {
      $('.md-modal').addClass('md-show');
    });
    
    $('.md-close').on('click', function() {
      $('.md-modal').removeClass('md-show');
    });
    
});

// Send contact form
function contact() {
  var url = document.getElementById("url").value;;
  var name = document.getElementById("name").value;
  var contact = document.getElementById("contact").value;
  var message = document.getElementById("message").value;
  $.post(url, {
      name: name,
      contact: contact,
      message: message,
    })
    .done(function(data) {
      $('#formContainter').html(
        '<div class="success-nessage">' + data + '</div>'
      );
    });

  return false;
}

function checkform(){
    var f = document.forms["contactForm"].elements;
    var cansubmit = true;

    for (var i = 0; i < f.length; i++) {
        if (f[i].value.length == 0) cansubmit = false;
    }

    if (cansubmit) {
        document.getElementById('send-form').style.visibility = 'visible';
    }
    else {
        document.getElementById('send-form').style.visibility = 'hidden';
    }
}

$('.invert').hover(mouseEnter, mouseLeave);
  function mouseEnter() {
      // find the image inside the div
      var img = this.querySelector('img');
      img.classList.add('invert_image');
  };
  function mouseLeave() {
        // find the image inside the div
      var img = this.querySelector('img');
      img.classList.remove('invert_image');  
  };

  $('.invert').click(function() {
    var img = this.querySelector('img');
    img.classList.toggle('invert_image');
  });
  