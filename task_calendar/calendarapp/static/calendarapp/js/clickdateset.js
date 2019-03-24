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
    
}
