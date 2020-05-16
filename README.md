# Property Sale Predictions in Melbourne

A full-stack AWS based web application that predicts property advertisements using the following AWS services: 
* AWS Elastic Container Registry to store Docker images to train and serve the prediction model
* AWS Sagemaker to train a boosted decision tree model
* AWS RDS to store training data and property advertisement listing data
* AWS DynamoDB to store Domain API data
* AWS Lambda to retrieve and store data from Domain's API to DynamoDB and get DynamoDB data
* AWS EC2 to host the prediction model API
* AWS S3 to store the static website assets
* AWS CloudFront as a CDN
