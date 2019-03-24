var showValue = function(val){
    var str = document.getElementById("top_div_header").textContent;
    var res = str.slice(-8,-1)
    if (val<10){
        var text = "0"+val+"/"+res;
    }
    else{
        var text = val+"/"+res;
    }

    document.getElementById("date").value = text;

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
    date: text
  }
  fetch("http://127.0.0.1:8000/update/", {
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
    document.getElementById("status").value = data.status;
    document.getElementById("task1").value = data.task1;
    document.getElementById("task2").value = data.task2;
    document.getElementById("task3").value = data.task3;
  }).catch(function(ex) {
    console.log("parsing failed", ex);
  });
}
