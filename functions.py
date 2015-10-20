#  _   _                 _____                 _   _                 
# | | | |___  ___ _ __  |  ___|   _ _ __   ___| |_(_) ___  _ __  ___ 
# | | | / __|/ _ \ '__| | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
# | |_| \__ \  __/ |    |  _|| |_| | | | | (__| |_| | (_) | | | \__ \
#  \___/|___/\___|_|    |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#                                                                    
# Welcome to User Functions, a file that lets you extend Pipulate's capability.
# Let's meet some libraries and modules we make available to every function.

import os, requests, datetime, json, time, urlparse, re   #All standard system libraries
from flask import session                                 #For if user function needs session info
import globs                                              #All objects treated as global variables (but somehow less despised)
from common import *                                      #For if user function neeeds framework functions

#  _   _      _                   _____                 _   _                 
# | | | | ___| |_ __   ___ _ __  |  ___|   _ _ __   ___| |_(_) ___  _ __  ___ 
# | |_| |/ _ \ | '_ \ / _ \ '__| | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
# |  _  |  __/ | |_) |  __/ |    |  _|| |_| | | | | (__| |_| | (_) | | | \__ \
# |_| |_|\___|_| .__/ \___|_|    |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#              |_|                                                            
# Take a look at some support-functions you can call from your own functions.
# The jobs done by these are so common, they get used almost everywhere.

def sleep():
  import time, datetime
  time.sleep(10)
  i = datetime.datetime.now()
  return i.strftime("%m/%d/%Y %H:%M:%S")

def gethtml(url):
  '''Return HTML text from given URL. Makes attempt to recycle pre-fetched
  HTML from current if any of them used the same URL input parameter.'''
  if globs.html:
    out("Recycling HTML.")
    return globs.html
  else:
    out("Doing first HTML fetch for row.")
    path = urlparse.urlparse(url).path
    ext = os.path.splitext(path)[1]
    if ext not in globs.texttypes:
      try:
        defend = requests.head(url)
      except:
        return None
      if 'Content-Type' in defend.headers:
        ct = defend.headers['Content-Type']
      else:
        return None
      if ct != '' and 'text' not in ct:
        return None
    try:
      globs.hobj = requests.get(url, timeout=(5, 10))
    except:
      return None
    globs.html = globs.hobj.text
  return globs.html

def unarchive(archive):
  import base64, bz2
  binary = base64.b64decode(archive)
  newhtml = bz2.decompress(binary)
  return newhtml

def archive(url):
  '''Return HTML text for given URL. Simple wrapper for gethtml function.'''
  def replacepat(pat, replacement, string):
    import re
    cpat = re.compile(pat, re.S | re.I)
    return cpat.sub(replacement, string) 
  import base64, bz2
  somehtml = requests.get(url).text
  globs.html = somehtml
  import re
  badpats = ['id="__EVENTVALIDATION" value=".*?"', 'id="__VIEWSTATE" value=".*?"']
  for pat in badpats:
    somehtml = replacepat(pat, '', somehtml)
  utf8html = somehtml.encode('utf-8-sig')
  compressed = bz2.compress(utf8html)
  cellfriendly = base64.b64encode(compressed)
  maxl = 900000
  alen = len(cellfriendly)
  if alen > maxl:
    return "[HTML too big to archivei (%s > %s)]" % (alen, maxl)
  return cellfriendly
  whatisthatmess = {
    'url' : url,
    'base64.decode(bz2.decompress(this))': cellfriendly
    }
  return json.dumps(whatisthatmess)

def walkdict(obj, key):
  """Take a JSON object and key and return the first matched value from the object."""
  stack = obj.items()
  while stack:
    k, v = stack.pop()
    if isinstance(v, dict):
      stack.extend(v.iteritems())
    else:
      if k == key:
        return v
  return None

def extension(url):
  """Return the file extension, given (typically) a URL."""
  if url:
    path = urlparse.urlparse(url).path
    ext = os.path.splitext(path)[1]
    return ext
  else:
    return None

