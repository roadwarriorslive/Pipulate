from flask import session
from common import *

def documentation():
  s = []
  s.append(['Canonical',            'Crawl',     'Url',                       'Return Canonical.', ''])
  s.append(['Comments',             'Facebook',  'Url',                       'Return Facebook count.', ''])
  s.append(['Crawl',                'Crawl',     'Url',                       'Make one row per link found on url, setting stage for Crawl2', ''])
  s.append(['Crawl2',               'Crawl',     'Target',                    'Make one row per link found on target, as set up by Crawl', ''])
  s.append(['Description',          'Crawl',     'Url',                       'Return meta description.', ''])
  s.append(['Difficulty',           'Keyword',   'Keyword',                   'Return SEMRush Keyword Difficulty.', ''])
  s.append(['DomainAuthority',      'MOZ',       'Url',                       'Return Moz Domain Authority score for a URL.', ''])
  s.append(['Fb',                   'Facebook',  'Url',                       'Return Facebook likes, shares, clicks and comments as JSON.', ''])
  s.append(['Followers',            'Twitter',   'Url',                       'Return Twitter followers count.', ''])
  s.append(['Following',            'Twitter',   'Url',                       'Return Twitter following count.', ''])
  s.append(['Ga',                   'Crawl',     'Url',                       'Return Google Analytics ID to check if GA installed on page.', ''])
  s.append(['GetLinks',             'Crawl',     'Url',                       'Return list of links found on page. Adds rows.', ''])
  s.append(['Instagram_Followers',  'Social',    'Instagram_Name',            'Return Instagram Followers count.', ''])
  s.append(['JsonApi',              'Generic',   'Endpoint, Url, Jkey',       "Return response code from any JSON API that doesn't require login.", ''])
  s.append(['Likes',                'Facebook',  'Url',                       'Return Facebook likes for given URL.', ''])
  s.append(['Mcanonical',           'Mobile',    'Canonical',                 'Return the canoncial tag from URL found in mobile column (used for mobile audits)', ''])
  s.append(['Mobile',               'Mobile',    'Url',                       '', ''])
  s.append(['Mobilicious',          'Mobile',    'Url, Mobile, Mcanonical',   '', ''])
  s.append(['PageAuthority',        'MOZ',       'Url',                       'Return Moz Page Authority score for a URL.', ''])
  s.append(['Pins',                 'Social',    'Url',                       '', ''])
  s.append(['Plusses',              'Social',    'Url',                       '', ''])
  s.append(['Position',             'Serps',     'Keyword, (Serps)',          '', ''])
  s.append(['Positions',            'Serps',     'Keyword, Site, (Positions)','', ''])
  s.append(['Redirect_Chain',       'Crawl',     'Url',                       '', ''])
  s.append(['RegEx',                'Crawl',     'Text, Pattern',             '', ''])
  s.append(['Response',             'Crawl',     'Url',                       '', ''])
  s.append(['RushDifficulty',       'Keyword',   'Keyword',                   'Return SEMRush Keyword Difficulty, batched. Processes 50 at a time. Only first question mark required.', ''])
  s.append(['Serps',                'Keyword',   'Keyword',                   '', ''])
  s.append(['Shares',               'Facebook',  'Url',                       '', ''])
  s.append(['Stumbles',             'Social',    'Url',                       '', ''])
  s.append(['Subscribers',          'YouTube',   'Url',                       '', ''])
  s.append(['ThumbsDown',           'YouTube',   'Url',                       '', ''])
  s.append(['ThumbsUp',             'YouTube',   'Url',                       '', ''])
  s.append(['Title',                'Crawl',     'Url',                       '', ''])
  s.append(['TopUrl',               'Serps',     'Site, (Positions)',         '', ''])
  s.append(['TweetTotal',           'Twitter',   'Url',                       '', ''])
  s.append(['Tweets',               'Twitter',   'Url',                       '', ''])
  s.append(['Twitter_Followers',    'Twitter',   'Twitter_Name',              '', ''])
  s.append(['Views',                'YouTube',   'url',                       '', ''])
  s.append(['Volume',               'Keyword',   'Keyword',                   'Return SEMRush Keyword Volume.', ''])
  return s

def crawlchoices():
  return [
    ('spam', 'Spam'),
    ('eggs', 'Eggs'),
    ('foo', 'Foo'),
    ('bar', 'Bar')
  ]

from flask_wtf import Form
from wtforms import (StringField,
                    RadioField,
                    HiddenField, 
                    SelectMultipleField,
                    TextAreaField,
                    SelectField, 
                    widgets)

class ConfigForm(Form):
  """Define form for aquiring configuration values."""
  import binascii, os
  apdef = binascii.hexlify(os.urandom(24))
  appsecret = StringField('Flask app secret (auto-generated):', default=apdef)
  clientid = StringField('Client ID (from Google Dev Console):')
  clientsecret = StringField('Client secret (from Google Dev Console):')

class PipForm(Form):
  """Define form for main Pipulate user interface."""
  pipurl = StringField('Paste a Google Sheet URL:')
  magicbox = TextAreaField("magicbox")
  options = SelectField("options")

class PipForm2(PipForm):
  """Define form for interstitial options"""
  secondary = HiddenField()

class ClearSheet1(PipForm2):
  radios = RadioField(choices=[
    ('clear', 'Yes, clear Sheet 1.'),
    ('cancel', 'Cancel')
    ])

class CrawlTypes(PipForm2):
  radios = RadioField(choices=[
    ('crawl1', 'Crawl Depth 1'),
    ('crawl2', 'Crawl Depth 2'),
    ('cancel', 'Cancel')
    ])

class AnotherMenu(PipForm2):
  radios = RadioField(choices=crawlchoices())
  checks = SelectMultipleField(choices=crawlchoices(),
    option_widget=widgets.CheckboxInput(),
    widget=widgets.ListWidget(prefix_label=False))

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

def menumaker():
  ''' Creates the entire cadence of the system.'''
  menu = [
  ('menu:clear' , "Clear Sheet 1"),
  ('menu:crawl' , "Crawl Website"),
  ('menu:cols'  , "Add Columns"),
  ('qmarks'     , "Replace ?'s"),
  ('menu:setup' , "Auto Setup"),
  ('menu:graph' , "See Visualization"),
  ('keywords'   , "Harvest Keywords")
  ]
  strmenu = '<option value="off">What do you want to do?</option>\n'
  for item in menu:
    strmenu += '<option value="%s">%s</options>\n' % (item[0], item[1])
  return strmenu

