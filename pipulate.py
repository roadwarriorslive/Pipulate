"""        Because life's too short to not collect  ABOUT THE AUTHOR:
           data in the same place you work with it  http://mikelev.in
            _____ _             _       _           http://levinux.com
           |  __ (_)           | |     | |          http://pipulate.com
           | |__) | _ __  _   _| | __ _| |_ ___    ___ ___  _ __ ___
           |  ___/ | '_ \| | | | |/ _` | __/ _ \  / __/ _ \| '_ ` _ \
           | |   | | |_) | |_| | | (_| | ||  __/ | (_| (_) | | | | | |
           |_|   |_| .__/ \__,_|_|\__,_|\__\___|(_)___\___/|_| |_| |_|
                   | |
            It does|_| look like much, but looks can be deceiving.
           I center these lines in the vim editor by hitting Shift-V
            to highlight the text and then hitting :center[Enter].
              This is important to remember. I program in Python
                 primarily so that I can work on this project
                   and generally think more clearly in life.
                    I crave super-powers in an age before,
                        yet obsessed with, super heros.
                          So, with the clock ticking
                             I have made this, my
                               best attempt, for
                                  my daughter
                                      Adi
"""
import sys, os, socket
socket.setdefaulttimeout(1.1)                             # Our story begins with Talmudic style commentaries 
if len(sys.argv) > 1:                                     # (in-line columns), which I'm using as a way 
  print("Captured invoking from command-line!")           # of issuing a challenge to myself to master the
  exit()                                                  # vim text editor, so as to make the sort of text
                                                          # manipulation skills required to pull this off no
import globs                                              # big thing. Oh yeah, and we import Python modules 
import requests, traceback, datetime, time, json          # here that should be available globally (everywhere)
from flask_wtf import Form                                # in the program. Oh, also that detection of sys.args
from wtforms import StringField                           # forks the behavior to the non-Flask command-line
from flask import (Flask,                                 # mode of Pipulate. This is required for the
  stream_with_context,                                    # Scheduler-behavior (versus webserver behavior).
  render_template,
  Response,                                         
  request,                                          
  session,                                          
  redirect,                                         
  url_for,                                          
  flash)                                            

app = Flask(__name__)                               

app.secret_key = "m\x00\r\xa5\\\xbeTW\xb3\xdf\x17\xb0!T\x9b6\x88l\xcf\xa1vmD}"

def Stop():
  print('''
    ____ ____    _  _____  _    _____ _                    _    ___        _   
   / ___|  _ \  / \|_   _|/ \  |_   _(_)_ __ ___   ___  __| |  / _ \ _   _| |_ 
  | |  _| | | |/ _ \ | | / _ \   | | | | '_ ` _ \ / _ \/ _` | | | | | | | | __|
  | |_| | |_| / ___ \| |/ ___ \  | | | | | | | | |  __/ (_| | | |_| | |_| | |_ 
   \____|____/_/   \_\_/_/   \_\ |_| |_|_| |_| |_|\___|\__,_|  \___/ \__,_|\__|
                                                                               
  ''')
  raise SystemExit

def gotcha(x=''):
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
  raise SystemExit

def out(msg, symbol='', dent=''):
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

def stream_template(template_name, **context):      # This is the key to streaming
  app.update_template_context(context)              # output to the user in the
  t = app.jinja_env.get_template(template_name)     # web browser much like a
  rv = t.stream(context)                            # long page load, but with
  return rv                                         # better memory efficiency.

@app.context_processor                              # Anything that I want to be
def templateglobals():                              # available in Jinja2 templates
  return dict(loginlink=getLoginlink(),             # without having to always
  bookmarklet=getBookmarklet(),                     # pass them as parameters
  logoutlink=getLogoutlink(),
  cyclemotto=cyclemotto(),
  )

class PipForm(Form):
  pipurl = StringField('Paste a Google Spreadsheet URL:')

