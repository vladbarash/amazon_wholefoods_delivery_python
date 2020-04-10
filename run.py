import requests
import json
from datetime import datetime


def main_func():
    
    url = "https://www.amazon.com/gp/checkoutportal/enter-checkout.html"
    querystring = {"proceedToCheckout":"1","ie":"UTF8","isFresh":"1","useDefaultCart":"1","brandId":"[...]","sessionID":"[...]","ref_":"[...]"}
    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'x-mash-csm-tc': "[...]",
        'user-agent': "[...]",
        'accept-language': "[...]",
        'cookie': "[...]",
        'cache-control': "no-cache"
        }
    AUTH = 'Basic [...]'

    response = requests.request("GET", url, headers=headers, params=querystring)
    r = json.dumps(response.text)
        
    if r.count('No delivery windows available.') < 2:
        url = "https://api.twilio.com/2010-04-01/Accounts/[...]/Messages.json"
        payload = {
            'From': "[...]",
            'Body': "Grocery delivery may be available.",
            'To': '[...]'
        }
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Authorization': AUTH,
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)


if __name__ == "__main__":
    main_func()
