from flask import session
from common import *

def documentation():
  s = []
  s.append(['Archive'  ,            'Crawl',     'Url',                       "Return an archived version of the page's URL. Scrapers can work against archive column.", ''])
  s.append(['Canonical',            'Crawl',     'Url',                       'Return Canonical.', ''])
  s.append(['Comments',             'Facebook',  'Url',                       'Return Facebook count.', ''])
  s.append(['Crawl',                'Crawl',     'LinksTo',                   'Make one row per link found on target, as set up by PreCrawl.', ''])
  s.append(['DateStamp',            'Time',      '',                          'Return current date only in easy to read format. Good for oncce/day tasks.', ''])
  s.append(['Description',          'Crawl',     'Url',                       'Return meta description.', ''])
  s.append(['Difficulty',           'Keyword',   'Keyword',                   'Return SEMRush Keyword Difficulty.', ''])
  s.append(['DomainAuthority',      'MOZ',       'Url',                       'Return Moz Domain Authority score for a URL.', ''])
  s.append(['Fb',                   'Facebook',  'Url',                       'Return Facebook likes, shares, clicks and comments as JSON.', ''])
  s.append(['Followers',            'Twitter',   'Url',                       'Return Twitter followers count.', ''])
  s.append(['Following',            'Twitter',   'Url',                       'Return Twitter following count.', ''])
  s.append(['Ga',                   'Crawl',     'Url',                       'Return Google Analytics ID to check if GA installed on page.', ''])
  s.append(['GetLinks',             'Crawl',     'Url',                       'Return list of links found on page. Adds rows.', ''])
  s.append(['Archive',              'Crawl',     'Url',                       'Return full html of page, zlib compressand and base64 encoded for spreadsheet cell-friendliness.', ''])
  s.append(['Instagram_Followers',  'Social',    'Instagram_Name',            'Return Instagram Followers count.', ''])
  s.append(['JsonApi',              'Generic',   'Endpoint, Url, Jkey',       "Return response code from any JSON API that doesn't require login.", ''])
  s.append(['Likes',                'Facebook',  'Url',                       'Return Facebook likes for given URL.', ''])
  s.append(['Mcanonical',           'Mobile',    'Canonical',                 'Return the canoncial tag from URL found in mobile column (used for mobile audits)', ''])
  s.append(['Mobile',               'Mobile',    'Url',                       'Return link tag URL that should be show for screens less than 640px.', ''])
  s.append(['Mobilicious',          'Mobile',    'Url, Mobile, Mcanonical',   'Return Pass or Fail depending on whether Mobile and Mobilecanonical match.', ''])
  s.append(['PageAuthority',        'MOZ',       'Url',                       'Return Moz Page Authority score for a URL.', ''])
  s.append(['Pins',                 'Social',    'Url',                       'Not yet implemented.', ''])
  s.append(['Plusses',              'Social',    'Url',                       'Return Google Plus count on a URL.', ''])
  s.append(['Position',             'Serps',     'Keyword, Site, (Serps)',    'Return the actual position for a given site for a given keyword.', ''])
  s.append(['Positions',            'Serps',     'Keyword, (Positions)',      'Return all the SERP positions as easily readable JSON for a given keyword.', ''])
  s.append(['PreCrawl',             'Crawl',     'Url',                       'Make one row per link found on url, setting stage for Crawl.', ''])
  s.append(['Redirect_Chain',       'Crawl',     'Url',                       'Not yet implemented', ''])
  s.append(['RegEx',                'Crawl',     'Text, Pattern',             'Return matched group named (?P<scrape>blah) given text and pattern.', ''])
  s.append(['Response',             'Crawl',     'Url',                       'Return http response code from fetching given URL.', ''])
  s.append(['RushDifficulty',       'Keyword',   'Keyword',                   'Return SEMRush Keyword Difficulty, batched. Processes 50 at a time. Only first question mark required.', ''])
  s.append(['Serps',                'Keyword',   'Keyword',                   'Return a JSON snapshot of the underlying non-modified positions.', ''])
  s.append(['Setolinks',            'Crawl',     'Url',                       'Return a list of URLs (in JSON format) found on the given a URL.', ''])
  s.append(['Shares',               'Facebook',  'Url',                       'Return Facebook share count for a URL.', ''])
  s.append(['Stumbles',             'Social',    'Url',                       'Return Stumbles count for a URL.', ''])
  s.append(['Subscribers',          'YouTube',   'Url',                       'Return Subscriber count for a YouTube channel URL.', ''])
  s.append(['ThumbsDown',           'YouTube',   'Url',                       'Return Thumbs-Up count for a YouTube video URL.', ''])
  s.append(['ThumbsUp',             'YouTube',   'Url',                       'Return Thumbs-Down count for a YouTube video URL.', ''])
  s.append(['TimeStamp',            'Time',      '',                          'Return current time and date, very useful for time-trend graphs.', ''])
  s.append(['Title',                'Crawl',     'Url',                       'Return Title tag value for a URL.', ''])
  s.append(['TopUrl',               'Serps',     'Site, (Positions)',         'Return URL-from-site in top position for a keyword and site.', ''])
  s.append(['TweetTotal',           'Twitter',   'Url',                       'Return Twitter total-tweet count for a Twitter profile URL.', ''])
  s.append(['Tweets',               'Twitter',   'Url',                       'Return Twitter tweet-count for a URL.', ''])
  s.append(['Twitter_Followers',    'Twitter',   'Twitter_Name',              'Return Twitter follower count for a Twitter profile URL.', ''])
  s.append(['Views',                'YouTube',   'url',                       'Return YouTube view count for a YouTube video URL.', ''])
  s.append(['Volume',               'Keyword',   'Keyword',                   'Return SEMRush Keyword Volume.', ''])
  return s