#  _____ _           _                      _       
# |  ___| | __ _ ___| | __  _ __ ___   __ _(_)_ __  
# | |_  | |/ _` / __| |/ / | '_ ` _ \ / _` | | '_ \ 
# |  _| | | (_| \__ \   <  | | | | | | (_| | | | | |
# |_|   |_|\__,_|___/_|\_\ |_| |_| |_|\__,_|_|_| |_|
#                                                   
@app.route("/", methods=['GET', 'POST'])            # Main point of entry when
def main():                                         # visiting app's homepage.
  stop = False
  print('''
               ____  _             _       _   _                          
              |  _ \(_)_ __  _   _| | __ _| |_(_)_ __   __ _              
              | |_) | | '_ \| | | | |/ _` | __| | '_ \ / _` |             
              |  __/| | |_) | |_| | | (_| | |_| | | | | (_| |  _   _   _  
              |_|   |_| .__/ \__,_|_|\__,_|\__|_|_| |_|\__, | (_) (_) (_) 
                      |_|                              |___/              
  ''')

  out("ENTERED MAIN FUNCTION", "0")
  STREAMIT = False                                  # Default to not streaming.
  form = PipForm(csrf_enabled=False)                # Initialize form for UI.
  if session:                                       # I've seen you before!
    if 'oa2' in session:                            # and I think you're logged in
      import gspread                                # so I'll grab spreadsheet API
      creds = Credentials(access_token=session['oa2'])
      for x in range(4):
        try:
          gsp = gspread.authorize(creds)
          gsp.openall()
          session['loggedin'] = "1"
        except:
          session.pop('loggedin', None)
          if 'u' not in session and globs.PIPURL:
            session['u'] = globs.PIPURL
  if request.method == 'POST':
    if form.pipurl.data:
      globs.PIPURL = form.pipurl.data
      STREAMIT = stream_with_context(Pipulate())
    else:
      flash('Please enter a URL to Pipulate (or click bookmarklet again)')
  else:
    if request.args and "access_token" in request.args:
      session['oa2'] = request.args.get("access_token")
      session['loggedin'] = "1"
      session['i'] -= 1 #Don't skip a message, just becuse I redirect.
      if 'u' in session :
        out("Redirecting with a filed-in URL")
        out("EXITING MAIN FUNCTION REDIRECT", "0", '-')
        return redirect(url_for('main', u=session['u']))
      else:
        out("Redirecting, no URL known")
        out("EXITING MAIN FUNCTION REDIRECT", "0", '-')
        return redirect(url_for('main'))
    elif request.args and 'logout' in request.args:
      if session:
        if 'oa2' in session:
          revokeurl = 'https://accounts.google.com/o/oauth2/revoke?token=' + session['oa2']
          requests.get(revokeurl)
        if 'u' in request.args:
          form.pipurl.data = request.args.get('u')
        session.pop('loggedin', None)
        flash('Logged out from Google.')
    elif request.args:
      if 'u' in request.args:
        form.pipurl.data = request.args.get('u')
        session['u'] = request.args.get('u')
      if session and 'u' in session:
        form.pipurl.data = session['u']
    if form.pipurl.data and request.url_root == url_root(form.pipurl.data):
      form.pipurl.data = '' #can't pipulate the pipulate site
  out("Selecting template method.")
  if STREAMIT:
    return Response(stream_template('pipulate.html', form=form, data=STREAMIT))
  else:
    out("EXITING MAIN FUNCTION RENDER", "0", '-')
    return render_template('pipulate.html', form=form)
  out("EXITING MAIN", "0", '-')

def makemescroll():
  for i in range(0, 10): 
    yield "line %s" % i

