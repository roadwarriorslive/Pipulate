#   ____ _       _           _  __     __         _       _     _           
#  / ___| | ___ | |__   __ _| | \ \   / /_ _ _ __(_) __ _| |__ | | ___  ___ 
# | |  _| |/ _ \| '_ \ / _` | |  \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|
# | |_| | | (_) | |_) | (_| | |   \ V / (_| | |  | | (_| | |_) | |  __/\__ \
#  \____|_|\___/|_.__/ \__,_|_|    \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/
#                                                                           
#                             Welcome to the globals
#                           You can reach them any way
#                        But to do so, use a globs prefix
#                         It's the price you have to pay

PCOM = False  # Turns True if pipulate in hostname. Tracks usage.
DBUG = True   # Turns on and off verbose console output.
PIPURL = ''   # Constant containing URL from bookmarklet click.
PIPMODE = ''  # Constant containing menu selection upon bookmarklet click.
KEYWORDS = '' # Constant containing selected text when bookmarklet clicked.
numrows = 0   # Tracks latest number of rows in sheet1 (for InsertRows)
config = {}   # In-memory copy of everything from Config tab
html = ''     # Avoids re-fetching HTML multiple times for same row.
hobj = ''     # Original Requests object for row's HTML with response headers.
row1 = []     # Copy of contents of sheet1, row 1 for many uses.
nest = ''     # Controls nested indents of debug output.
sheet = ''    # Makes sheet1 worksheet object accessible to user functions.
CANONICAL = "http://pipulate.com" # Default for Login Button
GBAD = "Timed-out on Google Data API. Sorry, try again." # Default message for GDocs unreachable.
letter = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',15:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'} # Spreadsheet-style mapping
# gethtml will not do a head request for Content-Type on URLs with these extensions.
texttypes = ['.asmx', '.asp', '.aspx', '.atom', '.cfm', '.cgi', '.css', '.htm',
  '.htm', '.html', '.js', '.json', '.jsp', '.php', '.php3', '.php4', '.php5',
  '.rss', '.shtm', '.shtml', '.xht', '.xhtm', '.xhtml', '.xml']

menu = {
'learn':        "Learn How To Pipulate!",
'test':         "Run System Tests",
'clear':        "Clear sheet1 (initialize)",
'seocrawl':     "1-Page SEO Crawl",
'socialcrawl':  '1-Page Social Crawl',
'ogcrawl':      '1-Page Open Graph Crawl',
'mobilecrawl':  '1-Page Mobile Crawl',
'keywords':     'Collect Keywords',
'search':       "Capture Search Results",
'qm':           "Replace Question Marks",
'ytsubs':       "Get Subscriber Count",
'ytviews':      "Get View Count",
'ytvids':       "Get Video Links",
'twsearch':     "Capture Twitter Search",
'twstats':      "Get Profile Stats"
}

invmenu = {v: k for k, v in menu.items()}
