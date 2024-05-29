const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");

signupBtn.onclick = (()=>{
  loginForm.style.marginLeft = "-50%";
  loginText.style.marginLeft = "-50%";
});
loginBtn.onclick = (()=>{
  loginForm.style.marginLeft = "0%";
  loginText.style.marginLeft = "0%";
});
signupLink.onclick = (()=>{
  signupBtn.click();
  return false;
});

// validate the forms
document.querySelector('#login-button').addEventListener('click', validateLoginForm);
document.querySelector('#sign-up-button').addEventListener('click', validateSignupForm);

function validateLoginForm() {
  var username = document.querySelector('#login-username').value,
      password = document.querySelector('#login-password').value

  if (!password || !username) {
    alert('Please enter the login form!');
    return;
  }

  // send request to get the user token if user has
  var request_obj = {
    url: "/auth/login-user",
    type: 'POST',
    data: {username, password}
  }
  $.ajax(request_obj).then((response) => {
    var data = JSON.parse(response);

    alert(data['message'])
    if (data['message'] == "user logged") {
        window.location.href = '/';
    }
  });
}


function validateSignupForm() {
  var username = document.querySelector('#sign-up-username').value,
      password = document.querySelector('#sign-up-password').value,
      passwordAgain = document.querySelector('#sign-up-again-password').value;

  if (password != passwordAgain) {
    alert('Please make sure that you entered the same password twice correctly');
    return;
  }

  var request_obj = {
    url: "/auth/create-user",
    type: 'POST',
    data: {username, password}
  }

  $.ajax(request_obj).then((response) => {
    var data = JSON.parse(response);
    alert(data['message']);

    if (data['message'] == "user created") {
        window.location.href = '/';
    }
  });
}
