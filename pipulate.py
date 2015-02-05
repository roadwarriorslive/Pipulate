""" Pipulate lets you collect data straight off of the Web into spreadsheets.

        _____ _             _       _
       |  __ (_)           | |     | |
       | |__) | _ __  _   _| | __ _| |_ ___     ___ ___  _ __ ___
       |  ___/ | '_ \| | | | |/ _` | __/ _ \   / __/ _ \| '_ ` _ \
       | |   | | |_) | |_| | | (_| | ||  __/  | (_| (_) | | | | | |
       |_|   |_| .__/ \__,_|_|\__,_|\__\___| (_)___\___/|_| |_| |_|
               | |
               |_|

"""

import globs #Create objects that don't have to be passed as arguments.
import requests
from flask import Flask, Response, request, render_template, session, flash, redirect, url_for

from flask_wtf import Form
from flask_wtf.file import FileField
from wtforms import validators, StringField
from wtforms.validators import DataRequired, Optional, Required

app = Flask(__name__, static_folder='../uploads', static_url_path='/files')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

def out(msg):
  if globs.DBUG:
    print(msg)

def stream_template(template_name, **context):
  app.update_template_context(context)
  t = app.jinja_env.get_template(template_name)
  rv = t.stream(context)
  rv.enable_buffering(5)
  return rv

@app.context_processor
def templateglobals():
    return dict(loginlink=getLoginlink(), bookmarklet=getBookmarklet())

class PipForm(Form):
  pipurl = StringField('Paste a Google Spreadsheet URL:')

@app.route("/", methods=['GET', 'POST'])
def main():
  out("Entering Main")
  form = PipForm(csrf_enabled=False)
  if session:
    if 'oa2' in session:
      import gspread
      credentials = Credentials(access_token=session['oa2'])
      try:
        gsp = gspread.authorize(credentials)
        gsp.openall()
        session['loggedin'] = "1"
      except:
        #session.clear()
        pass
  if request.method == 'POST':
    if form.pipurl.data:
      globs.PIPURL = form.pipurl.data
      pipulate()
    else:
      flash('Nothing to Pipulate. Enter a Google Spreadsheet URL and try again.')
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
        session.clear()
        flash('Logged out from Google.')
    elif request.args:
      if 'u' in request.args:
        session['u'] = request.args.get('u')
      if session:
        if 'u' in session:
          form.pipurl.data = session['u']
      if form.pipurl.data and request.url_root == url_root(form.pipurl.data):
        form.pipurl.data = ''
  def g():
    import time
    for i, c in enumerate("hello"*10):
      time.sleep(.1)  # an artificial delay
      yield i, c
  return Response(stream_template('pipulate4.html', form=form, data=g()))
  #return render_template('pipulate.html', form=form)

def url_root(url):
  from urlparse import urlparse
  parsed = urlparse(url)
  return "%s://%s%s" % (parsed[0], parsed[1], parsed[2])

def getLoginlink():
  baseurl = "https://accounts.google.com/o/oauth2/auth"
  qsdict = {  'scope': 'https://docs.google.com/feeds/ https://docs.googleusercontent.com/ https://spreadsheets.google.com/feeds/',
              'response_type': 'token',
              'redirect_uri': 'http://'+request.headers['Host'],
              'approval_prompt': 'force',
              'client_id': '394883714902-h3fjk3u6rb4jr4ntpeft41kov6et2nve.apps.googleusercontent.com'
            }
  from urllib import urlencode
  return "%s?%s" % (baseurl, urlencode(qsdict))

def getBookmarklet():
  return '''javascript:(function(){window.open('http://%s/?u='+encodeURIComponent(document.location.href), 'Pipulate', 'toolbar=0,resizable=1,scrollbars=1,status=1,width=640,height=520');})();''' % (request.headers['Host'])

class Credentials (object):
  def __init__ (self, access_token=None):
    self.access_token = access_token

