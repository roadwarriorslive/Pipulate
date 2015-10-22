from flask import session
from common import *

def documentation():
  s = []
  #s.append(['xxx',                  'Filter',    'Url',                       'Return xxx.', ''])
  s.append(['Archive',              'Crawl',     'Url',                       "Return an archived version of the page's URL. Scrapers can work against archive column.", ''])
  s.append(['Barebones',            'Filter',    'Url',                       'Return bare bones HTML (almost everything but critical tags stripped out).', ''])
  s.append(['Canonical',            'Crawl',     'Url',                       'Return Canonical.', ''])
  s.append(['Comments',             'Facebook',  'Url',                       'Return Facebook count.', ''])
  s.append(['Crawl',                'Crawl',     'LinksTo',                   'Make one row per link found on target, as set up by PreCrawl.', ''])
  s.append(['DateStamp',            'Time',      '',                          'Return current date only in easy to read format. Good for oncce/day tasks.', ''])
  s.append(['Description',          'Crawl',     'Url',                       'Return meta description.', ''])
  s.append(['Difficulty',           'Keyword',   'Keyword',                   'Return SEMRush Keyword Difficulty.', ''])
  s.append(['DomainAuthority',      'MOZ',       'Url',                       'Return Moz Domain Authority score for a URL.', ''])
  s.append(['ExtractKeywords',      'Crawl',     'Url',                       "Return a list of keywords extracted from URL in depending order of likely importance.", ''])
  s.append(['Fb',                   'Facebook',  'Url',                       'Return Facebook likes, shares, clicks and comments as JSON.', ''])
  s.append(['Followers',            'Twitter',   'Url',                       'Return Twitter followers count.', ''])
  s.append(['Following',            'Twitter',   'Url',                       'Return Twitter following count.', ''])
  s.append(['Ga',                   'Crawl',     'Url',                       'Return Google Analytics ID to check if GA installed on page.', ''])
  s.append(['GetLinks',             'Crawl',     'Url',                       'Return list of links found on page. Adds rows.', ''])
  s.append(['H1',                   'Crawl',     'Url',                       'Return contents of H1 tag.', ''])
  s.append(['H2',                   'Crawl',     'Url',                       'Return contents of H2 tag.', ''])
  s.append(['H3',                   'Crawl',     'Url',                       'Return contents of H3 tag.', ''])
  s.append(['H4',                   'Crawl',     'Url',                       'Return contents of H4 tag.', ''])
  s.append(['H5',                   'Crawl',     'Url',                       'Return contents of H5 tag.', ''])
  s.append(['H6',                   'Crawl',     'Url',                       'Return contents of H6 tag.', ''])
  s.append(['Headlines',            'Crawl',     'Url',                       'Return all headlines from the page, stuffed and stacked in a single cell.', ''])
  s.append(['Instagram_Followers',  'Social',    'Instagram_Name',            'Return Instagram Followers count.', ''])
  s.append(['JsonApi',              'Generic',   'Endpoint, Url, Jkey',       "Return response code from any JSON API that doesn't require login.", ''])
  s.append(['Likes',                'Facebook',  'Url',                       'Return Facebook likes for given URL.', ''])
  s.append(['Markdown',             'Filter',    'Url',                       'Return HTML stripped-down into markdown code.', ''])
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
  s.append(['TopKeyword',           'Crawl',     'ExtractKeywords',           "Return the top most likely important keyword from ExtractKeywords column.", ''])
  s.append(['TopUrl',               'Serps',     'Site, (Positions)',         'Return URL-from-site in top position for a keyword and site.', ''])
  s.append(['TweetTotal',           'Twitter',   'Url',                       'Return Twitter total-tweet count for a Twitter profile URL.', ''])
  s.append(['Tweets',               'Twitter',   'Url',                       'Return Twitter tweet-count for a URL.', ''])
  s.append(['Twitter_Followers',    'Twitter',   'Twitter_Name',              'Return Twitter follower count for a Twitter profile URL.', ''])
  s.append(['Views',                'YouTube',   'url',                       'Return YouTube view count for a YouTube video URL.', ''])
  s.append(['Volume',               'Keyword',   'Keyword',                   'Return SEMRush Keyword Volume.', ''])
  return s

def seedkeywordlist():
  return [
    ('Keyword', 'Priority', 'Source', 'Volume', 'Difficulty')
  ] + [''*5]*30

def expansionkeywordlist():
  return [
    ('Keyword', 'Volume', 'Difficulty', 'Source', 'Categories', 'Priority')
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

def meetings():
  return [
    ('Date', 'Subject', 'Attendees', 'Agenda', 'NextSteps')
  ]

def seochecklistlist():
  return [
    ('DateStamp', 'Task',                          'Category',    'Phase', 'StartDate', 'Recurrence', 'WhetherDue', 'Status', 'Notes'),
    (datestamp(), 'Monthly',                       'Reports',     '2',     '',          'True',       'True',       '?',      ''),
    (datestamp(), 'UXReport',                      'Reports',     '2',     '',          'True',       'True',       '?',      ''),
    (datestamp(), 'Statement of Work into Notes',  'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Customize Checklist per SOW',   'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Setup Project Management',      'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'List ALL sites in play',        'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Top-level Quick Audit',         'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Perform & Archive Deep Crawl',  'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Record Top-level Findings',     'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Conduct Discovery Meeting',     'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Get AW/GWT/Analytics Logins',   'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Inventory Content Assets',      'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Build Keyword Universe',        'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Build Keyword Portfolio',       'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Setup SERP Tracking',           'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Setup Any Other Tracking',      'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'SEO Software Training',         'Onboarding',  '1',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Review Crawl & robots.txt',     'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Architecture & URL',            'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Analytics Goals',               'SiteAudit',   '2',     '',          'False',      'True',       '?',      ''),
    (datestamp(), 'Responsive & Mobile Friendly',  'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Product & Categories',          'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Titles, Descriptions',          'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Body Copy',                     'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Open Graph & Sharability',      'SiteAutit',   '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Schema & HTML5 Semantics',      'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Local Pages',                   'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Site Speed',                    'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Duplicate Content',             'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Externalized Code',             'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'HTML & XML Sitemaps',           'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Server Response Codes',         'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Excessively Dynamic URLs',      'SiteAudit',   '2',     '',          'False',      'False',      '?',      ''),
    (datestamp(), 'Anlayze & Monitor',             'Competition', '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Report on',                     'Competition', '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Develop Content Strategy',      'Offsite',     '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Make Content Recos',            'Offsite',     '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Guide Email Outreach',          'Offsite',     '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Help w/ PR & Partnering',       'Offsite',     '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Social Media Signals',          'Offsite',     '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Conversion',                    'UXTesting',   '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Usability',                     'UXTesting',   '2',     '',          'True',       'False',      '?',      ''),
    (datestamp(), 'Multivariate/Heatmap/Playback', 'UXTesting',   '2',     '',          'True',       'False',      '?',      '')
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

