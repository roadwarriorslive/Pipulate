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