def pipulate():
  """Allows processing of multiple worksheets."""

  funcs = [x for x in globals().keys() if x[:2] != '__'] #List all functions
  globs.transfuncs = zipnamevaldict(funcs, funcs) #Keep translation table
  qmarkstotal = 0
  blankrows = 0
  import gspread
  if session:
    if 'oa2' in session:
      out("OAuth2 token found")
      credentials = Credentials(access_token=session['oa2'])
    else:
      out("Token appears to have expired")
      flash('Not logged into Google. Please Login.')
      return
    out("Attempting to connect to Google Docs API.")
    try:
      gsp = gspread.authorize(credentials)
    except:
      return
    out("Attempting to open spreadsheet.")
    try:
      pipdoc = gsp.open_by_url(globs.PIPURL) 
    except gspread.exceptions.SpreadsheetNotFound:
      flash("Please give the document a name to force first save.")
      return
    except:
      flash("Difficulty opening spreadsheet.")
      return
    out("Attempting to open Pipulate worksheet.")
    try:
      pipsheet = pipdoc.worksheet("Pipulate")
    except:
      out("Initializing Pipulate worksheet.")
      headers = ['URL', 'Tweeted', 'Shared', 'Liked', 'Plussed', 'DateStamp', 'TimeStamp']
      inittab(pipdoc, 'Pipulate', headers, pipinit())
    pipsheet = pipdoc.worksheet("Pipulate")
    globs.numrows = len(pipsheet.col_values(1))
    try:
      pipdoc.worksheet("Config")
    except:
      headers = ['name', 'value']
      inittab(pipdoc, 'Config', headers)
    globs.config = refreshconfig(pipdoc, "Config")
    try:
      pipdoc.worksheet("Scrapers")
    except:
      headers = ['name', 'type', 'pattern']
      inittab(pipdoc, 'Scrapers', headers, scrapes())
    sst = pipdoc.worksheet("Scrapers")
    snames = sst.col_values(1)
    stypes = sst.col_values(2)
    spatterns = sst.col_values(3)
    globs.scrapetypes = zipnamevaldict(snames, stypes)
    globs.scrapepatterns = zipnamevaldict(snames, spatterns)
    globs.transscrape = zipnamevaldict(snames, snames)
    trendlist = []
    globs.row1 = lowercaselist(pipsheet.row_values(1))
    row1funcs(globs.row1)

    out("Trend spotting")
    trended = False
    qstart = 1
    for rowdex in range(1, pipsheet.row_count+1): #Give trending its own loop
      if rowdex > 1:
        out("Looking for asteriks on row %s " % rowdex)
      onerow = pipsheet.row_values(rowdex)
      if onerow:
        if rowdex == 2: #Looking for trending requests
          if '*' in onerow:
            trended = True
            trendlist.append(onerow)
          else:
            break
        elif trendlist and rowdex > 2:
          if '*' in onerow:
            trendlist.append(onerow)
          else:
            blankrows += 1
            if blankrows > 2:
              break
      else:
        blankrows += 1
        if blankrows > 2:
          break
    if trended:
      qstart = globs.numrows - len(trendlist) + 1
    else:
      qstart = 1
    for trendrow in trendlist:
      trendrow = ['?' if x=='*' else x for x in trendrow]
      InsertRow(pipsheet, trendrow)
    trendlist = []

    #We need to get it again if trending rows were added.
    if trended:
      try:
        pipsheet = pipdoc.worksheet("Pipulate")
      except:
        flash("Couldn't reach Google Docs. Try logging in again.")
        return

    globs.numrows = len(pipsheet.col_values(1))
    blankrows = 0
    out("Question mark replacement")
    for rowdex in range(qstart, pipsheet.row_count+1): #Start stepping through every row.
      globs.hobj = None
      globs.html = '' #Blank the global html object. Recylces fetches.
      onerow = pipsheet.row_values(rowdex)
      if onerow: #But only process it if it does not come back as empty list.
        out("Examining row %s" % rowdex)
        if '?' in onerow:
          newrow = processrow(str(rowdex), onerow) #Replace question marks in row
          blankrows = 0
          for coldex, acell in enumerate(newrow): #Then step through new row
            if acell == None:
              acell = ''
            #!!!ERROR
            pipsheet.update_cell(rowdex, coldex+1, acell) #Gspread has no "0" column
            qmarkstotal += 1
      else:
        blankrows += 1
        if blankrows > 3:
          break
    if qmarkstotal:
      flash('Replaced %s question marks.' % qmarkstotal)
    else:
      flash('No question marks found in Sheet 1.')
  else:
    flash('Please Login to Google')

def refreshconfig(pipdoc, sheetname):
  worksheet = pipdoc.worksheet(sheetname)
  names = worksheet.col_values(1)
  values = worksheet.col_values(2)
  return zipnamevaldict(names, values)

def zipnamevaldict(keys, values):
  keys = lowercaselist(keys)
  return dict(zip(keys, values))

def lowercaselist(alist):
  for index, item in enumerate(alist):
    try:
      alist[index] = item.lower()
    except:
      pass
  return alist

def InsertRow(worksheet, alist):
  column = globs.letter[len(alist)]
  endrow = globs.numrows + 1
  rowrange = "A%s:%s%s" % (endrow, column, endrow)
  if endrow == worksheet.row_count + 1:
    worksheet.append_row(alist)
    #worksheet.add_rows(1)
  else:
    cell_list = worksheet.range(rowrange)
    out('Inserting row in range %s' % rowrange)
    for index, cell in enumerate(cell_list):
      ival = ''
      if alist[index] == None:
        ival = ''
      else:
        ival = alist[index]
      cell.value = ival
      worksheet.update_cells(cell_list)
  globs.numrows += 1

def inittab(gdoc, tabname, headerlist, listoflists=[]):
  numcols = len(headerlist)
  newtab = gdoc.add_worksheet(title=tabname, rows="1", cols=numcols)
  cell_list = newtab.range('A1:%s1' % globs.letter[numcols])
  for index, cell in enumerate(cell_list):
    cell.value = headerlist[index]
  newtab.update_cells(cell_list)
  for row in listoflists:
    newtab.append_row(row)
  flash("Created %s tab." % (tabname))
  return

def questionmark(oldrow, rowdex, coldex):
  """Returns true if a question mark is supposed to be replaced in cell.
  
  This is called for every cell on every row processed and checks whether
  question mark replacemnt should actually occur."""
  if rowdex != 1:
    if oldrow[coldex] == '?':
      return(True)
  return(False)

def processrow(rowdex, onerow):
  """Separates row-1 handling from question mark detection on all other rows.
  
  Called on each row of a worksheet and either initializes functions when it's
  row 1, or steps cell by cell along each subsequent (fed-in) row and when
  encountering a question mark, it determines whether to invoke the function
  indicated by the column label, using values from the active row as parameter
  values if available, parameter defaults if not, and None if not found."""
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
        out('FUNCTION: %s ' % collabel)
        if collabel in globs.transfuncs.keys():
          changedrow[coldex] = evalfunc(coldex, changedrow) #The Function Path
        elif collabel in globs.transscrape.keys():
          changedrow[coldex] = genericscraper(coldex, changedrow) #Scraping
  return(changedrow)

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
  return(eval(evalme))

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

