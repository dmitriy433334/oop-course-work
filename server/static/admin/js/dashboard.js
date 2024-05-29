import 'https://code.jquery.com/jquery-3.6.0.min.js';

$('.delete_btn').on('click', function(e) {
  var user_id = e.target.getAttribute("userId");

  var request_obj = {
    url: '/auth/delete-user',
    type: 'DELETE',
    data: {user_id}
  }

  $.ajax(request_obj).then(() => {
    alert('User was successfully deleted');
    window.location.reload();
  });
  })