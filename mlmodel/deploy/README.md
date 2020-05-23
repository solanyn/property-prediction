# ML Model Microservice API

This directory contains the necessary source code and Dockerfile to build a Docker image and push the image. The image retrieves the serialized machine learning model object with a FastAPI and Uvicorn application. Predictions can be made using API calls on a hosted instance. The application is intended to be hosted on an EC2 instance with an elastic IP associated with it. The `start.sh` script is used to get credentials for the EC2 instance to pull and run the image from Amazon Elastic Container Registry. The first time an EC2 instance is created, Docker must be installed on the instance and the contents of `start.sh` must be copied to `/etc/rc.local`.

To push this to the Amazon ECR, make sure the AWS CLI and Docker are installed and that necessary credentials are provided to access the account using the AWS CLI.

To build and push the image to the repository run the following commands:

`aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 462888025389.dkr.ecr.us-east-1.amazonaws.com
docker build -t serve_model .
docker tag serve_model:latest 462888025389.dkr.ecr.us-east-1.amazonaws.com/serve_model:latest
docker push 462888025389.dkr.ecr.us-east-1.amazonaws.com/serve_model:latest`
