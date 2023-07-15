function getLotValue() {
  var uiLot = document.getElementsByName("uiLot");
  for(var i in uiLot) {
    if(uiLot[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getFloorsValue() {
  var uiFloors = document.getElementsByName("uiFloors");
  for(var i in uiFloors) {
    if(uiFloors[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getGaragesValue() {
  var uiGarages = document.getElementsByName("uiGarages");
  for(var i in uiGarages) {
    if(uiGarages[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getroomsValue() {
  var uirooms = document.getElementsByName("uirooms");
  for(var i in uirooms) {
    if(uirooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}



function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var Lot = document.getElementById("uiLot");
  var Bathrooms = document.getElementById("uiBathrooms");
  var Floors = document.getElementById("uiFloors");
  var Garages = document.getElementById("uiGarages");
  var rooms = document.getElementById("uirooms");
  var State = document.getElementById("uiState");
  var Type = document.getElementById("uiType");
  var estPrice = document.getElementById("uiEstimatedPrice");

  // var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      Lot: parseFloat(Lot.value),
      Bathrooms: parseFloat(Bathrooms.value),
      Floors: parseFloat(Floors.value),
      Garages: parseFloat(Garages.value),
      rooms: parseFloat(rooms.value),
      State: State.value,
      Type: Type.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  var url = "/api/get_State_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_State_names request");
      if(data) {
          var state = data.state;
          var uiState = document.getElementById("uiState");
          $('#uiState').empty();
          for(var i in state) {
              var opt = new Option(state[i]);
              $('#uiState').append(opt);
          }
      }
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  var url = "/api/get_Type_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_Type_names request");
      if(data) {
          var type = data.type;
          var uiType = document.getElementById("uiType");
          $('#uiType').empty();
          for(var i in type) {
              var opt = new Option(type[i]);
              $('#uiType').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
