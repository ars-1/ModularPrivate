function toggleTwo() {
    let element = document.getElementById('TwoData');
    if (element.style.height == "28%") {
        element.style.height = "0px";
    } else {
        element.style.height = "28%";
    }
}

function toggleThree() {
    let element = document.getElementById('ThreeData');
    if (element.style.height == "16%") {
        element.style.height = "0px";
    } else {
        element.style.height = "16%";
    }
}

//Line Chart
var xValuesForLineChart = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
var yValuesForLineChart = [0, 4, 2, 5, 7, 5, 3, 7];

new Chart("LineChart", {
    type: "line",
    data: {
        labels: xValuesForLineChart,
        datasets: [{
            fill: false,
            lineTension: 0,
            backgroundColor: "rgba(244,67,54,1.0)",
            borderColor: "rgba(254,85,34,0.1)",
            color: "rgba(0,0,0,1.0)",
            data: yValuesForLineChart
        }]
    },
    options: {
        legend: {display: false},
        scales: {
            yAxes: [{ticks: {min: 0, max: 7}}],
        }
    }
});


//PieChart
var xValuesForPieChart = ["Area1", "Area2", "Area3", "Area4", "Area5"];
var yValuesForPieChart = [55, 49, 44, 24, 15];
var barColors = [
    "#b91d47",
    "#00aba9",
    "#2b5797",
    "#e8c3b9",
    "#1e7145"
];

new Chart("PieChart", {
    type: "pie",
    data: {
        labels: xValuesForPieChart,
        datasets: [{
            backgroundColor: barColors,
            data: yValuesForPieChart
        }]
    },
    options: {
        title: {
            display: true,
            text: "Area Distribution By Clients"
        }
    }
});


//BarChart
var xValuesForBarChart = ["Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7"];
var yValuesForBarChart = [55, 49, 44, 24, 65, 85, 55];
var barColors = ["#bb86fc", "#bb86fc", "#bb86fc", "#bb86fc", "#bb86fc", "#bb86fc", "#bb86fc"];

new Chart("BarChart", {
    type: "bar",
    data: {
        labels: xValuesForBarChart,
        datasets: [{
            backgroundColor: barColors,
            data: yValuesForBarChart
        }]
    },
    options: {
        legend: {display: false},
        title: {
            display: true,
            text: ""
        }
    }
});