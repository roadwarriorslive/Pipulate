""" Pipulate lets you collect data straight off of the Web into spreadsheets.
          _____ _             _       _
         |  __ (_)           | |     | |
         | |__) | _ __  _   _| | __ _| |_ ___     ___ ___  _ __ ___
         |  ___/ | '_ \| | | | |/ _` | __/ _ \   / __/ _ \| '_ ` _ \
         | |   | | |_) | |_| | | (_| | ||  __/  | (_| (_) | | | | | |
         |_|   |_| .__/ \__,_|_|\__,_|\__\___| (_)___\___/|_| |_| |_|
                 | |
                 |_|

            It doesn't look like much, but looks can be deceiving.
           I center these lines in the vim editor by hitting shift-V
            to highlight the text and then hitting :center[Enter].
              This is important to remember. I program in Python
                 primarily so that I can work on this project.
                     You will not understand this message
                           until you do. Greetings!
"""

import globs                                        # Talmudic style commentaries
import requests, time, sys, os, json                # Requests will help 3.x port
from flask_wtf import Form                          # All Flask form examples use it
from wtforms import StringField
from flask import (Flask,                           # This app is all about Flask
  stream_with_context,                              # Yes, comments even work here
  render_template,
  Response,                                         # Occasionally, open the Python
  request,                                          # interactive interpreter and
  session,                                          # then type: import this
  redirect,                                         # Internalize those messages
  url_for,                                          # and then wonder why exit()
  flash)                                            # needs those parentheses.

app = Flask(__name__)                               # Flask init requirement

app.secret_key = "m\x00\r\xa5\\\xbeTW\xb3\xdf\x17\xb0!T\x9b6\x88l\xcf\xa1vmD}"

def out(msg):                                       # Debug output to server terminal
  if globs.DBUG:
    print(msg)

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

@app.route("/", methods=['GET', 'POST'])            # Main point of entry when
def main():                                         # visiting app's homepage.
  streamit = False                                  # Default to not streaming.
  form = PipForm(csrf_enabled=False)                # Initialize form for UI.
  if session:                                       # I've seen you before!
    if 'oa2' in session:                            # and I think you're logged in
      import gspread                                # so I'll grab spreadsheet API
      creds = Credentials(access_token=session['oa2'])
      for x in range(0, globs.retrytimes):
        try:
          gsp = gspread.authorize(creds)
          gsp.openall()
          session['loggedin'] = "1"
        except:
          session.clear()
          flash("Login expired. Please log back in")

  if request.method == 'POST':                      # Pipulation must only ever
    if form.pipurl.data:                            # occur on the POST method
      globs.PIPURL = form.pipurl.data               # with a submitted URL. That
      streamit = stream_with_context(pipulate())    # tells us to start streaming.
    else:                                           # Some messages just have to
      flash('Please enter a URL to Pipulate')       # be flashed versus streamed.
  else:
    if request.args and "access_token" in request.args:
      session['oa2'] = request.args.get("access_token")
      session['loggedin'] = "1"
      if 'u' in session:
        return redirect(url_for('main', u=session['u']))
      else:
        return redirect(url_for('main'))
    elif request.args and 'logout' in request.args:
      if session:
        if 'oa2' in session:
          revokeurl = 'https://accounts.google.com/o/oauth2/revoke?token=' + session['oa2']
          requests.get(revokeurl)
        if 'u' in request.args:
          form.pipurl.data = request.args.get('u')
        session.clear()
        flash('Logged out from Google.')
    elif request.args:
      if 'u' in request.args:
        form.pipurl.data = request.args.get('u')
        session['u'] = request.args.get('u')
      if session and 'u' in session:
        form.pipurl.data = session['u']
    if form.pipurl.data and request.url_root == url_root(form.pipurl.data):
      form.pipurl.data = '' #can't pipulate the pipulate site
  if streamit:
    return Response(stream_template('pipulate.html', form=form, data=streamit))
  else:
    return render_template('pipulate.html', form=form)

