# Frontend

This directory contains the source code to the static webpage. The files in the directory are used to retrieve data from the various APIs hosted on AWS.

The web page uses Bootstrap styling, Leaflet.js to display the map and popups with tilesets from Mapbox and jQuery for web requests.

To deploy the front-end, follow the steps below:

* Set the files to be public
* In properties, under Static website hosting, set the bucket to be used as a Static website hosting and set the index document to index.html and save.
* Set up a CloudFront CDN and set the bucket as the source as the source. 
* Use the provided domain name under CloudFront as the entrypoint.
