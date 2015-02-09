import requests, datetime
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
  s.append("And now for something completely different... Pipulate!")
  s.append("What do you want to Pipulate today?")
  s.append("Step 1: Drag the bookmarklet to the Bookmark bar.")
  s.append("You can change the sample data filled into the Pipulate tab,")
  s.append("Make a Google Spreadsheet and click the Bookmarklet.")
  s.append("Pipulate can be coerced to do almost anything.")
  s.append("I never met a KPI I couldn't collect.")
  s.append("This box shows the data that's being shot around, FYI.")
  s.append("Need to scrape something different off the page? Scrapers tab!")
  s.append("Want real power? Try learning Regular Expressions!")
  s.append("I'd pipulate in Excel, but GDocs is free and has a Web API.")
  s.append("Point of interest: Pipulate is written in Python.")
  s.append("Visit the project at: https://github.com/miklevin/pipulate")
  s.append("On a Mac? Open Terminal, then type \"python\", then \"import this\".")
  s.append("To exit, type \"exit()\". Makes sense, right?")
  s.append("Careful, or else you might start learning some Python.")
  s.append("Download your own dedicated Pipulate server at Levinux.com.")
  s.append("Levinux: Give me 10 minutes, and I'll give you skills for life.")
  s.append("Learn the tech \"Short \"Stack: Linux, Python, vim and git.")
  s.append("You don't need to learn programming, but it really helps.")
  s.append("We all stand on the shoulders of giants.")
  s.append("The trick is choosing the correct shoulders to stand on.")
  s.append("Google Ken Thompson, Linus Torvalds and Guido van Rossum.")
  s.append("For extra points, google Richard Stallman.")
  s.append("I lost an electron. Are you positive?")
  s.append("Genius is mostly a matter of careful cultivation.")
  s.append("Girl, you pipulate alot!")
  mottomodulo = session['i'] % len(s)
  try:
    return s[mottomodulo]
  except:
    return s[0]

def pipinit():
  s = []
  s.append(['https://www.youtube.com/user/miklevin','*','*'])
  s.append(['https://www.youtube.com/user/ForeverG5','*','*'])
  s.append(['https://www.youtube.com/user/PewDiePie','*','*'])
  return s

def pipinit2():
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

def isotimestamp():
  i = datetime.datetime.now()
  return "%s" % i.isoformat() 

def datestamp():
  now = datetime.datetime.now()
  now = now.strftime("%B %d, %Y")
  return now
  
def timestamp():
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
