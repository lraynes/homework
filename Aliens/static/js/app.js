// from data.js
var tableData = data;

var tbody = d3.select("tbody");

data.forEach((ufoSightings) => {
	// Create new row
	let row = tbody.append("tr");
	
	// Add key: value pairs to row
	Object.entries(ufoSightings).forEach(([key, value]) => {
    let cell = tbody.append("td");
		cell.text(value);
	});
	
});

var submit = d3.select("#filter-btn");

submit.on("click", () => {

  // Prevent the page from refreshing
  d3.event.preventDefault();
	console.log("in here");
	
	// Select the input element and get the raw HTML node
  let inputElement = d3.select("#datetime");
	console.log(inputElement);

  // Get the value property of the input element
  let inputValue = inputElement.property("value");
  console.log(inputValue);

	let filter = tableData.filter(encounter => encounter.datetime === inputValue);
	console.log(filter);

	tbody.html("");

	filter.forEach(ufoSightings => {
		// Create new row
		let row = tbody.append("tr");
		
		// Add key: value pairs to row
		Object.entries(ufoSightings).forEach(([key, value]) => {
			tbody.append("td").text(value);
		});

	});

});