def regex(text, pattern):
  """Take text and a Regular Expression using a group named scrape, and return match."""
  if text[:4].lower() == 'http':
    text = requests.get(text).text
  match = re.search(pattern, text, re.S | re.I)
  if match:
    if "scrape" in match.groupdict().keys():
      return match.group("scrape")
  else:
    return None

def scraper(text, anxpath):
  """Take html and an XPATH, and return match."""
  if text[:4].lower() == 'http':
    text = requests.get(text).text
  import lxml.html
  searchme = lxml.html.fromstring(text)
  match = searchme.xpath(anxpath)
  if match:
    return match[0]
  else:
    return None

def xml(url):
  text = requests.get(url).text
  import lxml.html
  xobj = lxml.html.document_fromstring(text)
  from lxml import etree
  return (etree.tostring(xobj, pretty_print=True))

def jsonapi(endpoint, url, jkey):
  """Take a JSON API endpoint, a URL as a parameter and key name to return value pair."""
  thecall = endpoint + url
  respobj = requests.get(thecall, timeout=5)
  adict = respobj.json()
  return walkdict(adict, jkey)

#  ____                                   ____        __ _       _ _   _                 
# / ___|  ___ _ __ __ _ _ __   ___ _ __  |  _ \  ___ / _(_)_ __ (_) |_(_) ___  _ __  ___ 
# \___ \ / __| '__/ _` | '_ \ / _ \ '__| | | | |/ _ \ |_| | '_ \| | __| |/ _ \| '_ \/ __|
#  ___) | (__| | | (_| | |_) |  __/ |    | |_| |  __/  _| | | | | | |_| | (_) | | | \__ \
# |____/ \___|_|  \__,_| .__/ \___|_|    |____/ \___|_| |_|_| |_|_|\__|_|\___/|_| |_|___/
#                      |_|                                                               
# Many times, you don't even need to write a function when a scraper will do.
# If you did something nifty in the Scrapers tab, just make a new entry here.

def scrapes():
  """Define the functions available and modifiable from the Scrapers tab."""
  s = []
  s.append(['canonical',   'xpath', "/html/head/link[@rel = 'canonical']/@href"])
  s.append(['description', 'xpath', "//meta[translate(@name, 'ABCDEFGHJIKLMNOPQRSTUVWXYZ', 'abcdefghjiklmnopqrstuvwxyz')='description']/@content"])
  s.append(['followers',   'xpath', "//span[.='Followers']/following-sibling::span/text()"])
  s.append(['following',   'xpath', "//span[.='Following']/following-sibling::span/text()"])
  s.append(['ga',          'regex', r"(?:\'|\")(?P<scrape>UA-.*?)(?:\'|\")"])
  s.append(['h1',          'xpath', '//*[self::h1 or self::H1]/text()'])
  s.append(['h2',          'xpath', '//*[self::h2 or self::H2]/text()'])
  s.append(['h3',          'xpath', '//*[self::h3 or self::H3]/text()'])
  s.append(['h4',          'xpath', '//*[self::h4 or self::H4]/text()'])
  s.append(['h5',          'xpath', '//*[self::h5 or self::H5]/text()'])
  s.append(['h6',          'xpath', '//*[self::h6 or self::H6]/text()'])
  s.append(['headlines',   'xpath', '//*[self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6 or self::H1 or self::H2 or self::H3 or self::H4 or self::H5 or self::H6]/text()'])
  s.append(['metakeywords','xpath', "//meta[translate(@name, 'ABCDEFGHJIKLMNOPQRSTUVWXYZ', 'abcdefghjiklmnopqrstuvwxyz')='keywords']/@content"])
  s.append(['mobile',      'xpath', "/html/head/link[@media = 'only screen and (max-width: 640px)']/@href"])
  s.append(['subscribers', 'regex', r"subscriber-count.*?>(?P<scrape>[0-9,]+?)<"])
  s.append(['thumbsdown',  'xpath', "//button[@id='watch-dislike']/span/text()"])
  s.append(['thumbsup',    'xpath', "//button[@id='watch-like']/span/text()"])
  s.append(['title',       'xpath', "//title/text()"])
  s.append(['tweettotal',  'xpath', "//span[.='Tweets']/following-sibling::span/text()"])
  s.append(['views',       'xpath', "//div[@class='watch-view-count']/text()"])
  return s

