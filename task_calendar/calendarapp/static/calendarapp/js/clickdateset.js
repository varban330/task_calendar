var showValue = function(val,obj){
    var str = document.getElementById("top_div_header").textContent;
    var object = document.getElementById("tasks-panel")
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
  var url = obj.getAttribute('data-url');
  var myData = {
    date: text
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
    document.getElementById("status").value = data.status;
    var old_html = object.innerHTML
    var task_array = data.tasks
    var i;
    for (i = 0; i < task_array.length; i++) {
      old_html += `<div class="card" id="card${task_array[i][0]}">
        <div class="card-body">
          ${task_array[i][1]}
          <button type="button" id="${task_array[i][0]}" onclick="deletetask(this)" class="close" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
      </div>`;
    }
    object.innerHTML = old_html;
  }).catch(function(ex) {
    console.log("parsing failed", ex);
  });
}
