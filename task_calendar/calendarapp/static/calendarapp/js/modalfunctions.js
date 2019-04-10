function addnewtask() {
  var x = document.getElementById("newtaskdiv");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

var addtask = function(obj){
  var date_req = document.getElementById("date").value
  var task1 = document.getElementById("task1").value
  var newtask = document.getElementById("newtask").value
  if(task1 == "None"){
    task1 = newtask;
  }
  if(task1 == ""){
    alert("Enter Valid Task")
  }
  else{
  var url = obj.getAttribute('data-url');
  var object = document.getElementById("tasks-panel")
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
    date: date_req,
    task1: task1
  }
  fetch(url, {
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
    var oldhtml = object.innerHTML;
    var html = `<div class="card" id="card${data.id}">
      <div class="card-body">
        ${data.task1}
        <button type="button" id="${data.id}" onclick="deletetask(this)" class="close" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
    </div>`;
    var html2 = oldhtml + html
    document.getElementById("task1").value = "None";
    object.innerHTML = html2;
  }).catch(function(ex) {
    console.log("parsing failed", ex);
    console.log(url)
  });
}
}

var deletetask = function(obj){
  var id = obj.getAttribute('id');
  var card_id = "card"+id;
  var object = document.getElementById(card_id)
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
    id: id
  }
  fetch('/delete/', {
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
    object.outerHTML = ""
  }).catch(function(ex) {
    console.log("parsing failed", ex);
    console.log(url)
  });
}
