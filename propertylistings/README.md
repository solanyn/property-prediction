# Lambda Functions

The two Lambda functions in this repository are deployed using the AWS SAM CLI tool. `get-domain-listings` retrieves data from the DynamoDB table through an API interface. `lambda-store-domain-listings` makes an request to the Domain API and stores the retrieved data in the DynamoDB table.

Install the AWS SAM CLI tool. Since two serverless applications are already set up, to deploy the files, call `sam deploy`. 

The functions are built using the Hello World as a template<sup>[1]</sup> and the functions reside in the `hello_world` directory under `app.py`. The function dependencies are also included in `requirements.txt`.

## References:
[1]"Tutorial: Deploying a Hello World Application - AWS Serverless Application Model", docs.aws.amazon.com, 2020. [Online]. Available: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html. [Accessed: 08- May- 2020].
