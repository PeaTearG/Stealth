import requests
import urllib3
from Stealth import grabcreds


def connect(method, resource, params=None, payload=None):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    headers = {"accept": "application/json"}
    env = grabcreds.main("stealth", "sil")
    auth = env[:2]
    baseurl = env[2]
    url = "https://{}:8448/uisStealth/EcoApi/latest/{}".format(baseurl,resource)
    if method.lower() == "get":
        r = requests.get(url=url, auth=auth, headers=headers, verify=False, params=params)
    elif method.lower() == "post":
        r = requests.post(url=url, auth=auth, headers=headers, verify=False, params=params)
    elif method.lower() == "delete":
        r = requests.delete(url=url, auth=auth, headers=headers, verify=False, params=params)
    elif method.lower() == "put":
        r = requests.put(url=url, auth=auth, headers=headers, verify=False, params=params, json=payload)
    return r


