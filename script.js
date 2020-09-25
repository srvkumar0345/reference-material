function calculate_forex() {
    var xhttp = new XMLHttpRequest();
  
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = JSON.parse(this.responseText);
            exchange_rate_obj = response.rates
            value_date = response.date
            amt = Number(document.getElementById("amt").value)
            for (rate in exchange_rate_obj) {
              document.getElementById("result").value = Number(exchange_rate_obj[rate])*amt
            }
            document.getElementById("date_placeholder").innerHTML = "<small><em>*As of " + value_date + "</em></small>"
                       
    }
  }
    base=document.getElementById("curr1").value;
    symbols=document.getElementById("curr2").value;
    
    url='https://29s2zacvy8.execute-api.us-west-2.amazonaws.com/latest?'+'base='+base+"&"+'symbols='+symbols;
    console.log(url)
    xhttp.open("GET",url, true);
    xhttp.send();
    }