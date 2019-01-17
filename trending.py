import requests,os
from pprint import pprint as pp

api_key = os.environ['giphy_key']

base_url = "https://api.giphy.com/v1/gifs/trending"

headers = {
    'api_key' : api_key,
    'limit' : 5,
    'offset' : 0,
    'rating' : 'g',
    'string' : 'json'
}

res = requests.get(base_url,headers=headers)
pp(res.status_code)
pp(res.json()['data'][0])
