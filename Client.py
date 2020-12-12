import requests

def get(url):
    r = requests.get(url)
    res = r.json()
    return res