#  ____                 ___                     _                
# |  _ \ _____      __ |_ _|_ __  ___  ___ _ __| |_ ___ _ __ ___ 
# | |_) / _ \ \ /\ / /  | || '_ \/ __|/ _ \ '__| __/ _ \ '__/ __|
# |  _ < (_) \ V  V /   | || | | \__ \  __/ |  | ||  __/ |  \__ \
# |_| \_\___/ \_/\_/   |___|_| |_|___/\___|_|   \__\___|_|  |___/
#                                                                
# These are the functions that can add new rows, usually using globs.sheet.

def setolinks(url):
  '''Return a list of links from a given url'''
  import lxml.html
  apexdom = apex(url)
  ro = requests.get(url, timeout=5, verify=False)
  if ro.status_code == 200:
    doc = lxml.html.fromstring(ro.text)
    doc.make_links_absolute(url)
    somelinks = doc.xpath('/html/body//a/@href')
    links = set()
    for alink in somelinks:
      if urlparse.urlparse(alink)[1][-len(apexdom):] == apexdom:
        if alink != url:
          links.add(alink)
    links = list(links)
    return links
  else:
    return None

def precrawl(url):
  """Grab HTML from a link, parse links and add a row per link to spreadsheet."""
  fcols = ['linksto', 'depth', 'crawl']
  therange = 'B1:%s2' % globs.letter[len(fcols)+1]
  CellList = globs.sheet.range(therange)
  vals = fcols + [] + [] + []
  for i, val in enumerate(vals): # First, we add the columns we know we're going to need.
    CellList[i].value = val
  globs.sheet.update_cells(CellList)
  links = setolinks(url)
  if links:
    y = len(links)
    linkslist = zip([url]*y, links, ['0']*y, ['?']*y)
    InsertRows(globs.sheet, linkslist, 2)
    return ""
  else:
    return "can't reach"

def crawl(linksto, depth='0'):
  '''Performs second degree crawling from the 1st crawl function. No recursion
  necessary for a shalow crawl.'''
  if linksto and len(linksto) > 3 and linksto[:4] != 'http':
    Stop()
  else:
    links = setolinks(linksto)
    if links:
      y = len(links)
      globs.numrows = len(globs.sheet.col_values(1))
      if depth:
        depth = int(depth) + 1
      linkslist = zip([linksto]*y, links, [depth]*y)
      InsertRows(globs.sheet, linkslist, globs.numrows)
      return "visited"
    else:
      return "can't reach"

def getlinks(url):
  """Grab HTML from a URL, parse links and add a row per link to spreadsheet."""
  fcols = ['Depth', 'Archive', 'Title', 'Description', 'H1', 'H2', 'ExtractKeywords', 'TopKeyword']
  therange = 'B1:%s2' % globs.letter[len(fcols)+1]
  CellList = globs.sheet.range(therange)
  vals = fcols + ['0'] + ['?']*(len(fcols)-1)
  for i, val in enumerate(vals):
    CellList[i].value = val
  globs.sheet.update_cells(CellList)
  apexdom = apex(url)
  import lxml.html
  ro = requests.get(url, timeout=5)
  doc = lxml.html.fromstring(ro.text)
  doc.make_links_absolute(url)
  somelinks = doc.xpath('/html/body//a/@href')
  links = set()
  for alink in somelinks:
    if urlparse.urlparse(alink)[1][-len(apexdom):] == apexdom:
      links.add(alink)
  links = list(links)
  y = len(links)
  q = ['?']*y
  linkslist = zip(links,['1']*y,q,q,q,q,q,q,q)
  InsertRows(globs.sheet, linkslist, 2)
  return "0"

