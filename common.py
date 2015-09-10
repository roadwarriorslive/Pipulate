#   ____                                        __  __           _       _      
#  / ___|___  _ __ ___  _ __ ___   ___  _ __   |  \/  | ___   __| |_   _| | ___ 
# | |   / _ \| '_ ` _ \| '_ ` _ \ / _ \| '_ \  | |\/| |/ _ \ / _` | | | | |/ _ \
# | |__| (_) | | | | | | | | | | | (_) | | | | | |  | | (_) | (_| | |_| | |  __/
#  \____\___/|_| |_| |_|_| |_| |_|\___/|_| |_| |_|  |_|\___/ \__,_|\__,_|_|\___|
#                                                                               
#                         In every job that must be done,
#                           There is an element of fun.
#                   You find the fun and snap, the job's a game
#                          And every task you undertake
#                            Becomes a piece of cake...

import globs

class Credentials (object):
  def __init__ (self, access_token=None):
    self.access_token = access_token

def freshtoken(picklefile):
  import pickle
  from datetime import datetime, timedelta
  tdict = pickle.load(open(picklefile, "rb"))
  token = tdict['access_token']
  expires = tdict['expires']
  thetime = datetime.now()
  if thetime > expires:
    endpoint = "https://www.googleapis.com/oauth2/v3/token" # Note to self: research the v3 endpoint.
    configfile = open(globs.FILE, 'rb')
    lines = configfile.readlines()
    configfile.close()
    config = {}
    for item in lines:
      parts = item.split()
      config[parts[0]] = parts[2][1:-1]
    postheaders = {
      'client_id': config['CLIENT_ID'],
      'client_secret': config['CLIENT_SECRET'],
      'refresh_token': config['REFRESH_TOKEN'],
      'grant_type': 'refresh_token'
      }
    import requests
    r = requests.post(endpoint, postheaders)
    rd = r.json()
    xseconds = rd['expires_in']
    expiresin = datetime.now() + timedelta(seconds=xseconds)
    pickleme = {
      'access_token': rd['access_token'],
      'expires': expiresin
    }
    pickle.dump(pickleme, open(globs.TOKEN, 'wb'))
  else:
    return token

def out(msg, symbol='', dent=''):
  """Return message as command line debug output when in debug mode."""
  total = 80
  if globs.DBUG:
    if symbol:
      half = ((total-1 - len(msg)) / 2) - 2
      side = half*symbol
      msg = "%s << %s >> %s" % (side, msg, side)
      tmpmsg = ''
      if dent:
        tmpmsg = msg[len(globs.nest)-2:total-1]
        print(globs.nest)
        globs.nest = globs.nest[:-2]
      else:
        print(globs.nest)
      if symbol == '0':
        tmpmsg = msg[len(globs.nest):total]
        print("%s%s" % (globs.nest, tmpmsg))
      else:
        tmpmsg = msg[len(globs.nest):total-1]
        print("%s %s" % (globs.nest, tmpmsg))
      if not dent:
        if symbol == '0':
          globs.nest = symbol
        else:
          globs.nest = '%s %s' % (globs.nest, symbol)
      print(globs.nest)
    else:
      print("%s |%s" % (globs.nest, msg))

def Stop():
  """Stops Iterating, usually used in looping Pipulate function."""
  print('''
                            ____  _              _ 
                           / ___|| |_ ___  _ __ | |
                           \___ \| __/ _ \| '_ \| |
                            ___) | || (_) | |_) |_|
                           |____/ \__\___/| .__/(_)
                                          |_|      
  ''')
  if globs.WEB:
    #raise StopIteration('Forcing STOP with Stop()')
    raise SystemExit('Forcing STOP with Stop()')
  else:
    pass

def gotcha(x=''):
  """Use to progressively zero in on return value issues."""
  print('''
                   ____       _       _             _   _   _ 
                  / ___| ___ | |_ ___| |__   __ _  | | | | | |
                 | |  _ / _ \| __/ __| '_ \ / _` | | | | | | |
                 | |_| | (_) | || (__| | | | (_| | |_| |_| |_|
                  \____|\___/ \__\___|_| |_|\__,_| (_) (_) (_)
  ''')
  if x:
    if type(x) == list or type(x) == dict or type(x) == tuple:
      import pprint
      print("\n")
      pprint.pprint(x)
      print("\n")
    else:
      out("Gotcha !!! %s !!! </%s>" % (x, globs.nest[-1:]))
  else:
    out("Gotcha!!! </%s>" % globs.nest[-1:])
  globs.nest = globs.nest[:-2]
  if x:
    raise RuntimeError('Forcing STOP with Gotcha: %s' % x)
  else:
    raise RuntimeError('Forcing STOP with Gotcha')

def InsertRows(onesheet, listoflists, lastrowused=''):
  """Inserts a list-of-lists as rows into spreadsheet from lastrowused."""
  numnewrows = len(listoflists)
  if not lastrowused:
    lastrowused = globs.numrows
  numrowsneeded = len(listoflists)
  allrowsevenempty = onesheet.row_count
  availableblankrows = allrowsevenempty - lastrowused
  if availableblankrows < numrowsneeded:
    rowstoadd = numrowsneeded - availableblankrows
    onesheet.add_rows(rowstoadd)
    globs.numrows += rowstoadd
  upperleftrangenumber = lastrowused + 1
  lowerrightrangenumber = lastrowused + numnewrows
  column = globs.letter[len(listoflists[0])]
  rowrange = "A%s:%s%s" % (upperleftrangenumber, column, lowerrightrangenumber)
  flattenitlist = []
  for onelist in listoflists:
    for onecell in onelist:
      flattenitlist.append(onecell)
  flattenitlist = ['?' if x=='*' else x for x in flattenitlist]
  stop = True
  for x in range(5):
    try:
      CellList = onesheet.range(rowrange)
      stop = False
      break
    except:
      out("Retry %s of %s" % (x, 5))
      time.sleep(5)
  if stop:
    Stop()
  for index, onecell in enumerate(CellList):
    try:
      onecell.value = flattenitlist[index]
    except:
      pass
  for x in range(5):
    try:
      onesheet.update_cells(CellList)
      stop = False
      break
    except:
      out("Retry %s of %s" % (x, 5))
      time.sleep(5)
  if stop:
    Stop()
  return

def apex(url):
  """Usually returns the apex or registered domain, given a URL."""
  from urlparse import urlparse
  if url:
    apex = urlparse(url).hostname.split(".")
    try:
      apex = ".".join(len(apex[-2]) < 4 and apex[-3:] or apex[-2:])
      return apex
    except:
      return None
  else:
    return None

def checkurl(url):
  import re
  regex = re.compile(
    r'^https?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
  return url is not None and regex.search(url)

def lowercaselist(onelist):
  for index, item in enumerate(onelist):
    try:
      onelist[index] = item.lower().strip()
    except:
      pass
  return onelist

def timestamp():
  '''Return current date in simple format.'''
  import datetime
  i = datetime.datetime.now()
  return i.strftime("%m/%d/%Y %H:%M:%S")

def datestamp():
  'Return current time and date in time-trending-friendly format.'
  import datetime
  now = datetime.datetime.now()
  now = now.strftime("%B %d, %Y")
  return now

