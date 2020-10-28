import json

import requests


def GET_request(url):
    res = requests.get(url)
    if res.status_code == 200:
        print("Peticion exitosa")
        return json.loads(res.text)
    print("Peticion fallida")
    return None
