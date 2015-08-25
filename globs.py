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

config =    {}     # In-memory copy of everything from Config tab
row1 =      []     # Copy of contents of sheet1, row 1 for many uses.
nosedive =  False  # Allow to recur but once.
STOP =      False  # The Emergency Break so functions cans top Pipulate.
DOCID =     None   # The Google Doc key for use anywhere in system
DOCLINK =   None   # The full a href link for the Google Sheet.
WEB =       False  # Controls whether yields show (webpipulate vs. loopipulate)
PCOM =      True   # Turns True if pipulate in hostname. Tracks usage.
DBUG =      True   # Turns on and off verbose console output.
PIPURL =    ''     # Constant containing URL from bookmarklet click.
MODE =      ''     # Constant containing menu selection upon bookmarklet click.
KEYWORDS =  ''     # Constant containing selected text when bookmarklet clicked.
html =      ''     # Avoids re-fetching HTML multiple times for same row.
hobj =      ''     # Original Requests object for row's HTML with response headers.
nest =      ''     # Controls nested indents of debug output.
sheet =     ''     # Makes sheet1 worksheet object accessible to user functions.
EMPTY =     ''     # How to populate cell if nothing returned
TAB =       ''     # Name of Sheet1 on Tab
numrows =   0      # Tracks latest number of rows in sheet1 (for InsertRows)
ROWMAX =    10000  # The size over which a row will not attempt to insert into sheet.
NAME =      "Pipulate"                                      # Default GSheet file name.
DOMURL =    "http://pipulate.com"                           # Default for Login Button
FILE =      "/var/opt/pipulate.cfg"                         # Flask server configuration
TOKEN =     "/var/opt/pipulate.pkl"                         # OAuth2 access token
SHEETS =    'https://docs.google.com/spreadsheets'          # URL to identify being in GSheets"
OAUTHURL =  "https://accounts.google.com/o/oauth2/auth"     # OAuth2 API Endpoint
GBAD =      "Google Data API timed out. Sorry, try again."  # Default message for GDocs unreachable.
PBNJMAN =   '&nbsp;<img id="pbjt" src="./static/gifs/pbjmanwhite.gif" style="vertical-align: top;">'
letter =    {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',15:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'} # Spreadsheet-style mapping
# gethtml will not do a head request for Content-Type on URLs with these extensions.
texttypes = ['.asmx', '.asp', '.aspx', '.atom', '.cfm', '.cgi', '.css', '.htm',
  '.htm', '.html', '.js', '.json', '.jsp', '.php', '.php3', '.php4', '.php5',
  '.rss', '.shtm', '.shtml', '.xht', '.xhtm', '.xhtml', '.xml']