def pipulate():
  try:
    out("Beginning to pipulate")
    yield "Beginning to pipulate...", "", ""
    yield "spinon", "", ""
    funcs = [x for x in globals().keys() if x[:2] != '__'] #List all functions
    globs.transfuncs = ziplckey(funcs, funcs) #Keep translation table
    blankrows = 0
    import gspread
    if session:
      if 'oa2' in session:
        out("OAuth2 token found")
        creds = Credentials(access_token=session['oa2'])
      else:
        yield "Google Login appears to have expired. Log back in.", "", ""
        yield "spinoff", "", ""
        raise StopIteration
      try:
        gsp = gspread.authorize(creds)
      except:
        yield "Google Login unsuccessful.", "", ""
        yield "spinoff", "", ""
        raise StopIteration
      try:
        gdoc = gsp.open_by_url(globs.PIPURL)
      except gspread.exceptions.NoValidUrlKeyFound:
        yield "Currently, the URL must be a Google Spreadsheet.", "", ""
        yield "<a href='https://docs.google.com/spreadsheets/create' target='_new'>Create</a> a new Google Spreadsheet and click Bookmarklet again.", "Google Spreadsheet Not Found.", ""
        raise StopIteration
      except gspread.exceptions.SpreadsheetNotFound:
        yield "Please give the document a name to force first save.", "", ""
        yield "spinoff", "", ""
        raise StopIteration
      except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        ename = type(e).__name__
        fixme = "%s, %s, %s" % (ename, fname, exc_tb.tb_lineno)
        yield fixme, "", ""
        yield "spinoff", "", ""
        raise StopIteration
      try:
        worksheet = gdoc.worksheet("Pipulate")
      except:
        headers = ['URL', 'Tweeted', 'Shared', 'Liked', 'Plussed', 'DateStamp', 'TimeStamp']
        yme = InitTab(gdoc, 'Pipulate', headers, pipinit())
        worksheet = gdoc.worksheet("Pipulate")
        yield yme, "", ""
      finally:
        globs.numrows = len(worksheet.col_values(1))
      try:
        gdoc.worksheet("Config")
      except:
        headers = ['name', 'value']
        yme = InitTab(gdoc, 'Config', headers)
        yield yme, "", ""
      globs.config = refreshconfig(gdoc, "Config")
      try:
        gdoc.worksheet("Scrapers")
      except:
        headers = ['name', 'type', 'pattern']
        yme = InitTab(gdoc, 'Scrapers', headers, scrapes())
        yield yme, "", ""
      sst = gdoc.worksheet("Scrapers")
      lod = sst.get_all_records() #Returns list of dictionaries
      #lod = json.dumps(sst.get_all_records()) #Returns list of dictionaries
      #yield "Getting all records", "All Records", pjson
      #raise StopIteration
      pat = [[d['pattern']][0] for d in lod]
      typ = [[d['type']][0] for d in lod]
      nam = [[d['name']][0] for d in lod]
      globs.scrapetypes = ziplckey(nam, typ)
      globs.scrapepatterns = ziplckey(nam, pat)
      globs.transscrape = ziplckey(nam, nam)

      trendlistoflists = []
      globs.row1 = lowercaselist(worksheet.row_values(1))
      row1funcs(globs.row1)
      trended = False
      qstart = 1
      yield "", "Looking For Trend Jobs", ""
      for rowdex in range(1, worksheet.row_count+1): #Give trending its own loop
        onerow = worksheet.row_values(rowdex)
        yield "", "", json.dumps(onerow)
        if onerow:
          if rowdex == 2: #Looking for trending requests
            if '*' in onerow:
              yield "Found trending asterisks in row 2", "", ""
              trended = True
              trendlistoflists.append(onerow)
            else:
              break
          elif trendlistoflists and rowdex > 2:
            if '*' in onerow:
              yme = ", %s" % rowdex
              yield yme, "", ""
              trendlistoflists.append(onerow)
            else:
              blankrows += 1
              if blankrows > 1:
                break
        else:
          blankrows += 1
          if blankrows > 1:
            break
      if trended:
        qstart = globs.numrows + 1
      else:
        qstart = 1
      if trendlistoflists:
        for x in range(0, globs.retrytimes):
          try:
            InsertRows(worksheet, trendlistoflists)
            trendlistoflists = []
            break
          except Exception as e:
            exc_type, exc_value, exc_tb = sys.exc_info()
            filename, line_num, func_name, text = traceback.extract_tb(exc_tb)[-1]
            out('%s, %s, %s, %s' % (filename, func_name, line_num, text))
            out("Error on trending, retry %s" % x)
            time.sleep(globs.retryseconds)

      #We need to get it again if trending rows were added.
      if trended:
        try:
          worksheet = gdoc.worksheet("Pipulate")
        except:
          yield "Couldn't reach Google Docs. Try logging in again.", "", ""
          yield "spinoff", "", ""
          raise StopIteration

      globs.numrows = len(worksheet.col_values(1))
      blankrows = 0 #Lets us skip occasional blank rows
      out("Question mark replacement")
      for index, rowdex in enumerate(range(qstart, worksheet.row_count+1)): #Start stepping through every row.
        if index == 0:
          yme = "Pipulating row: %s" % rowdex
          yield yme, "", ""
        else:
          yme = ", %s" % rowdex
          yield yme, "", ""
        globs.hobj = None
        globs.html = '' #Blank the global html object. Recylces fetches.
        rowrange = "A%s:%s%s" % (rowdex, globs.letter[len(globs.row1)], rowdex)
        CellList = worksheet.range(rowrange)
        onerow = []
        for cell in CellList:
          onerow.append(cell.value)
        yield "", "Row %s" % rowrange, json.dumps(onerow)
        if '?' in onerow:
          #Perfect opportunity to test nested generator messages
          blankrows = 0
          newrow = processrow(str(rowdex), onerow) #Replace question marks in row
          newrow = ['' if x==None else x for x in newrow]
          out(newrow)
          #yield "", "", json.dumps(newrow)
          for index, onecell in enumerate(CellList):
            onecell.value = newrow[index]
            result = None
          for x in range(0, globs.retrytimes):
            try:
              result = worksheet.update_cells(CellList)
              out("Successfully updated row %s" % rowdex)
              break
            except:
              out("API problem on row %s. Retrying." % rowdex)
              time.sleep(globs.retryseconds)
        elif onerow.count('') == len(onerow):
          blankrows += 1
          if blankrows > globs.skippableblankrows:
            break
      out('Finished question marks')
    else:
      yield 'Please Login to Google', "", ""
    yield "Pipulation complete.", "", ""
    yield "spinoff", "", ""
    out("Pipulation complete")
  except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    ename = type(e).__name__
    if ename == "StopIteration":
      loginmsg = ""
      if session and 'loggedin' in session and session['loggedin'] != '1':
        loginmsg = "Login link under the upper-left \"burger button\"."
      yield "Better pipulating next time.", loginmsg, ""
    else:
      fixme = "%s, %s, %s" % (ename, fname, exc_tb.tb_lineno)
      yield fixme, "", ""
      yield "Pipulation prematurely terminated.", "", ""
      yield "Please open an issue at https://github.com/miklevin/pipulate", "", ""
      yield "Or just tap me on the shoulder.", "", ""
    yield "spinerr", "", ""

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
  return '''javascript:(function(){window.open('http://%s/?u='+encodeURIComponent(document.location.href), 'Pipulate', 'toolbar=0,resizable=1,scrollbars=1,status=1,width=640,height=520');})();''' % (request.headers['Host'])

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
  worksheet = gdoc.worksheet(sheetname)
  names = worksheet.col_values(1)
  values = worksheet.col_values(2)
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

