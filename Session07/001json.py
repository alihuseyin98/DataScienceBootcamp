import requests
res=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
import json
d=json.loads(res.content)
print(d["time"])