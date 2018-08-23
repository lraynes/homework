

// Create the tile layer that will be the background of our map
let satellitemap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.satellite",
  accessToken: API_KEY
});

let lightmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
});

let outdoormap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.outdoors",
  accessToken: API_KEY
});

// Create a baseMaps object to hold the lightmap layer
let baseMaps = {
  "Satellite": satellitemap,
  "Light Map": lightmap,
  "Outdoors": outdoormap
};

let myMap = L.map("map-id", {
  center: [33.82, -117.65],
  zoom: 4,
  layers: [satellitemap]
});

L.control.layers(baseMaps).addTo(myMap);



var url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

function chooseColor(magnitude) {
  if (magnitude < 1){
    return "green"
  } else if (magnitude >= 1 && magnitude < 2){
    return "yellow"
  } else if (magnitude >= 2 && magnitude < 3){
    return "blue"
  } else if (magnitude >= 3 && magnitude < 4){
    return "purple"
  } else if (magnitude >= 4 && magnitude < 5){
    return "teal"
  } else if (magnitude >= 5){
    return "red"
  } else {
    return "black"
  };
};

function chooseSize(magnitude) {
  if (magnitude < 1){
    return 5**6.5
  } else if (magnitude >= 1 && magnitude < 2){
    return 5.3**6.5
  } else if (magnitude >= 2 && magnitude < 3){
    return 5.9**6.5
  } else if (magnitude >= 3 && magnitude < 4){
    return 5.9**6.5
  } else if (magnitude >= 4 && magnitude < 5){
    return 6.2**6.5
  } else if (magnitude >= 5){
    return 7**6.5
  } else {
    return 0
  };
};


// function chooseSize(magnitude) {
//   if (magnitude < 2){
//     return 5**6.5
//   } else if (magnitude >= 2 && magnitude < 5){
//     return 5.6**6.5
//   } else if (magnitude >= 5 && magnitude < 7){
//     return 6.2**6.5
//   } else if (magnitude >= 7){
//     return 6.8**6.5
//   } else {
//     return 0
//   };
// };

d3.json(url, function(data){
  console.log(data.features)
  let earthquake = data.features

  for (let i = 0; i < earthquake.length; i++) {
    
    let coordinates = [earthquake[i].geometry.coordinates[1], earthquake[i].geometry.coordinates[0]]

    L.circle(coordinates, {
      fillOpacity: 1,
      color: "black",
      weight: .4,
      fillColor: chooseColor(earthquake[i].properties.mag),
      radius: chooseSize(earthquake[i].properties.mag)
    }).bindPopup("Magnitude " + earthquake[i].properties.mag + "<hr>" + earthquake[i].properties.place).addTo(myMap);
  }

  
})