def InsertRow(worksheet, onelist):
  column = globs.letter[len(onelist)]
  endrow = globs.numrows + 1
  rowrange = "A%s:%s%s" % (endrow, column, endrow)
  if endrow == worksheet.row_count + 1:
    worksheet.append_row(onelist)
    #worksheet.add_rows(1)
  else:
    CellList = worksheet.range(rowrange)
    out('Inserting row in range %s' % rowrange)
    for index, cell in enumerate(CellList):
      ival = ''
      if onelist[index] == None:
        ival = ''
      else:
        ival = onelist[index]
      cell.value = ival
      worksheet.update_cells(CellList)
  globs.numrows += 1

def InsertRows(worksheet, listoflists):
  numnewrows = len(listoflists)
  lastrowused = globs.numrows
  numrowsneeded = len(listoflists)
  allrowsevenempty = worksheet.row_count
  availableblankrows = allrowsevenempty - lastrowused
  if availableblankrows < numrowsneeded:
    rowstoadd = numrowsneeded - availableblankrows
    worksheet.add_rows(rowstoadd)
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
  CellList = worksheet.range(rowrange)
  for index, onecell in enumerate(CellList):
    try:
      onecell.value = flattenitlist[index]
    except:
      pass
  worksheet.update_cells(CellList)
  return