#  ____  _             _       _       
# |  _ \(_)_ __  _   _| | __ _| |_ ___ 
# | |_) | | '_ \| | | | |/ _` | __/ _ \
# |  __/| | |_) | |_| | | (_| | ||  __/
# |_|   |_| .__/ \__,_|_|\__,_|\__\___|
#         |_|                          
#
def Pipulate():
  stop = False
  badtuple = (globs.GBAD, globs.GBAD, "", "")
  out("PIPULATION BEGINNING", "1")
  #for i in makemescroll():
  #  yield i, "", "", ""
  try:
    yield "Beginning to pipulate...", "", "", ""
    yield "spinon", "", "", ""
    out("Reading in functions.")
    funcs = [x for x in globals().keys() if x[:2] != '__'] #List all functions
    transfuncs = ziplckey(funcs, funcs) #Keep translation table
    blankrows = 0
    import gspread
    login = False
    if session:
      out("LOGIN ATTEMPT", "2")
      if 'oa2' in session:
        creds = Credentials(access_token=session['oa2'])
        out("Credential object created.")
      else:
        out("Expired login.")
        yield "Google Login appears to have expired. Log back in.", "Login under the \"burger button\" in the upper-right.", "", ""
        yield "spinoff", "", "", ""
      try:
        gsp = gspread.authorize(creds)
      except:
        out("Login failed.")
        yield "Google Login unsuccessful.", "", "", ""
        yield "spinoff", "", "", ""
        raise StopIteration
      else:
        out("Login successful.")
      out("Opening Spreadsheet...")
      yield("Opening Spreadsheet...", "", "", "")
      gdoc = None
      stop = True
      for x in range(5):
        try:
          gdoc = gsp.open_by_url(globs.PIPURL) #HTTPError
          stop = False
          break
        except gspread.httpsession.HTTPError, e:
          out("Login appeared successful, but rejected on document open attempt.")
          yield "Please Log In again first.", "Login under the \"burger button\" in the upper-right.", "", ""
          if session and 'loggedin' in session:
            session.pop('loggedin', None)
          if 'u' not in session and globs.PIPURL:
            session['u'] = globs.PIPURL
        except gspread.exceptions.NoValidUrlKeyFound:
          yield "Currently, the URL must be a Google Spreadsheet.", "", "", ""
          yield "<a href='https://docs.google.com/spreadsheets/create' target='_new'>Create</a> a new Google Spreadsheet and click Bookmarklet again.", "Google Spreadsheet Not Found.", "", ""
        except gspread.exceptions.SpreadsheetNotFound:
          yield "Please give the document a name to force first save.", "", "", ""
          yield "spinoff", "", "", ""
        except Exception as e:
          exc_type, exc_obj, exc_tb = sys.exc_info()
          fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
          ename = type(e).__name__
          fixme = "%s, %s, %s" % (ename, fname, exc_tb.tb_lineno)
          yield fixme, "", "", ""
          yield "spinoff", "", "", ""
        else:
          login = True
          out("Google Spreadsheet successfully opened.")
          yield "", "", "", "" #whitelock
        if login:
          out("LOGIN SUCCESS", "2", '-')
        else:
          out("LOGIN FAILURE", "2", '-')
          raise StopIteration
      if stop:
        yield badtuple
        Stop()

      headers = ['URL', 'Subscribers', 'ISOTimeStamp', 'Count']
      try:
        InitTab(gdoc, 'Pipulate', headers, pipinit())
      except:
        print traceback.format_exc()

      out("Counting rows in Pipulate tab.")
      stop = True
      for x in range(10):
        try:
          onesheet = gdoc.worksheet("Pipulate")
          stop = False
          break
        except:
          out("Trying to count rows in Pipulate tab again.")
          time.sleep(5)
      if stop:
        yield badtuple
        Stop()

      stop = True
      for x in range(10):
        try:
          globs.numrows = len(onesheet.col_values(1)) #!!!UnboundLocalError HTTPError OPTIMIZE!
          stop = False
          break
        except:
          out("Reloading column 1 values for global numrows count.")
          time.sleep(10)
      if stop == True:
        yield badtuple
        Stop()
      yme = "%s rows found in Pipulate tab." % globs.numrows
      out(yme)
      yield yme, "", "", ""


      headers = ['name', 'value']
      config = []
      config.append(['rowthrottlenumber','1'])
      config.append(['rerunjobevery','minute'])
      InitTab(gdoc, 'Config', headers, config)

      try:
        out("Reading Config tab into globals.")
        globs.config = refreshconfig(gdoc, "Config") #HTTPError
      except:
        out("Copying Config tag to globals failed.")
      else:
        out("Config tab copied to globals.")


      headers = ['name', 'type', 'pattern']
      InitTab(gdoc, 'Scrapers', headers, scrapes())
      sst = None

      out("Loading Scrapers.")
      stop = True
      for x in range(5):
        try:
          sst = gdoc.worksheet("Scrapers")
          stop = False
          break
        except:
          out("Failed to load Scrapers.")
          time.sleep(3)
      if stop:
        yield badtuple
        Stop()

      try:
        lod = sst.get_all_records() #Returns list of dictionaries
      except:
        out("Failed to load Scrapers 2")
      else:
        pat = [[d['pattern']][0] for d in lod]
        typ = [[d['type']][0] for d in lod]
        nam = [[d['name']][0] for d in lod]
        scrapetypes = ziplckey(nam, typ)
        scrapepatterns = ziplckey(nam, pat)
        transscrape = ziplckey(nam, nam)
        out("Scrapaers loaded.")

      #!!! blink
      out("Loading row1 into globals.")
      for x in range(4):
        try:
          globs.row1 = lowercaselist(onesheet.row_values(1))
          break
        except Exception as e:
          print traceback.format_exc()
          out("Failed to load row 1.")
          time.sleep(2)
      out("Row 1 succesfully loaded.")
      trendlistoflists = []
      out("Scanning row 1 for function and scraper names.")
      fargs = {}
      for coldex2, fname in enumerate(globs.row1):
        try:
          fname = fname.lower()
        except:
          pass
        if fname in transfuncs.keys():
          out("Found function %s in row 1." % fname)
          fargs[coldex2] = {}
          from inspect import getargspec
          argspec = getargspec(eval(fname))
          if argspec:
            out("%s has arguments." % (fname))
            myargs = argspec[0]
            mydefs = argspec[3]
            offset = 0
            if mydefs:
              out("%s has defaults," % (fname))
              offset = len(myargs) - len(mydefs)
              if offset:
                for i in range(0, offset-1):
                  fargs[coldex2][myargs[i]] = None
                for i in range(offset, len(myargs)):
                  fargs[coldex2][myargs[i]] = mydefs[offset-i]
            else:
              out("%s has no defaults." % (fname))
              for anarg in myargs:
                fargs[coldex2][anarg] = None
            for argdex, anarg in enumerate(myargs): #For each argument of function
              fargs[coldex2][anarg] = None

      #            _            _     _        
      #   __ _ ___| |_ ___ _ __(_)___| | _____ 
      #  / _` / __| __/ _ \ '__| / __| |/ / __|
      # | (_| \__ \ ||  __/ |  | \__ \   <\__ \
      #  \__,_|___/\__\___|_|  |_|___/_|\_\___/
      #                                  
      trended = False
      qstart = 1
      out("Scan down Pipulate tab looking for asterisks.", "2")
      rightletter = globs.letter[len(globs.row1)]
      rightnumber = 100
      if globs.numrows < 100:
        rightnumber = globs.numrows
      inspectrange = "A2:%s%s" % (rightletter, rightnumber)
      CellList = None
      stop = True
      for x in range(4):
        try:
          CellList = onesheet.range(inspectrange)
          stop = False
          break
        except:
          out("Grabbing cells to inspect for asterisks failed.")
          time.sleep(4)
      if stop:
        yield badtuple
        Stop()
      onerow = []
      if CellList:
        for cell in CellList:
          onerow.append(cell.value)
      for rowdex in range(1, globs.numrows+1):
        out("Scanning row %s for asterisks." % rowdex) #This can have a pretty long delay
        stop = True
        for x in range(8):
          try:
            onerow = onesheet.row_values(rowdex) #!!! HTTPError OPTIMIZE THIS!
            stop = False
            break
          except:
            out("Couldn't open row.")
            time.sleep(5)
        if stop:
          yield badtuple
          Stop()
        out("Successfully opened row.")
        if onerow:
          if rowdex == 2: #Looking for trending requests
            if '*' in onerow:
              trended = True
              out("Found asterisks on row 2 -- trending activated!")
              trendlistoflists.append(onerow)
              yield "Found asterisks indicating trending in row 2", "Then we look for trending job requests...", json.dumps(onerow), ""
            else:
              break
          elif trendlistoflists and rowdex > 2:
            if '*' in onerow:
              out("Found astrisks on row %s." % rowdex)
              trendlistoflists.append(onerow)
              yme = ", %s" % rowdex
              yield yme, "", json.dumps(onerow), ""
            else:
              blankrows += 1
              if blankrows > 1:
                out("Found second row without asterisks, so stopped looking.")
                break
        else:
          blankrows += 1
          if blankrows > 1:
            out("Found second blank row, so trending scan complete.")
            break
      yme = "%s row trending-job found." % len(trendlistoflists)
      yield yme, "", "", ""
      trendingrowsfinished = True
      rowthrottlenumber = 0
      out("Done looking for asterisks", "2", "-")

      #  _   _                   ___                           _   
      # | |_(_)_ __ ___   ___   ( _ )     ___ ___  _   _ _ __ | |_ 
      # | __| | '_ ` _ \ / _ \  / _ \/\  / __/ _ \| | | | '_ \| __|
      # | |_| | | | | | |  __/ | (_>  < | (_| (_) | |_| | | | | |_ 
      #  \__|_|_| |_| |_|\___|  \___/\/  \___\___/ \__,_|_| |_|\__|
      #
      out("Count and ISOTimeStamp columns for trending", '2')
      times = []
      if trended and 'count' in globs.row1:
        backintime = globs.numrows - len(trendlistoflists) + 1
        countletter = globs.letter[globs.row1.index('count') + 1]
        mayhaverun = "%s%s:%s%s" % (countletter, backintime, countletter, globs.numrows)
        try:
          CellList = onesheet.range(mayhaverun)
        except:
          out("Failed to load the trending Count range.")
          raise StopIteration
        counts = []
        for onecell in CellList:
          counts.append(onecell.value)
        samecount = all(x == counts[0] for x in counts)
        if samecount:
          if counts[0] == '*':
            counts[0] = 0
          #Here we need to detect if there's rows left over.
          timeletter = globs.letter[globs.row1.index('isotimestamp') + 1]
          mayhaverun = "%s%s:%s%s" % (timeletter, backintime, timeletter, globs.numrows)
          try:
            CellList = onesheet.range(mayhaverun)
          except:
            out("Failed to load the trending ISOTimeStamp range.")
          for onecell in CellList:
            times.append(onecell.value)
          trendingrowsfinished = times.count('?') == 0
          if trendingrowsfinished:
            rowthrottlenumber = len(trendlistoflists)
            if not counts[0]:
              yield "Last set of trending rows complete.", "", "", ""
          if 'rowthrottlenumber' in globs.config:
            rowthrottlenumber = globs.config['rowthrottlenumber']
          try:
            int(rowthrottlenumber)
          except:
            rowthrottlenumber = 0
          if not trendingrowsfinished:
            qstart = globs.numrows - times.count('?') + 1
            trendlistoflists = []
          nextnum = int(counts[0]) + 1
          for onelist in trendlistoflists:
            onelist[globs.row1.index('count')] = nextnum
      out("Count and ISOTimeStamp columns for trending", '2', '-')

      #  _                     _                           
      # (_)_ __  ___  ___ _ __| |_   _ __ _____      _____ 
      # | | '_ \/ __|/ _ \ '__| __| | '__/ _ \ \ /\ / / __|
      # | | | | \__ \  __/ |  | |_  | | | (_) \ V  V /\__ \
      # |_|_| |_|___/\___|_|   \__| |_|  \___/ \_/\_/ |___/
      #
      out("Insert new rows for new time increment trending", '2')
      if trended and trendingrowsfinished == True:
        qstart = globs.numrows + 1
      elif trended:
        pass
      else:
        qstart = 1
      #jobstats = timewindow(times[0])
      insert, name, number, left, right, now = timewindow(times[0])
      yield "Job requested to process %s row(s) every %s %s" % (rowthrottlenumber, number, name), "", "", ""
      if left and right and now:
        yield "%s = Start of last time wndow" % left, "", "", ""
        yield "%s = End of last time window" % right, "", "", ""
        yield "%s = Currrent time" % now, "", "", ""
      if trendlistoflists and insert: #This line will show in errors for any Config scheduling screw-ups.
        for x in range(4):
          try:
            InsertRows(onesheet, trendlistoflists)
          except Exception as e:
            print traceback.format_exc()
            out("Error on trending, retry %s" % x)
            time.sleep(2)
          else:
            trendlistoflists = []
            break
      #We need to get it again if trending rows were added. !!! Optimize
      if trended:
        try:
          onesheet = gdoc.worksheet("Pipulate")
        except:
          yield "Couldn't reach Google Docs. Try logging in again.", "", "", ""
          yield "spinoff", "", "", ""
          raise StopIteration
        else:
          pass
      #globs.numrows = len(onesheet.col_values(1))
      globs.numrows = globs.numrows + len(trendlistoflists) #faster
      out("Insert new rows for new tine inrement trending", '2', '-')
      #                        _   _                                    _        
      #   __ _ _   _  ___  ___| |_(_) ___  _ __    _ __ ___   __ _ _ __| | _____ 
      #  / _` | | | |/ _ \/ __| __| |/ _ \| '_ \  | '_ ` _ \ / _` | '__| |/ / __|
      # | (_| | |_| |  __/\__ \ |_| | (_) | | | | | | | | | | (_| | |  |   <\__ \
      #  \__, |\__,_|\___||___/\__|_|\___/|_| |_| |_| |_| |_|\__,_|_|  |_|\_\___/
      #     |_|                                                                  
      #
      out("Question Mark Replacement.", '2')
      blankrows = 0 #Lets us skip occasional blank rows
      for index, rowdex in enumerate(range(qstart, onesheet.row_count+1)): #Start stepping through every row.
        if rowthrottlenumber: # if rowthrottlenumber is 0, this won't trap
          if index >= int(rowthrottlenumber):
            break
        if index == 0:
          yme = "Pipulating row: %s" % rowdex
          yield yme, "Next, we replace question marks. This may take awhile...", "", ""
        else:
          yme = ", %s" % rowdex
          yield yme, "", "", ""
        globs.hobj = None
        globs.html = '' #Blank the global html object. Recylces fetches.
        rowrange = "A%s:%s%s" % (rowdex, globs.letter[len(globs.row1)], rowdex)
        CellList = onesheet.range(rowrange)
        onerow = []
        for cell in CellList:
          onerow.append(cell.value)
        if '?' in onerow:
          #   _ __ _____      __
          #  | '__/ _ \ \ /\ / /
          #  | | | (_) \ V  V / 
          #  |_|  \___/ \_/\_/  
          #
          out("PROCESSING ROW %s." % rowdex, '3')
          blankrows = 0
          yield "", "", json.dumps(onerow), ""
          rowdexstring = str(rowdex)
          newrow = onerow[:]
          if rowdexstring > 1:
            #All subsequent rows are checked for question mark replacement requests.
            for coldex, acell in enumerate(newrow):
              if questionmark(onerow, rowdexstring, coldex):
                if 'url' in globs.row1: #Only fetch html once per row if possible
                  try:
                    globs.html = gethtml(onerow[globs.row1.index('url')])
                  except:
                    pass
                collabel = globs.row1[coldex]
                if collabel in transfuncs.keys():
                  for x in range(4):
                    #   __                  _   _                 
                    #  / _|_   _ _ __   ___| |_(_) ___  _ __  ___ 
                    # | |_| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
                    # |  _| |_| | | | | (__| |_| | (_) | | | \__ \
                    # |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
                    #                                             
                    out("Function Start", "4")
                    fname = transfuncs[globs.row1[coldex]]
                    farg = fargs[coldex]
                    evalme = "%s(" % fname #Begin building string that will eventually be eval'd
                    if farg:
                      #The function we're looking at DOES have required arguments.
                      for anarg in farg:
                        #Add an arg=value to string for each required argument.
                        anarg = anarg.lower()
                        argval = getargval(anarg, farg[anarg], newrow)
                        evalme = "%s%s=%s, " % (evalme, anarg, argval)
                      evalme = evalme[:-2] + ')' #Finish building string for the eval statement.
                    else:
                      #No arguments required, so just immediately close the parenthesis.
                      evalme = evalme + ')'
                    try:
                      newrow[coldex] = eval(evalme)
                      out('%s worked' % collabel)
                    except Exception as e:
                      print traceback.format_exc()
                      time.sleep(2)
                    out("Function End", "4", '-')
                elif collabel in transscrape.keys():
                  for x in range(4):
                    #  ____                                 
                    # / ___|  ___ _ __ __ _ _ __   ___ _ __ 
                    # \___ \ / __| '__/ _` | '_ \ / _ \ '__|
                    #  ___) | (__| | | (_| | |_) |  __/ |   
                    # |____/ \___|_|  \__,_| .__/ \___|_|   
                    #                      |_|              
                    out("Scrape Start", "4")
                    try:
                      out("Entering generic scraper.")
                      sname = transscrape[globs.row1[coldex]]
                      stype = scrapetypes[sname]
                      spattern = scrapepatterns[sname]
                      if 'url' in globs.row1:
                        url = onerow[globs.row1.index('url')]
                        html = gethtml(url)
                        if stype.lower() == 'xpath':
                          import lxml.html
                          searchme = lxml.html.fromstring(html)
                          match = searchme.xpath(spattern)
                          if match:
                            newrow[coldex] = match[0]
                          else:
                            newrow[coldex] =  None
                        elif stype.lower() == 'regex':
                          import re
                          match = re.search(spattern, html, re.S | re.I)
                          if match:
                            if "scrape" in match.groupdict().keys():
                              newrow[coldex] = match.group("scrape")
                            else:
                              newrow[coldex] = None
                          else:
                            newrow[coldex] = None

                      out('%s worked.' % collabel)
                    except Exception as e:
                      print traceback.format_exc()
                      out("Scrape problem on row %s. Retrying." % rowdexstring)
                      time.sleep(2)
                    out("Scrape End", "4", '-')
          out("DONE PROCESSING ROW %s." % rowdex, '3', '-')




          out("Finished pipulating replacing questionmarks in memory.")
          newrow = ['' if x==None else x for x in newrow]
          yield "", "", json.dumps(newrow), ""
          for index, onecell in enumerate(CellList):
            onecell.value = newrow[index]
            result = None
          for x in range(4):
            try:
              result = onesheet.update_cells(CellList)
              out("Successfully updated row %s" % rowdex)
              break
            except:
              out("API problem on row %s. Retrying." % rowdex)
              time.sleep(2)
        elif onerow.count('') == len(onerow):
          blankrows += 1
          if blankrows > skippableblankrows:
            break
      out("Question Mark Replacement.", '2', '-')


    else: #No session object found
      yield 'Please Login to Google', "", "", ""
    yield "Pipulation complete.&nbsp;&nbsp;", "Congratulations, pipulation complete! Now, do a little victory dance.", "", ""
    yield "spinoffsuccess", "", "", ""
    out("PIPULATION OVER", "1", '-')
  except Exception as e:
    print traceback.format_exc()

    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    ename = type(e).__name__
    fixme = "%s, %s, %s" % (ename, fname, exc_tb.tb_lineno)
    out(fixme)
    out("Pipulation Failure")
    if ename == "StopIteration":
      loginmsg = ""
      if session and 'loggedin' in session and session['loggedin'] != '1':
        loginmsg = "Login link under the upper-left \"burger button\"."
      yield "Session timed out. Try again", "If at first you don't succeed, pipulate again.", "", ""
    else:
      yield fixme, "", "", ""
      yield "Pipulation prematurely terminated.", "", "", ""
      yield "Please open an issue at https://github.com/miklevin/pipulate", "", "", ""
      yield "Or just tap me on the shoulder.", "", "", ""
    yield "spinerr", "", "", ""
    out("PIPULATION ERROR", "1", '-')
  out("EXITING MAIN", "0", '-') #Special case of function exit reporting
  print("\n")

