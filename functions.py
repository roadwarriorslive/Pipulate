import requests, datetime
from flask import session
import globs

def rawserps(keyword):
  import time, json
  times = 4
  api = "http://ajax.googleapis.com/ajax/services/search/web"
  returnme = []
  for start in [8*n for n in range(0,times)]:
    pdict = {'rsz':'large', 'v':'1.0', 'q': keyword, 'start':start}
    respobj = requests.get(api, params=pdict)
    returnme.append(respobj.json())
    time.sleep(1)
  return json.dumps(returnme)

def positions(rawserps=''):
  import json
  if rawserps:
    serplist = json.loads(rawserps)
    serplist = serplist[0]["responseData"]["results"]
    shortdict = {}
    for i, result in enumerate(serplist):
      shortdict[i+1] = result['url']
    return json.dumps(shortdict)

  else:
    return "I would execute rawserps"

#This is only here to remind myself it's available for user functions.
def walkdict(obj, key):
  stack = obj.items()
  while stack:
    k, v = stack.pop()
    if isinstance(v, dict):
      stack.extend(v.iteritems())
    else:
      if k == key:
        return v
  return None

def response(url):
  if globs.hobj:
    return globs.hobj.status_code
  else:
    try:
      return requests.get(url).status_code
    except:
      return "Error"

def plusses(url):
  api = "https://clients6.google.com/rpc"
  jobj = '''{
    "method":"pos.plusones.get",
    "id":"p",
    "params":{
        "nolog":true,
        "id":"%s",
        "source":"widget",
        "userId":"@viewer",
        "groupId":"@self"
        },
    "jsonrpc":"2.0",
    "key":"p",
    "apiVersion":"v1"
  }''' % (url)
  respobj = requests.post(api, jobj)
  adict = respobj.json()
  return walkdict(adict, 'count')

def tweets(url):
  api = "http://urls.api.twitter.com/1/urls/count.json?url="
  respobj = requests.get(api + url)
  adict = respobj.json()
  return walkdict(adict, 'count')

def shares(url):
  respobj = requests.get('https://graph.facebook.com/' + url) 
  adict = respobj.json()
  return walkdict(adict, 'shares')

def likes(url): 
  respobj = requests.get('https://graph.facebook.com/' + url) 
  adict = respobj.json()
  return walkdict(adict, 'likes')