#   ___                         _ ____   ___  _   _      _    ____ ___     
#  / _ \ _ __   ___ _ __       | / ___| / _ \| \ | |    / \  |  _ \_ _|___ 
# | | | | '_ \ / _ \ '_ \   _  | \___ \| | | |  \| |   / _ \ | |_) | |/ __|
# | |_| | |_) |  __/ | | | | |_| |___) | |_| | |\  |  / ___ \|  __/| |\__ \
#  \___/| .__/ \___|_| |_|  \___/|____/ \___/|_| \_| /_/   \_\_|  |___|___/
#       |_|                                                                
# All these have high volume, publically available (no login) endpoints
# meaning they're almost as simple as the Scraper functions.

def tweets(url):
  """Return the number of times a given URL had been tweeted."""
  endpoint = "http://urls.api.twitter.com/1/urls/count.json?url="
  return jsonapi(endpoint, url, 'count')

def stumbles(url):
  """Return the number of times a given URL was viewed in StumbleUpon."""
  endpoint = 'http://www.stumbleupon.com/services/1.01/badge.getinfo?url='
  return jsonapi(endpoint, url, 'views')

def pins(url):
  """Return the number of times a given URL has been pinned in Pinterest."""
  endpoint = 'http://api.pinterest.com/v1/urls/count.json?url='
  return jsonapi(endpoint, url, 'count')

#      _       _     _   ____  _          __  __   _   _               
#     / \   __| | __| | / ___|| |_ _   _ / _|/ _| | | | | ___ _ __ ___ 
#    / _ \ / _` |/ _` | \___ \| __| | | | |_| |_  | |_| |/ _ \ '__/ _ \
#   / ___ \ (_| | (_| |  ___) | |_| |_| |  _|  _| |  _  |  __/ | |  __/
#  /_/   \_\__,_|\__,_| |____/ \__|\__,_|_| |_|   |_| |_|\___|_|  \___|
#                                                                      
# And now what you've all been waiting for! If you write a Python function that
# just works stand-alone elsewhere, simply paste it here to extend Pipulate.

def extractkeywords(url):
  import rake, operator, re
  html = gethtml(url)
  title = scraper(html, '//title/text()')
  description = scraper(html, "//meta[translate(@name, 'ABCDEFGHJIKLMNOPQRSTUVWXYZ', 'abcdefghjiklmnopqrstuvwxyz')='description']/@content")
  from markdown import *
  scrubbed = markdown(html)
  newtxt = "%s %s %s" % (title, description, scrubbed)
  newtxt = newtxt.replace('\n', ' ')
  newtxt = re.sub('<[^<]+?>', ' ', newtxt)
  newtxt = re.sub(' +',' ', newtxt)
  rake_object = rake.Rake("SmartStoplist.txt", 3, 4, 2)
  keywords = rake_object.run(newtxt)
  stackum = ''
  for keyword in keywords:
    candidate = keyword[0].split()
    if len(candidate) > 1:
      stackum += keyword[0] + '\n'
  return stackum

def topkeyword(extractkeywords):
  try:
    kwlist = extractkeywords.split('\n')
    return kwlist[0]
  except:
    return []

def mozsig(expires):
  import hmac, base64
  from hmac import new
  from urllib import quote_plus
  from hashlib import sha1
  from base64 import standard_b64encode
  accessID = globs.config['mozid']
  secretKey = globs.config['mozkey']
  stringToSign = "%s\n%s" % (accessID, expires)
  binarySignature = new(secretKey, stringToSign, sha1).digest()
  textSignature = standard_b64encode(binarySignature)
  urlSafeSignature = quote_plus(textSignature)
  return urlSafeSignature

def mozcall(url, bitmask, label):
  from time import time, sleep
  from urllib import quote_plus
  url = quote_plus(url)
  accessID = globs.config['mozid']
  expires = int(time()) + 3000
  signature = mozsig(expires)
  endpoint =  "http://lsapi.seomoz.com/linkscape/url-metrics/%s?" % (url)
  parameters = "Cols=%s&AccessID=%s&Expires=%s&Signature=%s" % (bitmask, accessID, expires, signature)
  out("Sleeping for 5 seconds (for Moz).")
  sleep(5)
  return jsonapi(endpoint, parameters, label)

