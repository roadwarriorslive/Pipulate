import requests, datetime
from flask import session
import globs

def count():
  return 1

def dontgetfrustrated(x):
  num = 0
  s = []
  s.append("Heavy traffic on the Inter-Webs tonight.")
  s.append("Hang on a sec... I feel your pain.")
  s.append("You know, it's a miracle this is working at all.")
  s.append("tap, tap, tap, tap, tap, tap, tap, tap, tap")
  s.append("I cannot teach him. The boy has no patience.")
  s.append("Sometimes, you just gotta know when to call it quits.")
  s.append("I know your time is valuable. I'm not ignoring you..")
  s.append("Have confidence, girl! I accounted for this.")
  s.append("I'll time-out after about 30 seconds.")
  s.append("Google, I'm asking you a question!")
  s.append("Maybe go check your Facebook, Twitter or something.")
  s.append("I don't like this any more than you do.")
  yield "", s[num], "", ""
  num += 1
  if num == len(s):
    num = 0

def cyclemotto():
  try:
    session['i']
  except:
    session['i'] = 0
  else:
    session['i'] += 1
  s = []
  s.append("Paste a Google Spreadsheet URL and start pipulating.")
  s.append("Pipulate is a Free and Open Source app for SEO & Social Media.")
  s.append("Drag the bookmarklet to the Bookmark bar for easier pipulating.")
  s.append("To use Spreadsheets is human; to Pipulate, divine.")
  s.append("Capture Twitter and YouTube counts directly into Spreadsheets.")
  s.append("Capture FB Likes & Shares, Google Pluses, URL PageRanks and more.")
  s.append("Make a new Google Spreadsheet, name it, then click the Bookmarklet.")
  s.append("Change the sample data in Pipulate tab to your own profiles.")
  s.append("Schedule jobs to run automatically by sharing in a gmail.")
  s.append("Out of the box, Pipulate already does an awful lot.")
  s.append("Anything Pipulate doesn't do, you can make it do.")
  s.append("The easy customization is done under the Scrapers tab.")
  s.append("Advanced cusotmization is programmed in Python.")
  s.append("The Pipulate premise is really very simple.")
  s.append("Data in each column is either a function's input our output.")
  s.append("Pipulate comes with a lot of common functions built-in.")
  s.append("New functions can be written as stand-alone Python snippets.")
  s.append("Pipulate then applies your function to each row in the sheet.")
  s.append("Customizing Pipulate is easier than you think.")
  s.append("Pipulate is some good sheet.")
  s.append("I never met a KPI I couldn't collect.")
  s.append("How do I love thee? Let me Pipulate the ways.")
  s.append("Stop me before I Pipulate again.")
  s.append("This box shows the data that's being shot around, FYI.")
  s.append("Pipulate: It Slices. It Dices. It teaches you Python.")
  s.append("Pipulate relies on Google Docs because of its unique Web API.")
  s.append("Someday, Pipulate's dependency on Google Docs will go away.")
  s.append("Visit the project at: https://github.com/miklevin/pipulate")
  s.append("On a Mac? Open Terminal, then type \"python\", then \"import this\".")
  s.append("Google Python \"Hello World\" and try writing some code.")
  s.append("Download your own dedicated Pipulate server at Levinux.com.")
  s.append("Levinux: Give me 10 minutes, and I'll give you skills for life.")
  s.append("We all stand on the shoulders of giants.")
  s.append("Choose the correct giant-shoulders to stand on.")
  s.append("Ken Thompson, Linus Torvalds and Guido van Rossum are good giants.")
  s.append("I lost an electron. Are you positive?")
  s.append("Girl, you pipulate alot!")
  mottomodulo = session['i'] % len(s)
  try:
    return s[mottomodulo]
  except:
    return s[0]

def pipinit():
  s = []
  s.append(['https://www.youtube.com/user/miklevin','*','*','*'])
  s.append(['https://www.youtube.com/user/ForeverG5','*','*','*'])
  s.append(['https://www.youtube.com/user/PewDiePie','*','*','*'])
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