def url_root(url):
  from urlparse import urlparse
  parsed = urlparse(url)
  return "%s://%s%s" % (parsed[0], parsed[1], parsed[2])

def getLoginlink():
  redir = 'http://'+request.headers['Host']
  if request.args and 'u' in request.args:
    session['u'] = request.args.get('u')
  baseurl = "https://accounts.google.com/o/oauth2/auth"
  qsdict = {  'scope': 'https://docs.google.com/feeds/ https://docs.googleusercontent.com/ https://spreadsheets.google.com/feeds/',
              'response_type': 'token',
              'redirect_uri': redir,
              'approval_prompt': 'force',
              'client_id': '394883714902-h3fjk3u6rb4jr4ntpeft41kov6et2nve.apps.googleusercontent.com'
            }
  from urllib import urlencode
  return "%s?%s" % (baseurl, urlencode(qsdict))

def getBookmarklet():
  return '''javascript:(function(){window.open('http://%s/?u='+encodeURIComponent(document.location.href), 'Pipulate', 'toolbar=0,resizable=1,scrollbars=1,status=1,width=640,height=600');})();''' % (request.headers['Host'])

def getLogoutlink():
  from urllib import quote_plus
  u = ''
  host = request.headers['Host']
  if session and 'u' in session:
    u = session['u']
  elif request.args and 'u' in request.args:
    u = request.args.get('u')
  if u:
    u = quote_plus(u)
  if u:
    logout = "http://%s?logout&u=%s" % (host, u)
  else:
    logout = "http://%s?logout" % host
  return logout

