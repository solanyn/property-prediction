# Frontend

This directory contains the source code to the static webpage. The files in the directory are used to retrieve data from the various APIs hosted on AWS.

The web page uses Bootstrap[1] styling, Leaflet.js[2] to display the map and popups with tilesets from Mapbox[3] and jQuery[4] for web requests.

To deploy the front-end, follow the steps below:

* Set the files to be public
* In properties, under Static website hosting, set the bucket to be used as a Static website hosting and set the index document to index.html and save.
* Set up a CloudFront CDN and set the bucket as the source as the source. 
* Use the provided domain name under CloudFront as the entrypoint.

## References
[1]a. Mark Otto, "Introduction", getbootstrap.com, 2020. [Online]. Available: https://getbootstrap.com/docs/4.5/getting-started/introduction/. [Accessed: 07- May- 2020].

[2]"Documentation - Leaflet - a JavaScript library for interactive maps", leafletjs.com, 2020. [Online]. Available: https://leafletjs.com/reference-1.6.0.html. [Accessed: 23- May- 2020].

[3]"Documentation", Mapbox, 2020. [Online]. Available: https://docs.mapbox.com/. [Accessed: 07- May- 2020].

[4]"jQuery API Documentation", api.jquery.com, 2020. [Online]. Available: https://api.jquery.com/. [Accessed: 07- May- 2020].
