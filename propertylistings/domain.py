# https://colab.research.google.com/drive/16wg0VWPim1-dwt7W8jZuJrqFRMrW8iQ0#scrollTo=M9WV6WDU5k-0
# Reference on how to auth and access with Python

import json
import requests 
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth


def auth(client_id, secret):
    auth = HTTPBasicAuth(client_id, secret)
    payload = {
            "client_id": client_id
            , "client_secret": secret
            , "Content-Type": "text/json"
            , "grant_type": "client_credentials"
            , "scope": "api_listings_read api_salesresults_read api_suburbperformance_read"
    }
    r = requests.post("https://auth.domain.com.au/v1/connect/token", data=payload, auth=auth)
    return r 


def auth_handler(event, context):
    message = ""
    with open("oauth.json", "r") as f:
        details = json.load(f)
    clientId = details["clientId"] 
    secret = details["secret"]
    r = auth(clientId, secret)
    if r is not None:
        f = open("token.txt", "w")
        f.write(r.json()["access_token"])
        message = "success"
        f.close()

    return {
        "message": message,         
    }



def get_token():
    with open("token.txt", "r") as f:
        token = f.read()
        f.close()

    return token

def get_listings():
    payload = {
        "listingType": "Sale",
        "locations": [
            {
                "state": "VIC"
                , "region": ""
                , "area": ""
                , "suburb": ""
                , "postCode": ""
                , "includeSurroundingSuburbs": False
            }
        ],
    }
    auth = { "Authorization": "Bearer " + get_token()}
    r = requests.post("https://api.domain.com.au/v1/listings/residential/_search", json=payload, headers=auth)
    print(r.json())
    with open("data/listings.json", "w") as f:
        json.dump(r.json(), f)

def get_sales_results(city):
    auth = {"Authorization": "Bearer " + get_token()}
    r = requests.get("https://api.domain.com.au/v1/salesResults/"+city+"listings", headers=auth)
    print(r.json())
    with open("data/sales_results.json", "w") as f:
        json.dump(r.json(), f)

if __name__ == "__main__":
    get_listings()
    get_sales_results("Melbourne")
