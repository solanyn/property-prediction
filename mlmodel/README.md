# Components to serve the ML Model

This directory contains a few components:

* The first is `Property Price Prediction.ipynb`. This is an IPython Notebook file to be run in an Amazon SageMaker notebook instance. The notebook results in a serialized machine learning model object that gets saved to an S3 bucket using boto3 API[1]. The model is based on the Catboost algorithm[2].

* The second is the API microservice. The microservice is composed of a Docker image that serves the prediction model created by the notebook. It uses a FastAPI application hosted by a Uvicorn server instance[3]. After the Docker image is built, the image is then pushed to Amazon Elastic Container Registry from which an EC2 instance can pull the image and host the API by writing the contents of `start.sh` to `/etc/rc.local` on the EC2 instance.

* The third is the training microservice to update the machine learning model for new model revisions. This is to be run when the model needs to be updated when more data is available in the database.

## References
[1]"Boto3 documentation — Boto3 Docs 1.13.16 documentation", boto3.amazonaws.com, 2020. [Online]. Available: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html. [Accessed: 07- May- 2020].
[2]"CatBoost Documentation", catboost.ai, 2020. [Online]. Available: https://catboost.ai/docs/concepts/about.html. [Accessed: 07- May- 2020].
[3]"FastAPI", fastapi.tiangolo.com, 2020. [Online]. Available: https://fastapi.tiangolo.com/. [Accessed: 07- May- 2020].