class Credentials (object):
  def __init__ (self, access_token=None):
    self.access_token = access_token

def refreshconfig(gdoc, sheetname):
  #!!! Needs optimization
  onesheet = gdoc.worksheet(sheetname)
  names = onesheet.col_values(1)
  values = onesheet.col_values(2)
  return ziplckey(names, values)

def ziplckey(keys, values):
  keys = lowercaselist(keys)
  return dict(zip(keys, values))

def lowercaselist(onelist):
  for index, item in enumerate(onelist):
    try:
      onelist[index] = item.lower()
    except:
      pass
  return onelist

def timewindow(amiinnewtimewindow):
  if amiinnewtimewindow == "*":
    return (True,'','','','','')
  intervallanguage = ""
  intervalnumber= ""
  intervalname=""
  intervalparts=[]
  if 'rerunjobevery' in globs.config:
    intervallanguage = globs.config['rerunjobevery'].strip()
    if ' ' in intervallanguage:
      intervalparts=intervallanguage.split()
      intervalname = intervalparts[1]
      if intervalname:
        intervalname = intervalname.lower()
      intervalnumber = intervalparts[0]
      out("Parsed out interval name: %s" % intervalname)
      out("Parsed out interval number: %s" % intervalnumber)
    else:
      if intervallanguage.isdigit():
        intervalname = "minute"
        intervalnumber = intervallanguage
      else:
        intervalname = intervallanguage
        intervalnumber = '1'
    ltr = intervalname[:2].lower()
    if ltr == 'mi':
      intervalname = "minute"
    elif ltr == 'ho':
      intervalname = "hour"
    elif ltr == 'da':
      intervalname = "day"
    elif ltr == 'we':
      intervalname = "week"
    elif ltr == 'mo':
      intervalname = "month"
    else:
      intervalname = "minute"
    now = datetime.datetime.now()
    now2 = now
    import dateutil.parser
    try:
      tick = dateutil.parser.parse(amiinnewtimewindow)
    except:
      tick = now #double-check this fall-over action
    left = None
    right = None
    try:
      intervalnumber = int(intervalnumber)
    except:
      out("Caught the type error")
      return (False,'','','','','')
    doinserts = False
    if intervalname == 'minute':
      out("Processing a %s %s interval." % (intervalnumber, intervalname))
      left = tick - datetime.timedelta(minutes=tick.minute % intervalnumber, seconds=tick.second, microseconds=tick.microsecond)
      now = now - datetime.timedelta(minutes=now.minute % intervalnumber, seconds=now.second, microseconds=now.microsecond)
      right = left + datetime.timedelta(minutes=intervalnumber)
    elif intervalname == 'hour':
      out("Processing a %s %s interval." % (intervalnumber, intervalname))
      left = tick - datetime.timedelta(hours=tick.hour % intervalnumber, minutes=tick.minute, seconds=tick.second, microseconds=tick.microsecond)
      now = now - datetime.timedelta(hours=now.hour % intervalnumber, minutes=now.minute, seconds=now.second, microseconds=now.microsecond)
      right = left + datetime.timedelta(hours=intervalnumber)
    elif intervalname == 'day':
      #Could be made shorter with use of .date()
      out("Processing a %s %s interval." % (intervalnumber, intervalname))
      left = tick - datetime.timedelta(days=tick.day % intervalnumber, hours=tick.hour, minutes=tick.minute, seconds=tick.second, microseconds=tick.microsecond)
      now = now - datetime.timedelta(days=now.day % intervalnumber, hours=now.hour, minutes=now.minute, seconds=now.second, microseconds=now.microsecond)
      right = left + datetime.timedelta(days=intervalnumber)
    elif intervalname == 'week':
      out("Processing a %s %s interval." % (intervalnumber, intervalname))
      left = find_sunday(tick.date())
      right = add_weeks(left, intervalnumber)
      now = now.date()
    elif intervalname == 'month':
      out("Processing a %s %s interval." % (intervalnumber, intervalname))
      left = tick.date().replace(day=1)
      right = left.replace(month=now.month + intervalnumber)
      now = now.date()
    else:
      out("unknown")
    out("%s last %s time interval left boundary." % (left, intervalname))
    out("%s last %s time interval right boundary." % (right, intervalname))
    out("%s is the current %s." % (now, intervalname))
    if now2 > right:
      out("We are in a new %s-boundary, so we insert rows." % intervalname)
      doinserts = True
    else:
      out("We are still within the old %s %s boundary, so skip new rows insert." % (intervalnumber, intervalname))
      doinserts = False
    rme = (doinserts, intervalname, intervalnumber, left, right, now2)
    return rme
  return (True,'','','','','')