def pageauthority(url):
  return mozcall(url, "34359738368", "upa")

def domainauthority(url):
  return mozcall(url, "68719476736", "pda")

def difficulty(keyword):
  if 'semrush' in globs.config:
    apikey = globs.config['semrush']
    try:
      call = 'http://api.semrush.com/?type=phrase_kdi&export_columns=Kd&phrase=%s&key=%s&database=us' % (keyword, apikey)
      respobj = requests.get(call, timeout=5)
      rtext = respobj.text
      out(rtext)
    except:
      return "Double-check your semrush entry in the Config tab."
    try:
      return rtext.splitlines()[1]
    except:
      return "N/A"
  else:
    return "In the Config tab, put semrush under name and the api key under value to proceed."

def rushdifficulty(keyword):
  pp = 50
  try:
    apikey = globs.config['semrush']
  except:
    return "In the Config tab, put semrush under name and the api key under value to proceed."
  funcol = globs.row1.index('rushdifficulty') + 1
  lastq = len(globs.sheet.col_values(funcol))
  mycol = globs.letter[funcol]
  if 'keyword' in globs.row1:
    kwcol = globs.letter[globs.row1.index('keyword') + 1]
    chunks = ['%s%s:%s%s' % (kwcol, chunk, kwcol, chunk+pp-1) for chunk in range(lastq, globs.numrows, pp)]
  else:
    return "You must have a column named keyword."
  if not chunks:
    return "Please use difficulty function instead."
  lastchunk = chunks[-1].split(":")
  lastchunk[1] = "%s%s" % (kwcol, globs.numrows)
  chunks[-1] = "%s:%s" % (lastchunk[0], lastchunk[1])
  for chunk in chunks:
    out("Chunk: %s" % (chunk))
    CellList1 = globs.sheet.range(chunk)
    try:
      CellList2 = globs.sheet.range(chunk.replace(kwcol, mycol))
    except:
      CellList2 = globs.sheet.range(chunk.replace(kwcol, mycol))
    kwlist = []
    for cindex, acell in enumerate(CellList1):
      asciival = acell.value.encode('ascii', errors='ignore')
      kwlist.append(asciival)
    kwstring = ';'.join(kwlist)
    endpoint = "http://api.semrush.com/"
    params = {
      'type': 'phrase_kdi',
      'export_columns': 'Ph,Kd',
      'database': 'us',
      'key': apikey,
      'phrase': kwstring
      } 
    out("Hitting SEMRush API...")
    try:
      respobj = requests.get(endpoint, params=params, timeout=5)
    except:
      Stop()
    resplist = respobj.text.splitlines()
    scoredict = {}
    apair = []
    for scorepair in resplist:
      apair = scorepair.split(';')
      if len(apair) > 1:
        scoredict[str(apair[0])] = str(apair[1])
    for cindex, acell in enumerate(CellList1):
      acell = acell.value.lower()
      if acell in scoredict:
        score = scoredict[acell]
        if not score:
          score = '-1'
        CellList2[cindex].value = score
      else:
        CellList2[cindex].value = '-1'
    globs.sheet.update_cells(CellList2)
    time.sleep(5)
  globs.STOP = True

def volume(keyword):
  if 'semrush' in globs.config:
    apikey = globs.config['semrush']
    try:
      call = 'http://api.semrush.com/?type=phrase_this&export_columns=Nq&phrase=%s&key=%s&database=us' % (keyword, apikey)
      respobj = requests.get(call, timeout=5)
      rtext = respobj.text
      out(rtext)
    except:
      return "Double-check your semrush entry in the Config tab."
    try:
      return rtext.splitlines()[1]
    except:
      return "N/A"
  else:
    return "In the Config tab, put semrush under name and the api key under value to proceed."

