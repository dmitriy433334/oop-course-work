var supported_file_types = ['application/pdf'];
var realUploadBtn = document.querySelector("#real-file");
var customText = document.querySelector("#custom-text");
var process_button = document.querySelector("#process_button");
var logOutBtn = document.querySelector("#log-out-btn");

$("#custom-button").on("click", (e) => {
    realUploadBtn.click();
})

$.ajax({
    url: "/auth/is-authorized",
    method: "POST",
}).then((res) => {
    let data = JSON.parse(res);
    if (data.isAuthorized) {
        document.querySelector('#myTopnav > div.navlinks > div:nth-child(3) > a').style.display = 'none';
    }else{
        document.querySelector('#log-out').style.display = 'none';
    }
});


realUploadBtn.addEventListener('change', function () {
  if (realUploadBtn.files) customText.innerHTML = 'File has been chosen';
  else customText.innerHTML = 'No file chosen, yet.';
});

process_button.addEventListener("click", () => {
   if (realUploadBtn.files.length < 1) {
     alert("there isn't a file selected");
     return;
   }

   const formData = new FormData();
   formData.append("file", realUploadBtn.files[0]);

   $.ajax({
     url: "/files/create-file",
     data: formData,
     method: "POST",
     processData: false,
     contentType: false
   }).then((res) => {
       res = JSON.parse(res);
       alert(res['message']);
       if ("file_src" in res) {
        window.location.href = `/files/${res.file_src}`;
       }
   })
});

logOutBtn.addEventListener("click", () => {
    $.ajax({
        url: "/auth/logout",
        method: "POST",
    }).then(() => window.location.reload())
})