def find_sunday(day):
  day_of_week = day.weekday()
  to_beginning_of_week = datetime.timedelta(days=day_of_week)
  beginning_of_week = day - to_beginning_of_week
  beginning_of_week = beginning_of_week - datetime.timedelta(days=1)
  return (beginning_of_week)

def add_weeks(sourcedate, weeks):
  days = weeks * 7
  daystoadd = datetime.timedelta(days=days)
  newdate = sourcedate + daystoadd
  return newdate

def InsertRow(onesheet, onelist):
  column = globs.letter[len(onelist)]
  endrow = globs.numrows + 1
  rowrange = "A%s:%s%s" % (endrow, column, endrow)
  if endrow == onesheet.row_count + 1:
    onesheet.append_row(onelist)
    #onesheet.add_rows(1)
  else:
    CellList = onesheet.range(rowrange)
    out('Inserting row in range %s' % rowrange)
    for index, cell in enumerate(CellList):
      ival = ''
      if onelist[index] == None:
        ival = ''
      else:
        ival = onelist[index]
      cell.value = ival
      onesheet.update_cells(CellList)
  globs.numrows += 1

def InsertRows(onesheet, listoflists):
  numnewrows = len(listoflists)
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
  CellList = onesheet.range(rowrange)
  for index, onecell in enumerate(CellList):
    try:
      onecell.value = flattenitlist[index]
    except:
      pass
  onesheet.update_cells(CellList)
  return

