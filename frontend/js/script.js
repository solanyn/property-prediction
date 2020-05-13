function onInit() {
	layer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1
	}).addTo(mymap);	
}

async function getData() {
	await $.getJSON("https://athty56064.execute-api.us-east-1.amazonaws.com/Prod/", result => {
		data = result.body.map(s => JSON.parse(s));
	});
	displayData();
}

function displayData() {  
	data.forEach(item => {
		var marker = L.marker([item.propertyDetails.latitude, item.propertyDetails.longitude])
			.addTo(mymap)
			.on('click', onClick);
		marker.data = item.propertyDetails;
		htmlString = "";
		htmlString = htmlString.concat("<h6>", marker.data.displayableAddress, "</h6>");
		marker.bindPopup(htmlString);
	});
}

function predictPrice() {
	if (selected) {
		// Update Popup with Price
		var type;
		if (selected.data.allPropertyTypes[0] == "ApartmentUnitFlat") {
			type = "u";
		} else if (selected.data.allPropertyTypes[0] == "House") {
			type = "h";
		} else if (selected.data.allPropertyTypes[0] == "Townhouse") {
			type = "t";
		}

		postData = {
			"suburb": selected.data.suburb,
			"rooms": selected.data.rooms,
			"type": type,
			"postcode": String(selected.data.postcode),
			"bathroom": selected.data.bathroom,
			"car": selected.data.carspaces
		};

		testJSON = {
			"suburb": "Noble Park",
			"rooms": 3,
			"type": "h",
			"postcode": "3174",
			"bathroom": 3,
			"car": 2
		};
		
		$.post("https://ra4nhjlooe.execute-api.us-east-1.amazonaws.com/prod/predict", postData, result => {
			console.log(result);
		});

	} else {
		console.log("No selected property");
	}

}

function onClick(e) {
	e.target.getPopup().on("remove", () => {
		selected = null;
	});
	selected = e.target;
}

// Stuff starts here
let mymap = L.map('mapid').setView([-37.8136, 144.9631], 12);
let layer;
onInit();
let data;
let selected;

getData();

// var popup = L.popup();