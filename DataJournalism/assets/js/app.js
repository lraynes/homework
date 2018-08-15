let svgWidth = 960;
let svgHeight = 500;

let margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

let width = svgWidth - margin.left - margin.right;
let height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
let svg = d3.select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

let chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import Data
d3.csv("assets/data/data.csv", function(err, healthData) {

  // Step 1: Parse Data/Cast as numbers
  // =====================================================
  healthData.forEach(function(data) {
    data.poverty = +data.poverty;
    data.healthcare = +data.healthcare;
    data.income = +data.income;
    data.obesity = +data.obesity;
    data.age = +data.age;
    data.smokes = +data.smokes;
  });
  
  xList = [d.poverty, d.income, d.age]
  yList = [d.healthcare, d.obesity, d.smokes]

  // Step 2: Create scale functions
  // ======================================================
  let xLinearScale = d3.scaleLinear()
    .domain(d3.extent(healthData, d => xList[0]))
    .range([0, width]);

  let yLinearScale = d3.scaleLinear()
    .domain([0, d3.max(healthData, d => yList[0])])
    .range([height, 0]);
  
    // Step 3: Create axis functions
  // =====================================================
  let xAxis = d3.axisBottom(xLinearScale);
  let yAxis = d3.axisLeft(yLinearScale);
  
  // Step 4: Append Axes to the chart
  // ==============================
  chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(xAxis);

  chartGroup.append("g")
    .call(yAxis);
  
  // Step 5: Create Circles
  // ==============================
  let points = chartGroup.selectAll("circle")
    .data(healthData)
    .enter()
  
  points.append("circle")
    .attr("cx", d => xLinearScale(xList[0]))
    .attr("cy", d => yLinearScale(yList[0]))
    .attr("r", "15") 
    .attr("class", "stateCircle")
    .attr("opacity", .9);
    
  points.append("text")
    .attr("x", d => xLinearScale(xList[0]))
    .attr("y", d => yLinearScale(yList[0]) + 15/2)
    .attr("class", "stateText")
    .text(d => d.abbr)

  // Create axes labels
  chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left + 40)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("class", "aText")
    .text("Poverty %");

  chartGroup.append("text")
    .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
    .attr("class", "aText")
    .text("Lacks Healthcare %");
  
  // Add state abbreviation
  // chartGroup.selectAll("text")
  //   .data(healthData)
  //   .enter()
  //   .append("text")
  //   .attr("x", d => xLinearScale(d.poverty))
  //   .attr("y", d => yLinearScale(d.healthcare))
  //   .text(d => d.abbr)
    
    // .attr("class", "stateText")
});