def InitTab(gdoc2, tabname, headerlist, listoflists=[]):
  #yield "Entering InitTab", "", "", ""
  initsheet = None
  try:
    initsheet = gdoc2.worksheet(tabname)
  except:
    pass
  else:
    out("%s Tab exists." % tabname)

  if not initsheet:
    numcols = len(headerlist)
    if listoflists and len(listoflists) > 1 and '*' in listoflists[1]:
      numrows = len(listoflists)+1
    elif listoflists:
      numrows = len(listoflists)+2
    else:
      numrows = 2
    endletter = globs.letter[numcols]
    newtab = gdoc2.add_worksheet(title=tabname, rows=numrows, cols=numcols)
    CellList = newtab.range('A1:%s%s' % (endletter, numrows))
    initlist = []
    for onelist in listoflists:
      for onecell in onelist:
        initlist.append(onecell)
    wholelist = headerlist + initlist
    for index, onecell in enumerate(CellList):
      try:
        onecell.value = wholelist[index]
      except:
        pass
    try:
      newtab.update_cells(CellList)
    except:
      out("%s tab creation failed." % tabname)
    else:
      out("%s tab created." % tabname)
    #yield "Exiting InitTab", "", "", ""
  

def questionmark(oldrow, rowdex, coldex):
  if rowdex != 1:
    if oldrow[coldex] == '?':
      return True
  return False

def gethtml(url):
  if globs.html:
    out("Recycling HTML.")
    return globs.html
  else:
    out("Doing first HTML fetch for row.")
    try:
      globs.hobj = requests.get(url)
    except:
      return None
    globs.html = globs.hobj.text
  return globs.html

def getargval(anarg, defargval, onerow):
  for coldex, acol in enumerate(globs.row1):
    if acol == anarg: #Found column named same thing as a required argument.
      if onerow[coldex]: #The cell in that column has a non-zero/empty value.
        return adq(onerow[coldex]) #So, we got what we need. Return it.
  #Oops, no required arguments were found on the row.
  if defargval:
    return adq(defargval) #So, if it's got a default value, return that.
  else:
    return None #We ALWAYS have to return at least None, least errors ensue.

def adq(aval):
  if aval == None:
    return None #None-in/None-out. This special keyword shouldn't be quoted.
  else:
    return "'%s'" % (aval) #ALMOST everything else should be quoted.

def retry():
  for x in range(4):
    try:
      a = 1
      break
    except:
      time.sleep(2)

from functions import *

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8888, debug=True)

