# Property Price Predictions in Melbourne

A full-stack AWS based web application that predicts prices of property advertisements. The web page is built with Leaflet.js using tilesets from Mapbox, Bootstrap styling and jQuery for web requests. The application uses Lambda functions to interface with DynamoDB and using API Gateway as an endpoint. A Docker image is used to deploy an API to serve machine learning predictions using FastAPI and Uvicorn running on an EC2 instance. 

The following AWS services are used:  
* Amazon Elastic Container Registry to store Docker images to train and serve the prediction model
* Amazon Sagemaker to train a gradient boosted decision tree model
* Amazon RDS to store training data and property advertisement listing data
* Amazon DynamoDB to store Domain API data
* Amazon Lambda to retrieve and store data from Domain's API to DynamoDB and get DynamoDB data
* Amazon EC2 to serve the prediction model as an API
* Amazon S3 to store the static website assets
* Amazon CloudFront as a CDN
* Amazon API Gateway as a centralised endpoint management