def seedkeywordlist():
  return [
    ('Keyword', 'Source', 'Volume', 'Difficulty', 'Priority', 'SERPs')
  ] + [''*6]*30

def expansionkeywordlist():
  return [
    ('Keyword', 'Source', 'Volume', 'Difficulty', 'Priority', 'Categories')
  ]

def keywordbuildchecklist():
  return [
    ('Phase',       'Task',                             'Status', 'Notes'),
    ('Discovery',   'Interview Client',                 '',       ''),
    ('Discovery',   "Crawl Client's Site",              '',       ''),
    ('Discovery',   "Get Analytics Logins",             '',       ''),
    ('Discovery',   "Competitors Identified by Client", '',       ''),
    ('Discovery',   "Client Identified Competitors",    '',       ''),
    ('Seeding',     "SERP-identified Competitors",      '',       ''),
    ('Seeding',     "Crawl Competitor Sites",           '',       ''),
    ('Seeding',     "Harvest Wikipedia Pages",          '',       ''),
    ('Seeding',     "Harvest PDFs and Other",           '',       ''),
    ('Expansion',   "Identify Best Seed Keywords",      '',       ''),
    ('Expansion',   "Google Keyword Planner",           '',       ''),
    ('Expansion',   "Google Suggest API",               '',       ''),
    ('Expansion',   "Proprietary Tool 1 (BrightEdge)",  '',       ''),
    ('Expansion',   "Proprietary Tool 2 (SEMRush)",     '',       ''),
    ('Quantify',    "Combine and Preserve Datapoints",  '',       ''),
    ('Quantify',    "Fill-in Missing Search Volumes",   '',       ''),
    ('Quantify',    "Fill-in Difficulty Scores",        '',       ''),
    ('Quantify',    "Stem Term Analysis",               '',       ''),
    ('Portfolio',   "Bucket by Category",               '',       ''),
    ('Portfolio',   "Frame Discussion in Spreadsheet",  '',       ''),
    ('Portfolio',   "Prioritize With Client",           '',       ''),
    ('Portfolio',   "Complete Prioritization",          '',       ''),
    ('Portfolio',   "Recommend Portfolio",              '',       ''),
    ('Portfolio',   "Refine With Client",               '',       ''),
    ('Portfolio',   "Setup Tracking",                   '',       '')
  ]

def seochecklistlist():
  return [
    ('DateStamp', 'Category',    'Task',                     'Phase', 'StartDate', 'Recurrence', 'WhetherDue', 'Status', 'Notes'),
    (datestamp(), 'Reports',     'Monthly',                  '2',     '',          'True',       'True',       '?',      ''),
    (datestamp(), 'Reports',     'UXReport',                 '2',     '',          'True',       'True',       '?',      ''),
    (datestamp(), 'Onboarding',  'Setup Project Management', '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Onboarding',  'Conduct Discovery Meeting','1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Onboarding',  'Archive Top-level Pages',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Onboarding',  'Get AW/GWT/Analytics Logins','1',   '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Onboarding',  'Inventory Content Assets', '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Onboarding',  'Build Keyword Universe',   '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Onboarding',  'Craft Keyword Portfolio',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Onboarding',  'Setup SERP Tracking',      '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Onboarding',  'Setup Optional Tracking',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Onboarding',  'SEO Software Training',    '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'SiteAudit',   'Review Crawl & robots.txt','2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'SiteAudit',   'Architecture & URL',       '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'SiteAudit',   'Analytics Goals',          '2',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'SiteAudit',   'Responsive & Mobile Friendly','2',  '',          'False',      'False',      '?',      ''),
    (datestamp(), 'SiteAudit',   'Product & Categories',     '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'SiteAudit',   'Titles, Descriptions',     '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'SiteAudit',   'Body Copy',                '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'SiteAutit',   'Open Graph & Sharability', '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'SiteAudit',   'Schema & HTML5 Semantics', '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'SiteAudit',   'Local Pages',              '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'SiteAudit',   'Site Speed',               '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'SiteAudit',   'Duplicate Content',        '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'SiteAudit',   'Externalized Code',        '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'SiteAudit',   'HTML & XML Sitemaps',      '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'SiteAudit',   'Server Response Codes',    '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'SiteAudit',   'Excessively Dynamic URLs', '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Competition', 'Anlayze & Monitor',        '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Competition', 'Report on',                '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Offsite',     'Develop Content Strategy', '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Offsite',     'Make Content Recos',       '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Offsite',     'Guide Email Outreach',     '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Offsite',     'Help w/ PR & Partnering',  '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Offsite',     'Social Media Signals',     '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'UXTesting',   'Conversion',               '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'UXTesting',   'Usability',                '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'UXTesting',   'Multivariate/Heatmap/Playback','2', '',          'True',       'False',      '?',      '')
  ]

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