def twitter_followers(twitter_name):
  api = 'https://twitter.com/'
  un = twitter_name
  if un.lower().strip() in ('na', 'n/a'):
    return un
  if un[0] == '@':
    un = un[1:]
  url = "%s%s" % (api, un)
  xpath = "//span[.='Followers']/following-sibling::span/text()"
  sendback = scraper(url, xpath)
  if ',' in sendback:
    sendback = sendback.replace(',', '')
  return sendback

def instagram_followers(instagram_name):
  api = 'https://instagram.com/'
  un = instagram_name
  if un.lower().strip() in ('na', 'n/a'):
    return un
  if un[0] == '@':
    un = un[1:]
  url = "%s%s" % (api, un)
  #pattern = 'followed_by":{"count":(?P<scrape>\d+)}'
  pattern = r'(followed_by":{"count":)(?P<scrape>\d+)}'
  sendback = regex(url, pattern)
  return sendback

def serps(keyword):
  """Return non-customized JSON search results for keyword from Google."""
  times = 6
  api = "http://ajax.googleapis.com/ajax/services/search/web"
  returnme = []
  for start in [8*n for n in range(0,times)]:
    pdict = {'rsz':'large', 'v':'1.0', 'q': keyword, 'start':start}
    respobj = requests.get(api, params=pdict, timeout=5)
    returnme.append(respobj.json())
    time.sleep(1)
  return json.dumps(returnme)

def positions(keyword, serps=''):
  """Return a position/url paired JSON dict of all results for keyword."""
  if not serps:
    def gserps(keyword):
      global serps
      return serps(keyword)
    serps = gserps(keyword)
  elif serps:
    serps = json.loads(serps)
    easydict = {}
    serpos = 1
    rd = serps[0]["responseData"]
    if rd == None:
      return "API quota likely exceeded"
    for serpage in serps:
      try:
        serpage = serpage["responseData"]["results"]
        for result in serpage:
          easydict[serpos] = result['url']
          serpos += 1
      except:
        pass
    return json.dumps(easydict)
  else:
    return "Error"

def topurl(site, positions=''):
  """Return the top performing URL for a site given a positions object."""
  if positions:
    urldict = json.loads(positions)
    for thepos, aurl in urldict.iteritems():
      if site in aurl:
        return aurl

def foundurl(lookforurl, positions=''):
  """Return a looked-for URL, given a positions object."""
  if positions:
    urldict = json.loads(positions)
    for thepos, aurl in urldict.iteritems():
      if lookforurl.lower() == aurl.lower():
        return aurl

def position(keyword, site, positions=''):
  """Return the position a provided site is in for a given keyword."""
  if not positions:
    def gpositions(keyword):
      global positions
      return positions(keyword)
    positions = gpositions(keyword)
  elif positions:
    urldict = json.loads(positions)
    for thepos, aurl in urldict.iteritems():
      if site in aurl:
        return thepos

def inposition(keyword, lookforurl, positions=''):
  """Return the position a provided lookforurl is in for a given keyword."""
  if not positions:
    def gpositions(keyword):
      global positions
      return positions(keyword)
    positions = gpositions(keyword)
  elif positions:
    urldict = json.loads(positions)
    for thepos, aurl in urldict.iteritems():
      if lookforurl.lower() == aurl.lower():
        return thepos

def response(url):
  """Return a numeric http response code for given URL."""
  if globs.hobj:
    return globs.hobj.status_code
  else:
    try:
      return requests.get(url, timeout=5).status_code
    except:
      return "Error"

def plusses(url):
  """Return the number of times the given URL was plussed in Google+"""
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

def fb(url):
  """Return Facebook likes, shares, clicks and comment counts for a given URL."""
  thecall = "https://graph.facebook.com/fql?q=SELECT+like_count,total_count,share_count,click_count,comment_count+FROM+link_stat+WHERE+url=%22"+url+"%22"
  jobj = requests.get(thecall).json()
  return json.dumps(jobj)

def shares(url, fb=''):
  """Return the number of times a given URL was shared in Facebook."""
  if not fb:
    def gfb(url):
      global fb
      return fb(url)
    fb = json.loads(gfb(url))
  else:
    fb = json.loads(fb)
  return walkdict(fb, "share_count")

