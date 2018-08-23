

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
  center: [33.11, -41.84],
  zoom: 3,
  layers: [satellitemap]
});

L.control.layers(baseMaps).addTo(myMap);



var url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

function chooseColor(magnitude) {
  if (magnitude < 1){
    return "#00FF00"
  } else if (magnitude >= 1 && magnitude < 2){
    return "#65FF00"
  } else if (magnitude >= 2 && magnitude < 3){
    return "#CCFF00"
  } else if (magnitude >= 3 && magnitude < 4){
    return "#FFCC00"
  } else if (magnitude >= 4 && magnitude < 5){
    return "#FF6600"
  } else if (magnitude >= 5){
    return "#FF0000"
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
    return 6.2**6.5
  } else if (magnitude >= 4 && magnitude < 5){
    return 6.5**6.5
  } else if (magnitude >= 5){
    return 6.9**6.5
  } else {
    return 0
  };
};

let legend = L.control({position: 'bottomright'});

legend.onAdd = function (map) {
  let div = L.DomUtil.create('div', 'info legend'),
    grades = [0, 1, 2, 3, 4, 5],
    labels = [];

  // loop through our density intervals and generate a label with a colored square for each interval
  for (let i = 0; i < grades.length; i++) {
    div.innerHTML +=
      '<i style="background:' + chooseColor(grades[i] + 1) + '"></i> ' +
      grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
  }
  return div;
};

legend.addTo(myMap);

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



