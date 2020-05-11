import requests
import json
import boto3
from requests.auth import HTTPBasicAuth
from botocore.exceptions import ClientError
from decimal import Decimal


class Domain:
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table("DomainListings")
        with open("oauth.json", "r") as f:
            details = json.load(f)
            f.close()
        self.client_id = details["clientId"]
        self.secret = details["secret"]
        self.access_token = ""

    def auth(self):
        auth = HTTPBasicAuth(self.client_id, self.secret)
        payload = {
            "client_id": self.client_id,
            "client_secret": self.secret,
            "Content-Type": "text/json",
            "grant_type": "client_credentials",
            "scope": "api_listings_read api_salesresults_read api_suburbperformance_read"
        }

        self.access_token = requests.post(
            "https://auth.domain.com.au/v1/connect/token", data=payload, auth=auth).json()["access_token"]

    def store_listings_batch(self):
        authorisation = {"Authorization": "Bearer " + self.access_token}
        i = 0
        payload = {
            "listingType": "Sale",
            "propertyTypes": [
                "House",
                "Townhouse",
                "ApartmentUnitFlat"
            ],
            "locations": [
                {
                    "state": "VIC",
                    "region": "Melbourne Region",
                    "area": "",
                    "suburb": "",
                    "postCode": ""
                }
            ],
            "sort": {
                "sortKey": "DateListed",
                "direction": "Descending"
            },
            "pageSize": 25,
            "pageNumber": i
        }

        r = requests.post(
            "https://api.domain.com.au/v1/listings/residential/_search", json=payload, headers=authorisation)

        totalPages = r.headers["X-Total-Count"]
        # Write to file
        if r.status_code == 200:
            # Write to DynamoDB
            try:
                with self.table.batch_writer(overwrite_by_pkeys=["id"]) as batch:
                    for listing in json.loads(json.dumps(r.json()), parse_float=Decimal):
                        item = {}
                        item["id"] = listing["listing"]["id"]
                        item["propertyDetails"] = dict()
                        for k, v in listing["listing"]["propertyDetails"].items():
                            if v != '':
                                item["propertyDetails"][k] = v
                        batch.put_item(Item=item)
            except ClientError as e:
                print(e.response["Error"]["Message"])
        else:
            return False
        return True

    def store_listings_put(self):
        authorisation = {"Authorization": "Bearer " + self.access_token}
        i = 0
        payload = {
            "listingType": "Sale",
            "propertyTypes": [
                "House",
                "Townhouse",
                "ApartmentUnitFlat"
            ],
            "locations": [
                {
                    "state": "VIC",
                    "region": "Melbourne Region",
                    "area": "",
                    "suburb": "",
                    "postCode": ""
                }
            ],
            "sort": {
                "sortKey": "DateListed",
                "direction": "Descending"
            },
            "pageSize": 200,
            "pageNumber": i
        }

        r = requests.post(
            "https://api.domain.com.au/v1/listings/residential/_search", json=payload, headers=authorisation)

        totalPages = r.headers["X-Total-Count"]
        r = requests.post(
            "https://api.domain.com.au/v1/listings/residential/_search", json=payload, headers=authorisation)
        # Write to file
        if r.status_code == 200:
            # Write to DynamoDB
            for listing in json.loads(json.dumps(r.json()), parse_float=Decimal):
                item = {}
                item["id"] = listing["listing"]["id"]
                item["propertyDetails"] = dict()
                for k, v in listing["listing"]["propertyDetails"].items():
                    if v != '':
                        item["propertyDetails"][k] = v
                self.table.put_item(Item=item)
        else:
            return False
        return True


def lambda_handler(event, context):
    d = Domain()
    d.auth()

    if d.store_listings_batch():
        return {
            'statusCode': 200,
            'body': json.dumps('Stored listings successfully')
        }

    return {
        'statusCode': 404,
        'body': json.dumps("Failed to store listings")
    }
