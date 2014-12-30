def Func1():
  return "Out from Function One"

def Func2(param1, param2='', status='Okay'):
  return "%s %s" % (param1, param2)

def tweets(url):
  import requests
  api = "http://urls.api.twitter.com/1/urls/count.json?url="
  respobj = requests.get(api + url)
  adict = respobj.json()
  return adict["count"]

def plusses(url):
  import requests
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
  return adict['result']['metadata']['globalCounts']['count']

def fbshares(url):
  import requests
  api = "http://graph.facebook.com/?id="
  respobj = requests.get(api + url)
  adict = respobj.json()
  return adict["shares"]


