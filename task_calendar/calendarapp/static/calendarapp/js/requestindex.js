function resetindex(){
    var date_text = document.getElementById("date").value;
    var status_text = document.getElementById("status").value;
    var task1_text = document.getElementById("task1").value;
    var task2_text = document.getElementById("task2").value;
    var task3_text = document.getElementById("task3").value;

    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) == (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
    }
  var myData = {
    date: date_text,
    status: status_text,
    task1: task1_text,
    task2: task2_text,
    task3: task3_text
  }
  fetch("http://127.0.0.1:8000/record/", {
    method: "post",
    credentials: "same-origin",
    headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Accept": "application/json",
        "Content-Type": "application/json"
    },
    body: JSON.stringify(myData)
  }).then(function(response) {
    return response.json();
  }).then(function(data) {
    console.log("Data is ok", data);
  }).catch(function(ex) {
    console.log("parsing failed", ex);
  });
}
