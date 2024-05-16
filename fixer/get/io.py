import requests
import json

base='http://data.fixer.io/api/latest?access_key='


def get_rates(key):
  response=requests.get(base+key)
  if response.status_code==200:
    return json.loads(response.text);
  return None
  
