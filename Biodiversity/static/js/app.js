function buildMetadata(sample) {
  
  // @TODO: Complete the following function that builds the metadata panel
  let url = "/metadata/" + sample;
  
  // Use `d3.json` to fetch the metadata for a sample
  d3.json(url).then(response => {

    // Use d3 to select the panel with id of `#sample-metadata`
    let panel = d3.select("#sample-metadata");

    // Use `.html("") to clear any existing metadata
    panel.html("");

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new tags for each key-value in the metadata. 
    Object.entries(response).forEach(function([key, value]) {
      panel.append("div").text(key + ": " + value);
    })
    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
  
  })
  
    
}

function buildCharts(sample) {
  let url = "/samples/" + sample; 

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json(url).then(response => {
    console.log(response.otu_ids)
    console.log(response)

    let colors = []

    for (let k = 0; k < response.otu_ids.length; k++) {
      if (response.otu_ids[k] <= 500) {
        colors.push("002DEB")
      } else if (response.otu_ids[k] <= 1000) {
        colors.push("006EE2")
      } else if (response.otu_ids[k] <= 1500) {
        colors.push("00AAD9")
      } else if (response.otu_ids[k] <= 2000) {
        colors.push("00D0BF")
      } else if (response.otu_ids[k] <= 2500) {
        colors.push("00C77C")
      } else {
        colors.push("00BF3D")
      }
    }

    console.log(colors)
    // @TODO: Build a Bubble Chart using the sample data
    
    let trace1 = {
      x: response["otu_ids"],
      y: response["sample_values"],
      mode: 'markers',
      text: response["otu_labels"],
      marker: {
        size: response["sample_values"],
        color: colors
      }
    };
    
    let data1 = [trace1];
    
    let layout1 = {
      showlegend: false,
      xaxis: { title: "OTU ID"}
    };
    
    Plotly.newPlot('bubble', data1, layout1);



















    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values, otu_ids, and labels (10 each).
    let samples = []
    for (let i = 0; i < response.sample_values.length; i++) 
      samples.push({
        'otu_ids': response.otu_ids[i], 
        'otu_labels': response.otu_labels[i],
        'sample_values': response.sample_values[i]
      });

    let sorted = samples.sort(function compareFunction(firstNum, secondNum) {
       return secondNum.sample_values - firstNum.sample_values;
      });
    
    let topTen = sorted.slice(0,10)

    let otu_ids = []
    let otu_labels = []
    let sample_values = []

    for (let k = 0; k < topTen.length; k++) {
      otu_ids.push(topTen[k].otu_ids);
      otu_labels.push(topTen[k].otu_labels);
      sample_values.push(topTen[k].sample_values);
    }
    
    let data = [{
      values: sample_values,
      labels: otu_ids,
      hovertext: otu_labels,
      type: 'pie'
    }];
    
    let layout = {
      title: ""
    };
    
    Plotly.newPlot('pie', data, layout);
  });  
}

function init() {
  // Grab a reference to the dropdown select element
  let selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
