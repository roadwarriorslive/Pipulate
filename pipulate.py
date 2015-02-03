""" Pipulate lets you collect data straight off of the Web into spreadsheets.

        _____ _             _       _
       |  __ (_)           | |     | |
       | |__) | _ __  _   _| | __ _| |_ ___     ___ ___  _ __ ___
       |  ___/ | '_ \| | | | |/ _` | __/ _ \   / __/ _ \| '_ ` _ \
       | |   | | |_) | |_| | | (_| | ||  __/  | (_| (_) | | | | | |
       |_|   |_| .__/ \__,_|_|\__,_|\__\___| (_)___\___/|_| |_| |_|
               | |
               |_|

Got a list that you need to look up something for every item - like grabbing
title tags for a list of URLs? Well, then Pipulate is your answer! For example,
for any given URL, you will be able to:

  1. Record the number of times that URL has appeared in a Tweet
  2. Record the number of times that URL was liked or shared in Facebook
  3. Record the number of times that URL was +1'd in Google Plus
  4. Figure out what keyword the page is trying to target for search traffic
  5. See how well that URL is doing for that keyword (position tracking)

And it all accumulates on a spreadsheet where you can do trending and keep
track of progress - all for free! But Pipulate is so much more, able to do such
lookups using any source data (addresses, keywords, etc.) against any Web or
data API source (you have access to), allowing you to write your own Python
functions to extend the system. And what system is that? You can learn it well,
because almost every line of code accompanied by a YouTube video. Playlist:
https://www.youtube.com/watch?v=SdzDaohx-GA&list=PLy-AlqZFg6G8tBTB6FFN68mryG4JlCaf-

REQUIREMENTS:
easy_install flask
easy_install flask_wtf
easy_install requests
easy_install gspread
"""

import globs #Create objects that don't have to be passed as arguments.
from flask import Flask, request, render_template, session, flash, redirect, url_for
from flask_wtf import Form
from flask_wtf.file import FileField
from wtforms import validators, StringField
from wtforms.validators import DataRequired, Optional, Required

app = Flask(__name__, static_folder='../uploads', static_url_path='/files')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.context_processor
def templateglobals():
    return dict(loginlink=getLoginlink(), bookmarklet=getBookmarklet())

class PipForm(Form):
  pipurl = StringField('Paste a Google Spreadsheet URL:')

@app.route("/", methods=['GET', 'POST'])
def main():
  form = PipForm(csrf_enabled=False)
  if session:
    if 'oa2' in session:
      import gspread
      credentials = Credentials(access_token=session['oa2'])
      try:
        gc = gspread.authorize(credentials)
        gc.openall()
        session['loggedin'] = "1"
      except:
        session.clear()
  if request.method == 'POST':
    if form.pipurl.data:
      globs.PIPURL = form.pipurl.data
      pipulate('gdocs')
    else:
      flash('Nothing to Pipulate. Enter a Google Spreadsheet URL and try again.')
    return render_template('pipulate.html', form=form)
  else:
    if request.args:
      if 'logout' in request.args:
        if session:
          if 'oa2' in session:
            import urllib2
            revokeurl = 'https://accounts.google.com/o/oauth2/revoke?token=' + session['oa2']
            urllib2.urlopen(revokeurl)
          session.clear()
          flash('Logged out from Google.')
        return render_template('pipulate.html', form=form)
      if "access_token" in request.args:
        session['oa2'] = request.args.get("access_token")
        session['loggedin'] = "1"
        return redirect(url_for('main'))
      if 'u' in request.args:
        session['u'] = request.args.get('u')
      if session:
        if 'u' in session:
          form.pipurl.data = session['u']
      if request.url_root == url_root(form.pipurl.data):
        form.pipurl.data = ''
    return render_template('pipulate.html', form=form)

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
  return '''javascript:(function(){window.open('http://%s/?u='+encodeURIComponent(document.location.href), 'Pipulate', 'toolbar=0,resizable=1,scrollbars=1,status=1,width=640,height=960');})();''' % (request.headers['Host'])

class Credentials (object):
  def __init__ (self, access_token=None):
    self.access_token = access_token

