import requests
import globs

def cyclemotto():
  from flask import session
  try:
    session['i']
  except:
    session['i'] = 0
  else:
    session['i'] += 1
  s = []
  s.append("What do you want to Pipulate today?")
  s.append("Shows on second cycle")
  s.append("Pipulate: What do you want it to be today?")
  s.append("Small Data is the new Big")
  s.append("Try making a new Scrape pattern.")
  s.append("Want real power? Learn Regular Expressions!")
  s.append("I lost an electron. Are you positive?")
  s.append("Careful, you might learn Python.")
  try:
    return session['i']
  except:
    return 'bar'

def pipinit():
  s = []
  s.append(['http://mikelev.in','*','*','*','*','*','*'])
  s.append(['http://levinux.com','*','*','*','*','*','*'])
  s.append(['http://pipulate.com','*','*','*','*','*','*'])
  s.append(['http://www.flyingpointdigital.com','*','*','*','*','*','*'])
  return s

def scrapes():
  s = []
  s.append(['title',       'xpath', "//title/text()"])
  s.append(['description', 'xpath', "//meta[@name='description']/@content"])
  s.append(['tweets',      'xpath', "//span[.='Tweets']/following-sibling::span/text()"])
  s.append(['following',   'xpath', "//span[.='Following']/following-sibling::span/text()"])
  s.append(['followers',   'xpath', "//span[.='Followers']/following-sibling::span/text()"])
  s.append(['views',       'xpath', "//div[@class='watch-view-count']/text()"])
  s.append(['thumbsup',    'xpath', "//button[@id='watch-like']/span/text()"])
  s.append(['thumbsdown',  'xpath', "//button[@id='watch-dislike']/span/text()"])
  s.append(['subscribers', 'regex', r"subscriber-count.*?>(?P<scrape>[0-9,]+?)<"])
  s.append(['ga',          'regex', r"(?:\'|\")(?P<scrape>UA-.*?)(?:\'|\")"])
  return s

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

def datestamp():
  import datetime
  return datetime.date.today()
  
def timestamp():
  import datetime
  return datetime.datetime.today().strftime('%X')

def response(url):
  if globs.hobj:
    return globs.hobj.status_code
  else:
    try:
      return requests.get(url).status_code
    except:
      return "Error"

def plussed(url):
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
  return walkdict(adict, 'count')

def shared(url):
  respobj = requests.get('https://graph.facebook.com/' + url) 
  adict = respobj.json()
  return walkdict(adict, 'shares')

def liked(url): 
  respobj = requests.get('https://graph.facebook.com/' + url) 
  adict = respobj.json()
  return walkdict(adict, 'likes')
