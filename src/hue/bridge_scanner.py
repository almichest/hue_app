import requests
import json


def get_bridge_ips():
    res = requests.get('http://www.meethue.com/api/nupnp').text
    data = json.loads(res)
    return [map['internalipaddress'] for map in data]

print(get_bridge_ips())
