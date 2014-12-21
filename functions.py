def Func1():
  return "Out from Function One"

def Func2(param1, param2='', status='Okay'):
  return "%s %s" % (param1, param2)

def tweets(url):
  import urllib2, json
  api = "http://urls.api.twitter.com/1/urls/count.json?url="
  respobj = urllib2.urlopen(api + url)
  adict = json.load(respobj)
  return adict["count"]

