import requests

def walkdict(obj, key):
  stack = obj.items()
  while stack:
    k, v = stack.pop()
    if isinstance(v, dict):
      stack.extend(v.iteritems())
    else:
      if k == key:
        return v

def scrapes():
  scrapelist = []
  scrapelist.append(['tweets',    'xpath', "//span[.='Tweets']/following-sibling::span/text()"])
  scrapelist.append(['following', 'xpath', "//span[.='Following']/following-sibling::span/text()"])
  scrapelist.append(['followers', 'xpath', "//span[.='Followers']/following-sibling::span/text()"])
  scrapelist.append(['views',     'xpath', "//div[@class='watch-view-count']/text()"])
  scrapelist.append(['thumbsup',  'xpath', "//button[@id='watch-like']/span/text()"])
  scrapelist.append(['thumbsdown','xpath', "//button[@id='watch-dislike']/span/text()"])
  scrapelist.append(['ga',        'regex', r"(?:\'|\")(?P<scrape>UA-.*?)(?:\'|\")"])
  return scrapelist

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
  # Lower line no longer necessary, but kept a little while for clarity!
  # return adict['result']['metadata']['globalCounts']['count']
  return walkdict(adict, 'count')

def tweeted(url):
  api = "http://urls.api.twitter.com/1/urls/count.json?url="
  respobj = requests.get(api + url)
  adict = respobj.json()
  return adict["count"]

def shares(url):
  api = "http://graph.facebook.com/?id="
  respobj = requests.get(api + url)
  adict = respobj.json()
  try:
    return adict["shares"]
  except:
    pass