def likes(url, fb=''):
  """Return the number of times a given URL was liked in Facebook."""
  if not fb:
    def gfb(url):
      global fb
      return fb(url)
    try:
      fb = json.loads(gfb(url))
    except:
      return "Error"
  else:
    try:
      fb = json.loads(fb)
    except:
      return "Error"
  if 'data' in fb:
    return walkdict(fb['data'][0], "like_count")
  else:
    return "Error"

def comments(url, fb=''):
  """Return the number of times a URL was commented on in Facebook."""
  if not fb:
    def gfb(url):
      global fb
      return fb(url)
    fb = json.loads(gfb(url))
  else:
    fb = json.loads(fb)
  return walkdict(fb, "comment_count")

def linkedin(url):
  """Return the number of times a given URL was shared in LinkedIn."""
  api = "https://www.linkedin.com/countserv/count/share?url=" + url
  respobj = requests.get(api, timeout=5)
  rtext = respobj.text
  spattern = '"count":(?P<scrape>[0-9,]+?),'
  return regex(rtext, spattern)

def pagerank(url):
  """Return the PageRank number that would show for this URL in Google Toolbar."""
  import urllib
  def CheckHash(HashInt):
    HashStr = "%u" % (HashInt)
    Flag = 0
    CheckByte = 0
    i = len(HashStr) - 1
    while i >= 0:
      Byte = int(HashStr[i])
      if 1 == (Flag % 2):
        Byte *= 2;
        Byte = Byte / 10 + Byte % 10
      CheckByte += Byte
      Flag += 1
      i -= 1
    CheckByte %= 10
    if 0 != CheckByte:
      CheckByte = 10 - CheckByte
      if 1 == Flag % 2:
        if 1 == CheckByte % 2:
          CheckByte += 9
        CheckByte >>= 1
    return '7' + str(CheckByte) + HashStr
  def HashURL(Str):
    def  IntStr(String, Integer, Factor):
      for i in range(len(String)) :
        Integer *= Factor
        Integer &= 0xFFFFFFFF
        Integer += ord(String[i])
      return Integer
    C1 = IntStr(Str, 0x1505, 0x21)
    C2 = IntStr(Str, 0, 0x1003F)
    C1 >>= 2
    C1 = ((C1 >> 4) & 0x3FFFFC0) | (C1 & 0x3F)
    C1 = ((C1 >> 4) & 0x3FFC00) | (C1 & 0x3FF)
    C1 = ((C1 >> 4) & 0x3C000) | (C1 & 0x3FFF)
    T1 = (C1 & 0x3C0) << 4
    T1 |= C1 & 0x3C
    T1 = (T1 << 2) | (C2 & 0xF0F)
    T2 = (C1 & 0xFFFFC000) << 4
    T2 |= C1 & 0x3C00
    T2 = (T2 << 0xA) | (C2 & 0xF0F0000)
    return (T1 | T2)
  hsh = CheckHash(HashURL(url))
  gurl = 'http://toolbarqueries.google.com/tbr?client=navclient-auto&features=Rank:&q=info:%s&ch=%s' % (urllib.quote(url), hsh)
  f = urllib.urlopen(gurl)
  st = f.read()
  st = st.lstrip().rstrip()
  st = st[9:]
  try:
    st = int(st)
  except:
    st = 0
  return st

def mcanonical(mobile):
  """Return the canonical tag found in the URL referred to by under the mobile column."""
  try:
    ro = requests.get(mobile, timeout=5)
    text = ro.text
    xpth = "/html/head/link[@rel = 'canonical']/@href"
    revcon = scraper(text, xpth)
    return revcon
  except:
    return None

def mobilicious(url, mobile, mcanonical):
  """Compare the URL of desktop version with the mobile canonical and return Pass if the same."""
  if mobile:
    if url == mcanonical:
      return "Pass"
    else:
      return "Fail"
  else:
    return "Fail"