def InitTab(gdoc, tabname, headerlist, listoflists=[]):
  numcols = len(headerlist)
  if listoflists and '*' in listoflists[1]:
    numrows = len(listoflists)+1
  elif listoflists:
    numrows = len(listoflists)+2
  else:
    numrows = 2
  endletter = globs.letter[numcols]
  newtab = gdoc.add_worksheet(title=tabname, rows=numrows, cols=numcols)
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
  newtab.update_cells(CellList)
  return "Making %s tab." % tabname

def questionmark(oldrow, rowdex, coldex):
  """Returns true if a question mark is supposed to be replaced in cell.

  This is called for every cell on every row processed and checks whether
  question mark replacemnt should actually occur."""
  if rowdex != 1:
    if oldrow[coldex] == '?':
      return True
  return False

def processrow(rowdex, onerow):
  """Separates row-1 handling from question mark detection on all other rows.

  Called on each row of a worksheet and either initializes functions when it's
  row 1, or steps cell by cell along each subsequent (fed-in) row and when
  encountering a question mark, it determines whether to invoke the function
  indicated by the column label, using values from the active row as parameter
  values if available, parameter defaults if not, and None if not found."""
  import traceback
  changedrow = onerow[:]
  if rowdex > 1:
    #All subsequent rows are checked for question mark replacement requests.
    for coldex, acell in enumerate(changedrow):
      if questionmark(onerow, rowdex, coldex):
        if 'url' in globs.row1: #Only fetch html once per row if possible
          try:
            globs.html = gethtml(onerow[globs.row1.index('url')])
          except:
            pass
        collabel = globs.row1[coldex]
        if collabel in globs.transfuncs.keys():
          for x in range(0, globs.retrytimes):
            try:
              changedrow[coldex] = evalfunc(coldex, changedrow) #The Function Path
              out('FUNCTION SUCCESS: %s ' % collabel)
              break
            except Exception as e:
              exc_type, exc_value, exc_tb = sys.exc_info()
              filename, line_num, func_name, text = traceback.extract_tb(exc_tb)[-1]
              out('%s, %s, %s, %s' % (filename, func_name, line_num, text))
              out("Function problem on row %s. Retrying." % rowdex)
              time.sleep(globs.retryseconds)
        elif collabel in globs.transscrape.keys():
          for x in range(0, globs.retrytimes):
            try:
              changedrow[coldex] = genericscraper(coldex, changedrow) #Scraping
              out('SCRAPE SUCCESS: %s ' % collabel)
              break
            except Exception as e:
              exc_type, exc_value, exc_tb = sys.exc_info()
              filename, line_num, func_name, text = traceback.extract_tb(exc_tb)[-1]
              out('%s, %s, %s, %s' % (filename, func_name, line_num, text))
              out("Scrape problem on row %s. Retrying." % rowdex)
              time.sleep(globs.retryseconds)
  return changedrow

