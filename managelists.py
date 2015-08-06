from flask import session
from common import *

def documentation():
  s = []
  s.append(['',''])
  s.append(['Learn to use Pipulate in 5 easy steps.', ''])
  s.append(['1: ', ''])
  s.append(['2: ', ''])
  s.append(['3: ', ''])
  s.append(['4: ', ''])
  s.append(['5: ', ''])
  s.append(['',''])
  s.append(["ADDITIONAL RESOURCES:",''])
  s.append(['Watch A High-level Google Slides Intro -->', 'http://goo.gl/QPQb3t'])
  s.append(['Read Main Documentation at Github -->', 'http://goo.gl/IOHjTJ'])
  s.append(['Watch YouTube Video Tutorials -->', 'http://goo.gl/Nh3z7U'])
  s.append(['',''])
  s.append(["EASTER EGGS:",''])
  s.append(['Get List-of-Functions Tab -->',''])
  s.append(['Get JSON API Tab -->',''])
  return s

def dontgetfrustrated(x):
  s = []
  s.append("Heavy traffic on the Inter-Webs tonight.")
  s.append("I feel your pain. Have patience while I re-try.")
  s.append("You know, it's a miracle this is working at all.")
  s.append("The Google Data API is being uncooperative.")
  s.append("Tap, tap, tap, tap, tap, tap, tap...")
  s.append("Sometimes, you just gotta know when to call it quits.")
  s.append("This could take a moment. Check Facebook or something.")
  s.append("I know your time is valuable. I'm not ignoring you.")
  s.append("Google, I'm talking to you. Is anybody home?")
  s.append("I don't like this any more than you do.")
  return 'stormyweather',s[x%len(s)],'',''

def cyclemotto():
  try:
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
    s.append("Capture FB Likes & Shares, Google Pluses, Authority and more.")
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
  except:
    return ['Configuring']

#  ____  _               _     ___       _ _   _       _ _                  
# / ___|| |__   ___  ___| |_  |_ _|_ __ (_) |_(_) __ _| (_)_______ _ __ 
# \___ \| '_ \ / _ \/ _ \ __|  | || '_ \| | __| |/ _` | | |_  / _ \ '__/
#  ___) | | | |  __/  __/ |_   | || | | | | |_| | (_| | | |/ /  __/ |
# |____/|_| |_|\___|\___|\__| |___|_| |_|_|\__|_|\__,_|_|_/___\___|_|
#                                                                           

def menumaker(url='', keywords=False):
  import urlparse
  """ For any given URL, return a what-to-do-next menu-key."""
  key = ''
  menu = {
  'clear':        "Clear sheet1 (initialize)",
  'crawl':        "1-Page Crawl",
  'keywords':     'Collect Keywords',
  'qm':           "Replace Question Marks"
  }
  if url:
    if keywords and keywords.strip() != '':
      key = 'keywords'
    elif url == 'sheets':
      key = 'sheets'
    elif url == 'seo':
      key = 'seo'
    else:
      apexdom = apex(url)
      urlparts = urlparse.urlparse(url)
      netloc = urlparts[1]
      path = urlparts[2]
      query = urlparts[4]
      key = 'seo'
  else:
    key = 'seo'
  mdict = {}
  mdict['keywords'] = [menu['keywords']]
  mdict['sheets'] =   [
                      menu['qm'],
                      menu['clear'], 
                      menu['crawl'],
                      menu['keywords']
                      ]
  mdict['seo'] =      [
                      menu['qm'],
                      menu['crawl'],
                      menu['clear'], 
                      menu['keywords']
                      ]
  optlist = mdict[key]
  cgimenu = '<option value="off">What do you want to do?</option>\n'
  invmenu = {v: k for k, v in menu.items()}
  for option in optlist:
    cgimenu += '<option value="%s">%s</options>\n' % (invmenu[option], option)
  return cgimenu