def sheetinitializer(sheet1key):
  """ For any given menu-selection, return lists to become row 1 and 2."""
  sinit = {}
  sinit['crawl'] = (['source', 'crawl'], [globs.PIPURL, '?'])
  return sinit[sheet1key]

def cancel():
  globs.STOP = True

def length(archive):
  return len(archive)

def makeview(viewname):
  import base64, bz2
  from uuid import uuid4
  compressed = bz2.compress(sampleData())
  cellfriendly = base64.b64encode(compressed)
  mygid = uuid4()
  rowdict = {
    'sharelink': 'http://%s/v?k=%s&v=%s' % (globs.HOST, globs.DOCID, mygid),
    'datestamp': datestamp(), 
    'guid': mygid, 
    'includecode': '<script src="http://js.cytoscape.org/js/cytoscape.min.js"></script>',
    'compresseddata': cellfriendly
    }
  return 'made', rowdict

def status(recurrence, whetherdue):
  if whetherdue == 'FALSE':
    return '[N/A]'
  elif whetherdue == 'TRUE':
    return "[Is it done?]"

def sampleData():

  sheet1 = globs.gdoc.sheet1
  row1 = lowercaselist(sheet1.row_values(1))
  fromurldex = row1.index('url') + 1
  linkstodex = row1.index('linksto') + 1
  fromurl = sheet1.col_values(fromurldex)
  linksto = sheet1.col_values(linkstodex)
  edgetuples = zip(fromurl, linksto)
  nodes = ''
  for aurl in set(fromurl):
    if aurl != 'url':
      nodes = nodes + "{ data: { id: '%s', name: '%s'} },\n" % (aurl, aurl)
  nodes = nodes[:-2]
  edges = ''
  for atuple in edgetuples:
    if atuple[0] != 'url':
      edges = edges + "{ data: { source: '%s', target: '%s' } },\n" % (atuple[0], atuple[1])
  edges = edges[:-2]

  xnodes = '''{ data: { id: 'j', name: 'j'} },
             { data: { id: 'e', name: 'e'} },
             { data: { id: 'k', name: 'k'} },
             { data: { id: 'g', name: 'g'} }'''

  xedges = '''{ data: { source: 'j', target: 'e' } },
        { data: { source: 'j', target: 'k' } },
        { data: { source: 'j', target: 'g' } },
        { data: { source: 'e', target: 'j' } },
        { data: { source: 'e', target: 'k' } },
        { data: { source: 'k', target: 'j' } },
        { data: { source: 'k', target: 'e' } },
        { data: { source: 'k', target: 'g' } },
        { data: { source: 'g', target: 'j' } }'''

  return '''$(function(){ // on dom ready

  $('#cy').cytoscape({
    style: cytoscape.stylesheet()
      .selector('node')
        .css({
          'content': 'data(name)',
          'text-valign': 'center',
          'color': 'white',
          'text-outline-width': 2,
          'text-outline-color': '#888'
        })
      .selector('edge')
        .css({
          'target-arrow-shape': 'triangle'
        })
      .selector(':selected')
        .css({
          'background-color': 'black',
          'line-color': 'black',
          'target-arrow-color': 'black',
          'source-arrow-color': 'black'
        })
      .selector('.faded')
        .css({
          'opacity': 0,
          'text-opacity': 0.25
        }),
    
    elements: {
      nodes: [
        %s
      ],
      edges: [
        %s 
      ]
    },
    
    layout: {
      name: 'breadthfirst',
      padding: 10,
      strictHierarchy: true,
      avoidOverlap: true
    },
    
    // on graph initial layout done (could be async depending on layout...)
    ready: function(){
      window.cy = this;
      
      // giddy up...
      
      cy.elements().unselectify();
      
      cy.on('tap', 'node', function(e){
        var node = e.cyTarget; 
        var neighborhood = node.neighborhood().add(node);
        
        cy.elements().addClass('faded');
        neighborhood.removeClass('faded');
      });
      
      cy.on('tap', function(e){
        if( e.cyTarget === cy ){
          cy.elements().removeClass('faded');
        }
      });
    }
  });

  }); // on dom ready''' % (nodes, edges)
