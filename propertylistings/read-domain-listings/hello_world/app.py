import json
import boto3
import requests
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


class DynamoDB:
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table("DomainListings")

    def get_all(self):
        scan = self.table.scan()["Items"]
        results = []
        for i in scan:
            results.append(json.dumps(i, cls=DecimalEncoder))
        return results

    def get_list(self, ids):
        results = []
        for id in ids:
            query = self.table.query(
                KeyConditionExpression=Key("id").eq(id)
            )
            results.append(json.dumps(query["Items"][0], cls=DecimalEncoder))

        return results


def lambda_handler(event, context):
    dynamodb = DynamoDB()
    try:
        if not event:
            results = dynamodb.get_all()
        else:
            results = dynamodb.get_list(event["id"])

        return {
            "statusCode": 200,
            "body": results
        }
    except ClientError as e:
        return {
            "statusCode": 404,
            "body": e.response["Error"]["Message"]
        }