def row1funcs(onerow):
  """Scans row-1 for names of global functions and builds dict of requirements.

  This is only invoked on row 1 of a worksheet, where the names of functions
  and parameters are expected to be discovered. By the end, we've created a
  dictionary of dictionaries called globs.fargs which plays an important role
  in building the code necessary for question mark replacement."""
  fargs = {}
  for coldex, fname in enumerate(onerow):
    try:
      fname = fname.lower()
    except:
      pass
    if fname in globs.transfuncs.keys(): #Detect if column name is a function
      fargs[coldex] = {}
      from inspect import getargspec
      argspec = getargspec(eval(fname))
      if argspec: # Function has parameters
        myargs = argspec[0]
        mydefs = argspec[3]
        offset = 0
        if mydefs:
          offset = len(myargs) - len(mydefs)
          if offset:
            for i in range(0, offset-1):
              fargs[coldex][myargs[i]] = None
            for i in range(offset, len(myargs)):
              fargs[coldex][myargs[i]] = mydefs[offset-i]
        else:
          for anarg in myargs:
            fargs[coldex][anarg] = None
        for argdex, anarg in enumerate(myargs): #For each argument of function
          fargs[coldex][anarg] = None

  globs.fargs = fargs #Make dict global so we don't have to pass it around

def evalfunc(coldex, onerow):
  """Builds string to execute to get value to replace question mark with.

  Once a question mark is found in a cell belonging to a function-named column,
  the exact invocation that's needed must be built, keeping in mind default
  values provided by function itself, as well as parameter values provided in
  the provided row. Because rows are being handled as lists, order is
  important, and the column index allows function name lookup."""
  fname = globs.transfuncs[globs.row1[coldex]]
  fargs = globs.fargs[coldex]
  evalme = "%s(" % fname #Begin building string that will eventually be eval'd
  if fargs:
    #The function we're looking at DOES have required arguments.
    for anarg in fargs:
      #Add an arg=value to string for each required argument.
      anarg = anarg.lower()
      argval = getargval(anarg, fargs[anarg], onerow)
      evalme = "%s%s=%s, " % (evalme, anarg, argval)
    evalme = evalme[:-2] + ')' #Finish building string for the eval statement.
  else:
    #No arguments required, so just immediately close the parenthesis.
    evalme = evalme + ')'
  return eval(evalme)

def genericscraper(coldex, onerow):
  sname = globs.transscrape[globs.row1[coldex]]
  stype = globs.scrapetypes[sname]
  spattern = globs.scrapepatterns[sname]
  if 'url' in globs.row1:
    url = onerow[globs.row1.index('url')]
    html = gethtml(url)
    if stype.lower() == 'xpath':
      import lxml.html
      searchme = lxml.html.fromstring(html)
      match = searchme.xpath(spattern)
      if match:
        return match[0]
      else:
        return None
    elif stype.lower() == 'regex':
      import re
      match = re.search(spattern, html, re.S | re.I)
      if match:
        if "scrape" in match.groupdict().keys():
          keep = match.group("scrape")
          return keep
        else:
          return None
      else:
        return None

def gethtml(url):
  if globs.html:
    out("Recycling fetched HTML")
    return globs.html
  else:
    out("Doing first HTML fetch for row")
    try:
      globs.hobj = requests.get(url)
    except:
      return None
    globs.html = globs.hobj.text
  return globs.html

def getargval(anarg, defargval, onerow):
  """Returns value to set argument equal-to in function invocation string.

  This function returns which value should be used as the arguments to the
  function invocation string being built. The value found on the row always
  beats the default provided by the function. Lacking values on the row and a
  default, the Python value of None will be returned."""
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
  """Conditionally builds quotes on arg-value for function invocation string.

  This handles the value quoting details when building argument part of the
  function invocation string when replacing a question mark. For example, the
  keyword None must not become quoted. Typically, numbers shouldn't be quoted
  either, but we're feeding everything but None around as strings for now."""
  if aval == None:
    return None #None-in/None-out. This special keyword shouldn't be quoted.
  else:
    return "'%s'" % (aval) #ALMOST everything else should be quoted.

from functions import *

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8888, debug=True)

