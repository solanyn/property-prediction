import json
import requests 
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth


def auth(client_id, secret):
    auth = HTTPBasicAuth(client_id, secret)
    payload = {
            "grant_type": "client_credentials",
            "scope": "api_listings_read api_agencies_read"
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


if __name__ == "__main__":
    auth_handler("", "")
