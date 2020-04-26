import json
import requests

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

def get_token():
    with open("token.txt", "r") as f:
        token = f.read()

    return token

def get_listings():
    token = get_token()
    payload = {
        "listingType": "Sale",
        "locations": [
            {
                "state": "VIC",
                "region": ""
            }
        ]
    }
    r = requests.post("https://api.domain.com.au/v1/listings/residential/_search", data=payload, auth=BearerAuth(token))
    print(r.text)

if __name__ == "__main__":
    get_listings()