def pipulate(dbsource):
  """Allows processing of multiple worksheets."""

  funcs = [x for x in globals().keys() if x[:2] != '__'] #List all functions
  globs.funcslc = [x.lower() for x in funcs] #Lower-case all function names
  globs.transfunc = dict(zip(globs.funcslc, funcs)) #Keep translation table
  import pickle, gspread
  if session:
    if 'oa2' in session:
      credentials = Credentials(access_token=session['oa2'])
    else:
      flash('Not logged into Google. Please Login.')
      return
    try:
      gc = gspread.authorize(credentials)
      wks = gc.open_by_url(globs.PIPURL).sheet1 #HTTP connection errors happen here.
      # https://docs.google.com/spreadsheets/d/182yAd0VYBhY30IW1sGXUg110aWh0pMaQa4nVtWXgNBo/edit?usp=sharing
    except:
      flash("Couldn't reach Google Docs. Try logging in again.")
      return
    for rowdex in range(1, wks.row_count): #Start stepping through every row.
      arow = wks.row_values(rowdex)
      if arow: #But only process it if it does not come back as empty list.
        newrow = processrow(str(rowdex), arow) #Replace question marks in row
        for coldex, acell in enumerate(newrow): #Then step through new row
          if questionmark(arow, rowdex, coldex): #And update Google worksheet
            wks.update_cell(rowdex, coldex+1, acell) #Gspread has no "0" column
      else:
        break #Stop grabbing new rows at the first empty one encountered.
    flash('Processed Google Spreadsheet')
  else:
    flash('Please Login to Google')

def questionmark(oldrow, rowdex, coldex):
  """Returns true if a question mark is supposed to be replaced in cell.
  
  This is called for every cell on every row processed and checks whether
  question mark replacemnt should actually occur."""
  if rowdex != 1:
    if globs.row1[coldex] in globs.funcslc:
      if oldrow[coldex] == '?':
        return(True)
  return(False)

def processrow(rowdex, arow):
  """Separates row-1 handling from question mark detection on all other rows.
  
  Called on each row of a worksheet and either initializes functions when it's
  row 1, or steps cell by cell along each subsequent (fed-in) row and when
  encountering a question mark, it determines whether to invoke the function
  indicated by the column label, using values from the active row as parameter
  values if available, parameter defaults if not, and None if not found."""
  changedrow = arow[:]
  if str(rowdex) == '1':
    #Row 1 is always specially handled because it contains function names.
    globs.row1 = [x.lower() for x in changedrow]
    row1funcs(changedrow)
  else:
    #All subsequent rows are checked for question mark replacement requests.
    for coldex, acell in enumerate(changedrow):
      if questionmark(arow, rowdex, coldex):
        changedrow[coldex] = evalfunc(coldex, changedrow)
  return(changedrow)

def row1funcs(arow):
  """Scans row-1 for names of global functions and builds dict of requirements.
  
  This is only invoked on row 1 of a worksheet, where the names of functions
  and parameters are expected to be discovered. By the end, we've created a
  dictionary of dictionaries called globs.fargs which plays an important role
  in building the code necessary for question mark replacement."""
  fargs = {}
  for coldex, fname in enumerate(arow):
    if fname.lower() in globs.funcslc: #Detect if column name is a function
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

def evalfunc(coldex, arow):
  """Builds string to execute to get value to replace question mark with.
  
  Once a question mark is found in a cell belonging to a function-named column,
  the exact invocation that's needed must be built, keeping in mind default
  values provided by function itself, as well as parameter values provided in
  the provided row. Because rows are being handled as lists, order is
  important, and the column index allows function name lookup."""
  fname = globs.transfunc[globs.row1[coldex]]
  fargs = globs.fargs[coldex]
  evalme = "%s(" % fname #Begin building string that will eventually be eval'd
  if fargs:
    #The function we're looking at DOES have required arguments.
    for anarg in fargs: 
      #Add an arg=value to string for each required argument.
      anarg = anarg.lower()
      argval = getargval(anarg, fargs[anarg], arow) 
      evalme = "%s%s=%s, " % (evalme, anarg, argval)
    evalme = evalme[:-2] + ')' #Finish building string for the eval statement.
  else:
    #No arguments required, so just immediately close the parenthesis.
    evalme = evalme + ')' 
  #return('%s: %s' % (evalme, eval(evalme)))
  return(eval(evalme))

def getargval(anarg, defargval, arow):
  """Returns value to set argument equal-to in function invocation string.
  
  This function returns which value should be used as the arguments to the
  function invocation string being built. The value found on the row always
  beats the default provided by the function. Lacking values on the row and a
  default, the Python value of None will be returned."""
  for coldex, acol in enumerate(globs.row1):
    if acol == anarg: #Found column named same thing as a required argument.
      if arow[coldex]: #The cell in that column has a non-zero/empty value.
        return adq(arow[coldex]) #So, we got what we need. Return it.
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

