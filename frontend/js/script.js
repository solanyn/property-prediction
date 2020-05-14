async function onInit() {
	layer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1
	}).addTo(mymap);

	// Alert with instructions
	$("#warn").hide();
}

async function getData() {
	await $.getJSON("https://athty56064.execute-api.us-east-1.amazonaws.com/Prod/", result => {
		data = result.body.map(s => JSON.parse(s))
	});

	await displayData();
}


function displayData() {
	data.forEach(item => {
		let valid = true;
		keys.forEach(field => {
			if (item.propertyDetails[field] === undefined) {
				valid = false;
				return;
			}
		});

		if (!valid)
			return;

		var marker = L.marker([item.propertyDetails.latitude, item.propertyDetails.longitude])
			.addTo(mymap)
			.on('click', onClick);
		marker.data = item.propertyDetails;

		htmlString = "";
		htmlString = htmlString.concat("<table class=\"table table-sm\">");
		htmlString = htmlString.concat("<thead class=\"thead-dark\"><tr><th>Address</th><th>", marker.data.displayableAddress, "</th></tr></thead>");
		htmlString = htmlString.concat("<tbody><tr><td>Suburb</td><td>", marker.data.suburb, "</td></tr>");
		htmlString = htmlString.concat("<tr><td>Type</td><td>", marker.data.allPropertyTypes[0], "</td></tr>");
		htmlString = htmlString.concat("<tr><td>Postcode</td><td>", marker.data.postcode, "</td></tr>");
		htmlString = htmlString.concat("<tr><td>Bedrooms</td><td>", marker.data.bedrooms, "</td></tr>");
		htmlString = htmlString.concat("<tr><td>Bathrooms</td><td>", marker.data.bathrooms, "</td></tr>");
		htmlString = htmlString.concat("<tr><td>Carspaces</td><td>", marker.data.carspaces, "</td></tr>");
		htmlString = htmlString.concat("</tbody></table>");
		marker.bindPopup(htmlString);
	});
}


async function predictPrice() {
	if (selected != null && (!("price" in selected.data))) {
		let type;
		if (selected.data.allPropertyTypes[0] == "ApartmentUnitFlat") {
			type = "u";
		} else if (selected.data.allPropertyTypes[0] == "House") {
			type = "h";
		} else if (selected.data.allPropertyTypes[0] == "Townhouse") {
			type = "t";
		}

		postData = {
			"suburb": selected.data.suburb,
			"rooms": selected.data.bedrooms,
			"type": type,
			"postcode": selected.data.postcode,
			"bathroom": selected.data.bathrooms,
			"car": selected.data.carspaces
		};

		let response = await postPredictData(postData);
		let price = response.body.price;
		selected.data.price = price;

		let htmlString = "";
		htmlString = htmlString.concat("<table class=\"table table-sm\">");
		htmlString = htmlString.concat("<thead class=\"thead-dark\"><tr><th>Address</th><th>", selected.data.displayableAddress, "</th></tr></thead>");
		htmlString = htmlString.concat("<tbody><tr><td>Suburb</td><td>", selected.data.suburb, "</td></tr>");
		htmlString = htmlString.concat("<tr><td>Type</td><td>", selected.data.allPropertyTypes[0], "</td></tr>");
		htmlString = htmlString.concat("<tr><td>Postcode</td><td>", selected.data.postcode, "</td></tr>");
		htmlString = htmlString.concat("<tr><td>Bedrooms</td><td>", selected.data.bedrooms, "</td></tr>");
		htmlString = htmlString.concat("<tr><td>Bathrooms</td><td>", selected.data.bathrooms, "</td></tr>");
		htmlString = htmlString.concat("<tr><td>Carspaces</td><td>", selected.data.carspaces, "</td></tr>");
		htmlString = htmlString.concat("<tr class=\"table-success\"><th>Predicted Price</th><th>$", Math.round(price), "</th></tr>");
		htmlString = htmlString.concat("</tbody></table>");
		selected.bindPopup(htmlString);
	}

	if (selected == null || selected == undefined) {
		$("#welcome").alert("close");
		$("#warn").show();
	}
}


async function postPredictData(postData) {
	let response = await fetch("https://ra4nhjlooe.execute-api.us-east-1.amazonaws.com/prod/predict", {
		method: "POST",
		body: JSON.stringify(postData)
	});
	let resdata = await response.json();
	return resdata;
}


function onClick(e) {
	e.target.getPopup().on("remove", () => {
		selected = null;
		$("#warn").hide();
	});
	selected = e.target;
	$("#warn").hide();
}

// Stuff starts here
let keys = ["suburb", "propertyType", "postcode", "bedrooms", "bathrooms", "carspaces"]
let mymap = L.map('mapid').setView([-37.8136, 144.9631], 12);
let layer;
onInit();
let data;
let selected;
getData();

