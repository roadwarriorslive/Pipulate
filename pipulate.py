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
import sys, os, socket, urlparse, re, gspread                       # Hello World! I'm glad you found your way
import globs                                                        # to pipulate.py. While this is not the
from common import *                                                # exact file that kicks off Pipulate, it
import requests, traceback, datetime, time, json                    # is the most important to the process.
from flask_wtf import Form                                          # Those other files, like webpipulate.py
from wtforms import   (StringField, RadioField,                     # and loopipulate.py are merely shims for
                      HiddenField, SelectMultipleField,             # different Python code execution contexts.
                      TextAreaField,                                # Webpipulate creates an instance of the
                      SelectField, widgets)                         # Flask webserving app object, perhaps
from flask import     (Flask,                                       # somewhat controversially directly native
                      stream_with_context,                          # in Python. Yes, there's gunicorn, nginx,
                      render_template,                              # and all that wonderful webserver extra
                      Response,                                     # context, but who needs it? An entire
                      request,                                      # instance of Pipulate, including host OS,
                      session,                                      # Python, all 3rd party dependencies and
                      redirect,                                     # the application itself fit in under 60MB
                      url_for,                                      # of space, making it perfect to run from
                      flash)                                        # small servers, virtual machines or desktop.

from functions import *
from managelists import *

socket.setdefaulttimeout(10.0)                                      
app = Flask(__name__)                                               # Create that fateful instance of a Flask object.

def stream_template(template_name, **context):                      # Pipulate is a non-traditional streaming app
  """Open inexpensive Flask-based streaming."""                     # utilizing Flask's built-in streaming method.
  app.update_template_context(context)                              # Picture building a web user interface that is
  t = app.jinja_env.get_template(template_name)                     # able to update itself immediately following
  rv = t.stream(context)                                            # the initial request that built the form, so
  return rv                                                         # you can witness response data flowing in.

@app.context_processor                                              # context_processor called w/access to templateglobals
def templateglobals():                                              # Every templating system has some price to it
  """Make some functions usable in templates."""                    # and one of Flask's costs is a disconnect
  return dict(loginlink=getLoginlink(),                             # between templates and application functions.
  bookmarklet=getBookmarklet(),                                     # No big deal. We just explicitly add those
  blabel=getLabel(),                                                # that need to be globally available (without
  logoutlink=getLogoutlink(),                                       # explcitly passing as parameters on the
  cyclemotto=cyclemotto()                                           # template call -- another option) here.
  )

class ConfigForm(Form):                                             # Now, we define the forms we're going ot need.
  """Define form for aquiring configuration values."""
  import binascii
  apdef = binascii.hexlify(os.urandom(24))                          # Flask needs application secrets for sessions.
  appsecret = StringField('Flask app secret (auto-generated):', default=apdef)
  clientid = StringField('Client ID (from Google Dev Console):')    # OAuth2 equivalent to username and password.
  clientsecret = StringField('Client secret (from Google Dev Console):')

class PipForm(Form):
  """Define form for main Pipulate user interface."""
  pipurl = StringField('Paste a Google Sheet URL:')                 # Pipulate must know a Google Sheet URL to work.
  magicbox = TextAreaField("magicbox")                              # This box shows the JSON data being worked upon.
  options = SelectField("options")                                  # What you're asking Pipulate to do.

class PipForm2(PipForm):
  """Define form for interstitial options"""
  secondary = HiddenField()
  radios = RadioField(choices=crawlchoices())
  checks = SelectMultipleField(choices=crawlchoices(), 
    option_widget=widgets.CheckboxInput(), 
    widget=widgets.ListWidget(prefix_label=False))

#  _____ _           _                      _
# |  ___| | __ _ ___| | __  _ __ ___   __ _(_)_ __
# | |_  | |/ _` / __| |/ / | '_ ` _ \ / _` | | '_ \
# |  _| | | (_| \__ \   <  | | | | | | (_| | | | | |
# |_|   |_|\__,_|___/_|\_\ |_| |_| |_|\__,_|_|_| |_|
#
@app.route("/", methods=['GET', 'POST'])                            # In web-mode, Pipulate only uses this one point
def main():                                                         # of entry "/", via the Werkzeug routing package.
  """Ensures config and login requirements met."""                  # We always check first whether the server has
  print('''
               ____  _             _       _   _
              |  _ \(_)_ __  _   _| | __ _| |_(_)_ __   __ _
              | |_) | | '_ \| | | | |/ _` | __| | '_ \ / _` |
              |  __/| | |_) | |_| | | (_| | |_| | | | | (_| |  _   _   _
              |_|   |_| .__/ \__,_|_|\__,_|\__|_|_| |_|\__, | (_) (_) (_)
                      |_|                              |___/
  ''')
  out("ENTERED MAIN FUNCTION", "0")                                 # Establish hierarchical indenting of debug system.
  stop = False                                                      # Pipulate "stops" unless permitted to continue.
  streamit = False                                                  # Controls Flask's stream versus render template.
  form = PipForm(csrf_enabled=False)                                # All WTForms are instances of classes. Main form.
  form2 = PipForm2(csrf_enabled=False)
  pipstate = None
  docid = None
  configform = ConfigForm(csrf_enabled=False)                       # The form to let you 1st time configure server.
  if (os.path.isfile(globs.FILE) and                                # been configured or not. Configuration consists
      os.path.getsize(globs.FILE) > 0):                             # of a file with Google OAuth2 Client ID, Client
    app.config.from_pyfile(globs.FILE, silent=False)                # secret, and Flask application secret. Load them.
    app.config['SESSION_TYPE'] = 'filesystem'
  else:
    #                                                   __ _       
    #   ___  ___ _ ____   _____ _ __    ___ ___  _ __  / _(_) __ _ 
    #  / __|/ _ \ '__\ \ / / _ \ '__|  / __/ _ \| '_ \| |_| |/ _` |
    #  \__ \  __/ |   \ V /  __/ |    | (_| (_) | | | |  _| | (_| |
    #  |___/\___|_|    \_/ \___|_|     \___\___/|_| |_|_| |_|\__, |
    #                                                        |___/ 
    if request.method == 'POST':                                    # Final configuration has not yet occurred, but a
      import pickle                                                 # submitted form means that we're sitting on top
      pickleme = {                                                  # of the values, that we can grab and pickle into
        'CLIENT_ID': configform.clientid.data,                      # a temporary location. This pickle file is where
        'CLIENT_SECRET': configform.clientsecret.data,              # the access_token will be stored, but we don't
        'APP_SECRET': configform.appsecret.data                     # have it yet, and don't want to write into the
      }                                                             # config file yet, so we enter this server confg
      pickle.dump(pickleme, open(globs.TOKEN, 'wb'))                # block again for exchanging the initial OAuth2
      redir = globs.DOMURL                                          # "code" that we're about to get for a permanent
      if 'Host' in request.headers:                                 # refresh_token and temporary access_token.
        redir = 'http://'+request.headers['Host']                   # Use a host name if you've got one.
      scope = 'https://spreadsheets.google.com/feeds/'              # Normal pipulate servers don't need much scope, 
      if globs.PCOM:                                                # but if it's the main pipulate.com instance, then
        scope = 'profile email ' + scope                            # I'm going to do a little bit of user tracking.
      qsdict = {  'scope': scope,                                   # Here, we begin to construct the URL parameters
                  'response_type': 'code',                          # for a simple GET-method request to the Google
                  'access_type': 'offline',                         # OAuth2 authentication service. It is going to
                  'redirect_uri': redir,                            # return to the redirect_uri with a code parameter
                  'approval_prompt': 'force',                       # appended onto it that we'll use immediately
                  'client_id': configform.clientid.data             # below when the next elif traps that condition.
                }
      from urllib import urlencode
      linktologin = "%s?%s" % (globs.OAUTHURL, urlencode(qsdict))
      return redirect(linktologin) 
    elif request.args and 'code' in request.args:                   # Trap condition where "code" is found in querystring
      import pickle
      writeus = pickle.load(open(globs.TOKEN, "rb"))
      code = request.args['code']
      scope = 'https://spreadsheets.google.com/feeds/'
      redir = globs.DOMURL
      if 'Host' in request.headers:
        redir = 'http://'+request.headers['Host']
      endpoint = "https://www.googleapis.com/oauth2/v3/token" # Notice the new endpoint for this exchange.
      postheaders = {
        'client_id': writeus['CLIENT_ID'],
        'client_secret': writeus['CLIENT_SECRET'],
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': redir
        } # Construct POST header values for exchanging initial OAuth2 code for refresh and access tokens.
      r = requests.post(endpoint, postheaders)
      rd = r.json()
      output = open(globs.FILE, 'wb') # Copy temporarily pickled values to permanent Flask server config file.
      output.write("CLIENT_ID = '%s'\n" % writeus['CLIENT_ID'])
      output.write("CLIENT_SECRET = '%s'\n" % writeus['CLIENT_SECRET'])
      output.write("SECRET_KEY = '%s'\n" % writeus['APP_SECRET'])
      output.write("REFRESH_TOKEN = '%s'\n" % rd['refresh_token'])
      output.close()
      from datetime import datetime, timedelta
      xseconds = rd['expires_in']
      expiresin = datetime.now() + timedelta(seconds=xseconds)
      pickleme = {
        'access_token': rd['access_token'],
        'expires': expiresin
      }
      pickle.dump(pickleme, open(globs.TOKEN, 'wb')) # Pickle the frequenlty-changed access token
    else: # Config file not found, nor POST method or "code" on querystring.
      return render_template('pipulate.html', configform=configform) # Start server configuration procedure.
  if session and 'oa2' in session: # Appears that user is logged in already.
    #       _               _          _               _    
    #   ___| |__   ___  ___| |_    ___| |__   ___  ___| | __
    #  / __| '_ \ / _ \/ _ \ __|  / __| '_ \ / _ \/ __| |/ /
    #  \__ \ | | |  __/  __/ |_  | (__| | | |  __/ (__|   < 
    #  |___/_| |_|\___|\___|\__|  \___|_| |_|\___|\___|_|\_\
    #                                                       
    session.permanent = True
    creds = Credentials(access_token=session['oa2'])
    try:
      gsp = gspread.authorize(creds)
      gsp.openall()                                       # so, see if we can get a list of docs,
      session['loggedin'] = "1"
    except:
      session.pop('loggedin', None)                       # and if we can't, get rid of login clue.
      if 'u' not in session and globs.PIPURL:
        session['u'] = globs.PIPURL
    if session and 'loggedin' in session and session['loggedin'] == "1":
      needsPipulate = True
      if request.args and 'u' in request.args and globs.SHEETS in request.args.get('u'):
        needsPipulate = False
      elif request.method == 'POST':
        needsPipulate = False
      else:
        try:
          gdoc = gsp.open(globs.SHEET)
          docid = gdoc.id
          pipstate = {'ROW1': gdoc.sheet1.row_values(1), 'ROW2': gdoc.sheet1.row_values(2)}
          needsPipulate = False
        except:
          pass
      # Indoctrinate new Pipulate users here
      if request.args and 'logout' in request.args:
        pass
      elif request.args and 'code' in request.args:
        pass
      elif needsPipulate and 'access_token' not in request.args:
        out("EXITING MAIN FUNCTION RENDER INDOCTRINATE", "0", '-')
        return render_template('pipulate.html', form=form, select=None)
  stext = ''
  if request.method == 'POST':
    #  ____  _                              _ 
    # / ___|| |__   __ _ ______ _ _ __ ___ | |
    # \___ \| '_ \ / _` |_  / _` | '_ ` _ \| |
    #  ___) | | | | (_| |/ / (_| | | | | | |_|
    # |____/|_| |_|\__,_/___\__,_|_| |_| |_(_)
    #                                         
    if form2.secondary.data == 'on':
      gotcha("hit")
    if form.pipurl.data:
      globs.PIPURL = form.pipurl.data
      if form.options.data:
        globs.PIPMODE = form.options.data
        if ':' in globs.PIPMODE:
          mode = globs.PIPMODE.split(':')[1]
          return render_template('pipulate.html', form=form, form2=form2, mode=mode)
      if form.magicbox.data:
        globs.KEYWORDS = form.magicbox.data
        form.magicbox.data = None
      streamit = stream_with_context(Pipulate())
    else:
      flash('Please enter a URL to Pipulate.')
  else:
    #  ___                                _        _             
    # |__ \__ _ _   _  ___ _ __ _   _ ___| |_ _ __(_)_ __   __ _ 
    #   / / _` | | | |/ _ \ '__| | | / __| __| '__| | '_ \ / _` |
    #  |_| (_| | |_| |  __/ |  | |_| \__ \ |_| |  | | | | | (_| |
    #  (_)\__, |\__,_|\___|_|   \__, |___/\__|_|  |_|_| |_|\__, |
    #        |_|                |___/                      |___/ 
    if request.args and 's' in request.args: # User highlighted text on page before clicking bookmarklet
      form.magicbox.data = request.args.get('s')
      stext = request.args.get('s')
    elif session and 's' in session: # Selected text made the journey through login
      form.magicbox.data = session['s']
      stext = session['s']
    if request.args and 'access_token' in request.args: # Oops... necessary evil. Redirect quickly.
      try:
        LogUser(request.args['access_token'])
      except:
        pass
      session['oa2'] = request.args.get("access_token")
      session['loggedin'] = "1"
      session['i'] -= 1 # Don't skip a cute message, just becuse I redirect.
      if 'u' in session and 's' in session:
        out("EXITING MAIN FUNCTION REDIRECT WITH URL AND TEXT", "0", '-')
        return redirect(url_for('main', u=session['u'], s=session['s'], l='1'))
      elif 'u' in session:
        out("EXITING MAIN FUNCTION REDIRECT WITH URL", "0", '-')
        return redirect(url_for('main', u=session['u'], l='1'))
      else:
        out("Redirecting, no URL known")
        out("EXITING MAIN FUNCTION REDIRECT", "0", '-')
        return redirect(url_for('main'), l='1')
    elif request.args and 'logout' in request.args: # Logging out
      if session:
        if 'oa2' in session:
          revokeurl = 'https://accounts.google.com/o/oauth2/revoke?token=' + session['oa2']
          requests.get(revokeurl, timeout=5)
        if 'u' in request.args:
          form.pipurl.data = request.args.get('u')
        session.pop('loggedin', None)
    elif request.args: # Move selected text and current url into session object.
      try:
        if 's' in request.args:
          session['s'] = request.args.get('s')
        if 'u' in request.args:
          form.pipurl.data = request.args.get('u')
          session['u'] = request.args.get('u')
        if session and 'u' in session:
          form.pipurl.data = session['u']
      except:
        pass
  #      _                                          _               _   
  #  ___| |_ _ __ ___  __ _ _ __ ___     ___  _   _| |_ _ __  _   _| |_ 
  # / __| __| '__/ _ \/ _` | '_ ` _ \   / _ \| | | | __| '_ \| | | | __|
  # \__ \ |_| | |  __/ (_| | | | | | | | (_) | |_| | |_| |_) | |_| | |_ 
  # |___/\__|_|  \___|\__,_|_| |_| |_|  \___/ \__,_|\__| .__/ \__,_|\__|
  #                                                    |_|              
  out("Selecting template method.")
  options = menumaker()
  if form.magicbox.data:
    flash("Congratulations! You have chosen to harvest keywords.") 
    flash("The words filled into the above textarea will be inserted into %s." % globs.SHEET)
    flash("Insert commas between keywords, and each one will get its own row.")
    flash("You can also add more keyword variations by just typing them in.")
    flash('Then select "Harvest Keywords" from the dropdown menu.')
    flash('You can then find your keywords under the Harvest tab.')
  elif pipstate:
    form.magicbox.data = pipstate
    doclink = '%s/d/%s/edit#gid=0' % (globs.SHEETS, docid)
    flash("Welcome to Pipulate, an SEO tool that outputs jobs into Google Docs.")
    flash('You are about to perform changes to the Google Sheet named <a target="_new" href="%s">%s</a>.' % (doclink, globs.SHEET))
    flash("The text in box above represents the data in the first two rows of that sheet.")
    flash("{'ROW1': [], 'ROW2': []} means Sheet1 is empty and ready for a crawl or setup.")
    flash('If it\'s not empty, you can choose "Clear Sheet 1" to blank it in preparation.')
    flash('Pipulate lets you see the <a href="https://en.wikipedia.org/wiki/JSON">JSON data</a> flying around behind the scenes.')
  if streamit:
    #Handle streaming user interface updates resulting from a POST method call.
    return Response(stream_template('pipulate.html', form=form, select=options, data=streamit))
  else:
    #Handle non-streaming user interface build resulting from a GET method call.
    out("EXITING MAIN FUNCTION RENDER", "0", '-')
    return render_template('pipulate.html', form=form, select=options)
  out("EXITING MAIN", "0", '-')

def LogUser(authkey):
  """Track usage of the Pipulate bookmarklet per user on main domain instance."""
  import os.path
  if os.path.isfile(globs.TOKEN) and os.path.getsize(globs.TOKEN) > 0:
    token = freshtoken(globs.TOKEN)
    reds = Credentials(access_token=token)
    import gspread
    gsp2 = gspread.authorize(creds)
    api = 'https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token='
    api = api + authkey
    ujson = requests.get(api, timeout=5)
    adict = ujson.json()
    try:
      usersheet = gsp2.open("Users").sheet1
      emails = usersheet.col_values(1)
    except:
      return
    email = ''
    if "email" in adict:
      email = adict["email"].lower()
    if email in emails:
      emaildex = emails.index(email) + 1
      userange = 'H%s:I%s' % (emaildex, emaildex)
      try:
        CellList = usersheet.range(userange)
        CellList[0].value = timestamp()
        CellList[1].value = str(int(CellList[1].value) + 1)
        usersheet.update_cells(CellList)
      except:
        return
    else:
      user = []
      if 'email' in adict:
        user.append(adict["email"].lower())
      for item in ['name', 'link', 'locale', 'gender', 'id']:
        try:
          user.append(adict[item])
        except:
          user.append('')
      user.append(timestamp())
      user.append('')
      user.append('1')
      try:
        InsertRows(usersheet, [user], len(emails))
      except:
        return
  else:
    out("%s not found. Run python configure.py" % globs.FILE)

#  ____  _             _       _
# |  _ \(_)_ __  _   _| | __ _| |_ ___
# | |_) | | '_ \| | | | |/ _` | __/ _ \
# |  __/| | |_) | |_| | | (_| | ||  __/
# |_|   |_| .__/ \__,_|_|\__,_|\__\___|
#         |_|
#
def Pipulate(dockey='', token=''):
  """Generator that streams output to a web user interface."""
  stop = False
  qset = set()
  qstart = 1
  qend = 1
  badtuple = (globs.GBAD, globs.GBAD, "", "")
  lock = ("", "", "", "+")
  unlock = ("", "", "", "-")
  out("PIPULATION BEGINNING", "1")
  try:
    if globs.WEB: yield "Beginning to Pipulate...", "", "", ""
    if globs.WEB: yield "spinon", "", "", ""
    out("Reading in functions.")
    funcs = [x for x in globals().keys() if x[:2] != '__'] #List all functions
    transfuncs = ziplckey(funcs, funcs) #Keep translation table
    blankrows = 0
    gsp = None
    gdoc = None
    if session or (dockey and token):
      out("LOGIN ATTEMPT", "2")
      sheet = ''
      if dockey and token:
        creds = Credentials(access_token=token)
        gsp = gspread.authorize(creds)
        gdoc = gsp.open_by_key(dockey)
      else:
        if 'oa2' in session:
          creds = Credentials(access_token=session['oa2'])
          out("Credential object created.")
        else:
          out("Expired login.")
          if globs.WEB: 
            yield "Google Login expired. Log back in.", "Login under the \"burger button\" in the upper-right.", "", ""
            yield "spinoff", "", "", ""
        try:
          gsp = gspread.authorize(creds)
        except:
          out("Login failed.")
          if globs.WEB: 
            yield "Google Login unsuccessful.", "", "", ""
            yield "spinoff", "", "", ""
          raise StopIteration
        else:
          out("Login successful.")
        out("Opening Spreadsheet...")
        if globs.WEB: yield("Opening Spreadsheet...", "", "", "")
        stop = True
        sheet = ''
        for x in range(10):
          if globs.WEB: yield lock
          try:
            gdoc = gsp.open_by_url(globs.PIPURL)
            stop = False
            break
          except gspread.httpsession.HTTPError, e:
            out("Login appeared successful, but rejected on document open attempt.")
            yme = 'Please <a href="%s">Log In</a> again first.' % getLoginlink()
            if globs.WEB: yield yme, "Login under the \"burger button\" in the upper-right.", "", ""
            if session and 'loggedin' in session:
              session.pop('loggedin', None)
            if 'u' not in session and globs.PIPURL:
              session['u'] = globs.PIPURL
            break
          except gspread.exceptions.NoValidUrlKeyFound:
            try:
              gdoc = gsp.open(globs.SHEET)
              stop = False
              break
            except gspread.httpsession.HTTPError, e:
              out("No token found, session expired. Switch to HTML5 localStorage.")
              if globs.WEB: 
                yield "I am sorry, the sesson has expired. Please log back in.", "Log back in", "", ""
                yield "spinerr", "", "", ""
                break
            except:
              gotcha('c')
              if globs.WEB: 
                yield "I see you're on a URL that is not a Google Spreadsheet. Would you like to grab links?", "", "", ""
                yield "If so, just <a href='https://docs.google.com/spreadsheets/create' target='_new'>create</a> a new Spreadsheet, name it \"Pipulate\" and click Pipulate again.", "Google Spreadsheet Not Found.", "", ""
                yield 'New to this odd but awesome approach? Watch the <a target="_blank" href="http://goo.gl/v71kw8">Demo</a> and read the <a target="_blank" href="http://goo.gl/p2zQa4">Docs</a>.', "", "", ""
          except gspread.exceptions.SpreadsheetNotFound:
            if globs.WEB: yield "Please give the document a name to force first save.", "", "", ""
          except Exception as e:
            if globs.WEB: yield dontgetfrustrated(x)
            out("Retry login %s of %s" % (x, 10))
            time.sleep(6)
        if stop:
          if globs.WEB: 
            yield "spinerr", "", "", ""
            yield badtuple
          Stop() # Consider adding refresh_token logic for users (versus the scheduler)
      if globs.WEB: yield unlock
      out("Google Spreadsheet successfully opened.")

      if globs.PIPMODE == 'learn':
        out("<script>alert('hit');</script>")

      if (globs.PIPMODE == 'keywords'
        and globs.KEYWORDS 
        and globs.KEYWORDS[:1] != '[' 
        and globs.KEYWORDS[-1:] != ']'
        and globs.KEYWORDS[:1] != '{' 
        and globs.KEYWORDS[-1:] != '}'
        ):
        # Keywords Tab
        if globs.WEB: yield "Keyword Collection Detected", "Making Keywords Tab If Needed", "", ""
        headers = ['Keyword', 'Source']
        if globs.WEB: yield lock
        offset = 0
        newTab = False
        try:
          newTab = InitTab(gdoc, 'Harvest', headers)
        except:
          pass
        if newTab:
          offset = -1
        if globs.WEB: yield unlock
        ksheet = gdoc.worksheet("Harvest")
        kcount = ksheet.row_count + offset
        kwlist = globs.KEYWORDS.split(',')
        kwrows = []
        yme = "Collecting %s keywords." % len(kwlist)
        if globs.WEB: yield yme, "Collecting keywords", "", ""
        for kw in kwlist:
          kwrows.append([kw.strip(), globs.PIPURL])
        try:
          InsertRows(ksheet, kwrows, kcount)
        except:
          pass
        if globs.WEB:
          yield "Keywords Harvested!", "Mmmmmm, more keywords.", "", ""
          yield "spinoff", "", "", ""
        return
      #           _                       _               _     _
      #  ___  ___| |_   _   _ _ __    ___| |__   ___  ___| |_  / |
      # / __|/ _ \ __| | | | | '_ \  / __| '_ \ / _ \/ _ \ __| | |
      # \__ \  __/ |_  | |_| | |_) | \__ \ | | |  __/  __/ |_  | |
      # |___/\___|\__|  \__,_| .__/  |___/_| |_|\___|\___|\__| |_|
      #                      |_|
      # This is where special behavior like crawls get wedged in
      anything = re.compile('.+')
      cell = None
      if globs.PIPMODE == 'clear':
        anything = re.compile('.+')
        if globs.PIPMODE == 'clear':
          out("Clearing Tab 1...")
          if globs.WEB: yield "Clearing Sheet 1. Use revision history if a mistake.", "Clearing Sheet 1", "", ""
          try:
            CellList = gdoc.sheet1.findall(anything)
            for cell in CellList:
              cell.value = ''
            result = gdoc.sheet1.update_cells(CellList)
            if globs.WEB:
              yme = "Sheet1 Cleared! %s" % globs.PBNJMAN
              yield yme, "Sheet1 Cleared.", "", ""
              yield "spinoff", "", "", ""
            Stop()
          except:
            out("Could not clear tap one.")
            Stop()
      else:
        try:
          bothrows = sheetinitializer(globs.PIPMODE) # Beware! There is always an initialization attempt.
          row1 = bothrows[0]
          row2 = [bothrows[1]]
          if globs.WEB: yield lock
          try:
            InitTab(gdoc, "sheet1", row1, row2)
          except:
            pass
          if globs.WEB: yield unlock
        except:
          # yme = "Action for %s not defined." % globs.PIPMODE
          # if globs.WEB: yield yme, "Action not defined.", "", ""
          pass
      if globs.WEB: yield "Checking Tabs.", "Then we check for tabs...", "", ""
      # Documentation Tab
      headers = ['FunctionName', 'Category', 'RequiredColumns', 'Description', 'MoreInfo']
      InitTab(gdoc, 'Docs', headers, documentation())

      # Config Tab
      headers = ['NAME', 'VALUE']
      config = []
      config.append(['RepeatJobEvery','day'])
      config.append(['MaxRowsPerHour','3'])
      if globs.WEB: yield lock
      try:
        InitTab(gdoc, 'Config', headers, config)
      except:
        Stop()
      if globs.WEB: yield unlock

      # Scrapers Tab
      headers = ['name', 'type', 'pattern']
      InitTab(gdoc, 'Scrapers', headers, scrapes())
      sst = None
      out("Loading Scrapers.")
      stop = True
      for x in range(5):
        if globs.WEB: yield lock
        try:
          sst = gdoc.worksheet("Scrapers")
          stop = False
          break
        except:
          if globs.WEB: yield dontgetfrustrated(x)
          out("Retry get Scraper sheet %s of %s" % (x, 5))
          time.sleep(3)
      if stop:
        if globs.WEB: yield badtuple
        Stop()
      if globs.WEB: yield unlock

      try:
        out("Reading Config tab into globals.")
        globs.config = RefreshConfig(gdoc, "Config") #HTTPError
      except:
        out("Copying Config tag to globals failed.")
      else:
        out("Config tab copied to globals.")

      out("Counting rows in Pipulate tab.")
      stop = True
      for x in range(5):
        if globs.WEB: yield lock
        try:
          globs.sheet = gdoc.sheet1
          stop = False
          break
        except:
          if globs.WEB: yield dontgetfrustrated(x)
          out("Retry get Pipulate sheet %s of %s" % (x, 10))
          time.sleep(5)
      if stop:
        if globs.WEB: yield badtuple
        Stop()
      if globs.WEB: yield unlock

      stop = True
      for x in range(5):
        if globs.WEB: yield lock
        try:
          CellList = globs.sheet.findall("?")
          for cell in CellList:
            qset.add(cell.row)
          stop = False
          break
        except:
          if globs.WEB: yield dontgetfrustrated(x)
          out("Retry get rows with question marks %s of %s" % (x, 10))
          time.sleep(5)
      if stop:
        if globs.WEB: yield badtuple
        Stop()
      if globs.WEB: yield unlock

      stop = True
      for x in range(10):
        if globs.WEB: yield lock
        try:
          globs.numrows = len(globs.sheet.col_values(1)) #!!!UnboundLocalError HTTPError OPTIMIZE!
          stop = False
          break
        except:
          if globs.WEB: yield dontgetfrustrated(x)
          out("Retry count rows %s of %s" % (x, 10))
          time.sleep(10)
      if stop == True:
        if globs.WEB: yield badtuple
        Stop()
      if globs.WEB: yield unlock

      yme = "%s rows found in Pipulate tab." % globs.numrows
      out(yme)
      if globs.WEB: yield yme, "", "", ""
      if globs.numrows == 0 and globs.PIPMODE == 'qmarks':
        if globs.WEB:
          yield "Double-check that sheet is set up correctly.", "Pipulate needs question marks to replace.", "", ""
          yield "spinoff", "", "", ""
        return

      stop = True
      for x in range(5):
        try:
          lod = sst.get_all_records() #Returns list of dictionaries
          stop = False
          break
        except:
          if globs.WEB: yield dontgetfrustrated(x)
          out("Retry count rows %s of %s" % (x, 10))
          time.sleep(10)
      if stop == True:
        if globs.WEB: yield badtuple
        Stop()
      if globs.WEB: yield unlock
      pat = [[d['pattern']][0] for d in lod]
      typ = [[d['type']][0] for d in lod]
      nam = [[d['name']][0] for d in lod]
      scrapetypes = ziplckey(nam, typ)
      scrapepatterns = ziplckey(nam, pat)
      transscrape = ziplckey(nam, nam)
      out("Scrapers loaded.")

      if globs.WEB: yield "Analyzing spreadsheet for request...", "Reading spreadsheet...", "", ""

      out("Loading row1 into globals.")
      stop = True
      for x in range(10):
        if globs.WEB: yield lock
        try:
          globs.row1 = lowercaselist(globs.sheet.row_values(1))
          stop = False
          break
        except:
          if globs.WEB: yield dontgetfrustrated(x)
          out("Retry load Row1 %s of %s" % (x, 10))
          time.sleep(5)
      if stop:
        if globs.WEB: yield badtuple
        Stop()
      if globs.WEB: yield unlock

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
      out("Scan down Pipulate tab looking for ASTERISKS.", "2")

      for rowdex in range(1, globs.numrows+1):
        out("Scanning row %s for asterisks." % rowdex) #This can have a pretty long delay

        stop = True
        for x in range(8):
          if globs.WEB: yield lock
          try:
            onerow = globs.sheet.row_values(rowdex) #!!! HTTPError OPTIMIZE THIS!
            stop = False
            break
          except:
            if globs.WEB: yield dontgetfrustrated(x)
            out("Retry %s of %s" % (x, 8))
            time.sleep(5)
        if stop:
          if globs.WEB: yield badtuple
          Stop()
        if globs.WEB: yield unlock

        if onerow:
          if rowdex == 2: #Looking for trending requests
            if '*' in onerow:
              trended = True
              out("Found asterisks on row 2 -- trending activated!")
              trendlistoflists.append(onerow)
              if globs.WEB: yield "Found asterisks indicating trending in row 2", "Then we look for trending job requests...", json.dumps(onerow), ""
            else:
              break
          elif trendlistoflists and rowdex > 2:
            if '*' in onerow:
              out("Found astrisks on row %s." % rowdex)
              trendlistoflists.append(onerow)
              yme = ", %s" % rowdex
              if globs.WEB: yield yme, "", json.dumps(onerow), ""
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
      yme = "%s-Row trending-job found. Analyzing job frequency." % len(trendlistoflists)
      if globs.WEB: yield yme, "", "", ""
      trendingrowsfinished = True
      maxrowsperhour = 0
      out("Done looking for asterisks", "2", "-")
      #  _   _                   ___                           _
      # | |_(_)_ __ ___   ___   ( _ )     ___ ___  _   _ _ __ | |_
      # | __| | '_ ` _ \ / _ \  / _ \/\  / __/ _ \| | | | '_ \| __|
      # | |_| | | | | | |  __/ | (_>  < | (_| (_) | |_| | | | | |_
      #  \__|_|_| |_| |_|\___|  \___/\/  \___\___/ \__,_|_| |_|\__|
      #
      out("Count and timestamp columns for TRENDING", '2')
      times = []
      if trended and 'count' in globs.row1:
        backintime = globs.numrows - len(trendlistoflists) + 1
        countletter = globs.letter[globs.row1.index('count') + 1]
        mayhaverun = "%s%s:%s%s" % (countletter, backintime, countletter, globs.numrows)
        try:
          CellList = globs.sheet.range(mayhaverun)
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
          try:
            timeletter = globs.letter[globs.row1.index('timestamp') + 1]
          except:
            Stop()
          mayhaverun = "%s%s:%s%s" % (timeletter, backintime, timeletter, globs.numrows)
          try:
            CellList = globs.sheet.range(mayhaverun)
          except:
            out("Failed to load the trending timestamp range.")
          for onecell in CellList:
            times.append(onecell.value)
          trendingrowsfinished = times.count('?') == 0
          if trendingrowsfinished:
            maxrowsperhour = len(trendlistoflists)
            if not counts[0]:
              if globs.WEB: yield "Last set of trending rows complete.", "", "", ""
          if 'maxrowsperhour' in globs.config:
            maxrowsperhour = globs.config['maxrowsperhour']
          try:
            int(maxrowsperhour)
          except:
            maxrowsperhour = 0
          if not trendingrowsfinished:
            qstart = globs.numrows - times.count('?') + 1
            trendlistoflists = []
          nextnum = int(counts[0]) + 1
          for onelist in trendlistoflists:
            onelist[globs.row1.index('count')] = nextnum

      if trended and trendingrowsfinished == True:
        qstart = globs.numrows + 1
        qend = globs.numrows + 1
        qset.add(globs.numrows + 1)
      elif qset:
        qstart = min(qset)
        qend = max(qset) + 1
      else:
        qstart = 1
        qend = globs.numrows + 1
      out("Done count and timestamp columns for trending", '2', '-')
      #  _                     _
      # (_)_ __  ___  ___ _ __| |_   _ __ _____      _____
      # | | '_ \/ __|/ _ \ '__| __| | '__/ _ \ \ /\ / / __|
      # | | | | \__ \  __/ |  | |_  | | | (_) \ V  V /\__ \
      # |_|_| |_|___/\___|_|   \__| |_|  \___/ \_/\_/ |___/
      #
      out("INSERT NEW ROWS for new time increment trending", '2')
      #jobstats = timewindow(times[0])
      if times:
        insert, name, number, left, right, now = timewindow(times[0])
      else:
        insert, name, number, left, right, now = False, False, False, False, False, False
      if name and number:
        tellrow = maxrowsperhour
        if tellrow == 0:
          tellrow = 'all'
        if globs.WEB: yield "Job requested to process %s row(s) every %s %s" % (tellrow, number, name), "", "", ""
      else:
        if globs.WEB: yield "Pipulate running in questionmark replacement mode.", "", "", ""
      if left and right and now:
        if globs.WEB:
          yield "%s = Start of last time window" % left, "", "", ""
          yield "%s = End of last time window" % right, "", "", ""
          yield "%s = Currrent time" % now, "", "", ""
      if trendlistoflists and insert: #This line will show in errors for any Config scheduling screw-ups.
        for x in range(4):
          try:
            InsertRows(globs.sheet, trendlistoflists)
          except:
            if globs.WEB: yield dontgetfrustrated(x)
            out("Error on trending, retry %s" % x)
            time.sleep(2)
          else:
            trendlistoflists = []
            break
      #We need to get it again if trending rows were added. !!! Optimize
      if trended:
        try:
          globs.sheet = gdoc.sheet1
        except:
          if globs.WEB:
            yield "Couldn't reach Google Docs. Try logging in again.", "", "", ""
            yield "spinoff", "", "", ""
          raise StopIteration
        else:
          pass
      globs.numrows = len(globs.sheet.col_values(1))
      if trended:
        qend = globs.numrows + 1
      #globs.numrows = globs.numrows + len(trendlistoflists) #faster
      out("Done insert new rows for new time inrement trending", '2', '-')
      #                        _   _                                    _
      #   __ _ _   _  ___  ___| |_(_) ___  _ __    _ __ ___   __ _ _ __| | _____
      #  / _` | | | |/ _ \/ __| __| |/ _ \| '_ \  | '_ ` _ \ / _` | '__| |/ / __|
      # | (_| | |_| |  __/\__ \ |_| | (_) | | | | | | | | | | (_| | |  |   <\__ \
      #  \__, |\__,_|\___||___/\__|_|\___/|_| |_| |_| |_| |_|\__,_|_|  |_|\_\___/
      #     |_|
      #
      out("QUESTION MARK Replacement.", '2')
      if not qset and not trended:
        if globs.WEB:
          yme = 'New to Pipulate? Watch <a target="_blank" href="https://docs.google.com/presentation/d/10lr_d1uyLMOnWsMzbenKiPlFE5-BIt9bxVucw7O4GSI/edit?usp=sharing">Demo</a> and read <a target="_blank" href="https://github.com/miklevin/pipulate/blob/master/README.md">Docs</a>. ' + globs.PBNJMAN
          yield yme, "The first worksheet in your spreadsheet needs something in it.", "", ""
          yield "spinoff", "", "", ""
        return
      therange = range(qstart, qend)
      blankrows = 0 #Lets us skip occasional blank rows
      for index, rowdex in enumerate(therange): #Start stepping through every row.
        if rowdex in qset:
          if maxrowsperhour: # if maxrowsperhour is 0, this won't trap
            if index >= int(maxrowsperhour):
              break
          yme = "Pipulating row: %s (%s of %s)..." % (rowdex, index+1, len(therange))
          if globs.WEB: yield yme, "Next, we replace question marks. This may take awhile...", "", ""
          globs.hobj = None
          globs.html = '' #Blank the global html object. Recylces fetches.
          rowrange = "A%s:%s%s" % (rowdex, globs.letter[len(globs.row1)], rowdex)

          stop = True
          for x in range(5):
            if globs.WEB: yield lock
            try:
              CellList = globs.sheet.range(rowrange)
              stop = False
            except:
              out("Retry %s of %s" % (x, 5))
              time.sleep(2)
              if globs.WEB: yield dontgetfrustrated(x)
          if stop:
            if globs.WEB: yield "GData Timed Out","Sorry, GDATA Failed. Try again.","",""
            Stop()
          if globs.WEB: yield unlock

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
            if globs.WEB: yield "", "", json.dumps(onerow), ""
            rowdexstring = str(rowdex)
            newrow = onerow[:]
            if rowdexstring > 1:
              #All subsequent rows are checked for question mark replacement requests.
              for coldex, acell in enumerate(newrow):
                if questionmark(onerow, rowdexstring, coldex):
                  if 'url' in globs.row1: #Only fetch html once per row if possible
                    if globs.WEB: yield lock
                    try:
                      globs.html = gethtml(onerow[globs.row1.index('url')])
                    except:
                      pass
                    if globs.WEB: yield unlock
                  collabel = globs.row1[coldex]
                  if collabel in transfuncs.keys():
                    stop = True
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
                        stop = False
                        out('%s worked' % collabel)
                        yme = "<li>%s</li>" % (collabel)
                        if globs.WEB:
                          yield yme, yme, "", ""
                        break
                      except Exception as e:
                        print traceback.format_exc()
                        time.sleep(2)
                      if stop == True:
                        out("Function End (Failed)", "4", '-')
                        if globs.WEB:
                          yield "spinerr", "", "", ""
                        Stop()
                    out("Function End", "4", '-')
                  elif collabel in transscrape.keys():
                    stop = True
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
                          if globs.WEB: yield lock
                          html = gethtml(url)
                          if not html:
                            if globs.WEB:
                              yield "HTML not available. Possible Content-Type error. Continuing.", "Skipping this row and trying next row.", "", ""
                            out("HTML NOT AVAILABLE")
                            newrow[coldex] = "<Error>HTML Not Available</Error>"
                            stop = False
                            break
                          if globs.WEB: yield unlock
                          #add another elif condition for PyQuery https://pypi.python.org/pypi/pyquery
                          if stype.lower() == 'xpath':
                            import lxml.html
                            searchme = lxml.html.fromstring(html)
                            try:
                              match = searchme.xpath(spattern)
                            except lxml.etree.XPathEvalError:
                              out("BAD XPATH PATTERN")
                              yme = "Bad xpath: %s" % spattern
                              if globs.WEB: yield yme, "Bad XPATH Pattern!", "", ""
                              Stop()
                            except:
                              out("OTHER LXML ERROR")
                              if globs.WEB: yield "LXML parser problem. Check URL source", "LXML Problem!", "", ""
                              Stop()
                            if match:
                              if len(match) == 1:
                                newrow[coldex] = match[0]
                              else:
                                frag = ''
                                for item in match:
                                  if item.__class__.__name__ in ('HtmlElement', 'HtmlComment'):
                                    frag += stringify_children(item)
                                  else:
                                    try:
                                      frag += item
                                    except:
                                      pass
                                  frag += '\r\n'
                                newrow[coldex] = frag
                            else:
                              newrow[coldex] = "<Error>no match</Error>"
                          elif stype.lower() == 'regex':
                            match = re.search(spattern, html, re.S | re.I)
                            if match:
                              if "scrape" in match.groupdict().keys():
                                newrow[coldex] = match.group("scrape").strip()
                              else:
                                newrow[coldex] = None
                            else:
                              newrow[coldex] = None
                        out('%s worked.' % collabel)
                        yme = "<li>%s</li>" % (collabel)
                        if globs.WEB: yield yme, yme, "", ""
                        stop = False
                        break
                      except Exception as e:
                        print traceback.format_exc()
                        out("Scrape problem on row %s. Retrying." % rowdexstring)
                        time.sleep(2)
                        if globs.WEB: yield dontgetfrustrated(x)
                      if stop == True:
                        out("Scrape End (Failed)", "4", '-')
                        Stop()
                    out("Scrape End", "4", '-')
            out("DONE PROCESSING ROW %s." % rowdex, '3', '-')

            out("Finished processing row. Updating spreadsheet...")
            newrow = ['' if x==None else x for x in newrow]
            if len(str(newrow)) > globs.ROWMAX:
              if globs.WEB: yield "", "", "['TOO BIG']", ""
            else:
              try:
                if globs.WEB: yield "", "", json.dumps(newrow), ""
              except:
                if globs.WEB: yield "", "", newrow, ""
            for index, onecell in enumerate(CellList):
              onecell.value = newrow[index]
            result = None

            stop = True
            for x in range(10):
              if globs.WEB: yield lock
              try:
                result = globs.sheet.update_cells(CellList)
                stop = False
                break
              except:
                out("Writing row to spreadsheet, retry %s of %s" %(x, 10))
                time.sleep(5)
                if globs.WEB: yield dontgetfrustrated(x)
            if stop:
              if globs.WEB: yield badtuple
              Stop()
            if globs.WEB: yield unlock

          elif onerow.count('') == len(onerow):
            blankrows += 1
            if blankrows > 1:
              break
      out("Done question Mark Replacement.", '2', '-')

    else: #No session object found
      if globs.WEB: yield 'Please Login to Google', "", "", ""
    if globs.WEB:
      yme = 'Pipulation complete. Now, do a little victory dance. %s' % globs.PBNJMAN
      yield yme, 'Congratulations, pipulation complete!', "", ""
      yield "spinoff", "", "", ""
    out("PIPULATION OVER", "1", '-')
  except Exception as e:
    exceptiondata = traceback.format_exc()
    print(exceptiondata)
    exceptionlines = exceptiondata.splitlines()
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    ename = type(e).__name__
    fixme = "Error: %s, File: %s, Line: %s" % (ename, fname, exc_tb.tb_lineno)
    out(fixme)
    out("Pipulation Failure")
    if ename == "StopIteration":
      loginmsg = ""
      if session and 'loggedin' in session and session['loggedin'] != '1':
        loginmsg = "Login link under the upper-left \"burger button\"."
      # if globs.WEB: yield "Session timed out. Try again", "If at first you don't succeed, pipulate again.", "", ""
    else:
      if globs.WEB:
        yield exceptionlines[-1], "", "", ""
        yield fixme, "", "", ""
        yield "Pipulation prematurely terminated.", "", "", ""
        yield "Please open an issue at https://github.com/miklevin/pipulate", "", "", ""
        yield "Or just tap me on the shoulder.", "", "", ""
        if globs.PIPMODE != 'clear':
          yield "spinerr", "", "", ""
    out("PIPULATION ERROR", "1", '-')
  out("EXITING MAIN", "0", '-') #Special case of function exit reporting
  print("\n")

def url_root(url):
  """Return root domain from url"""
  parsed = urlparse.urlparse(url)
  return "%s://%s%s" % (parsed[0], parsed[1], parsed[2])

def getLoginlink():
  """Return the HTML code required for an OAuth2 login link."""
  redir = globs.DOMURL
  if 'Host' in request.headers:
    redir = 'http://'+request.headers['Host']
  try:
    if session and request.args and 'u' in request.args:
      session['u'] = request.args.get('u')
  except:
    pass
  scope = 'https://spreadsheets.google.com/feeds/'
  if globs.PCOM:
    scope = 'profile email ' + scope
  baseurl = globs.OAUTHURL
  cid = ''
  if 'CLIENT_ID' in app.config:
    cid = app.config['CLIENT_ID']
  qsdict = {  'scope': scope,
              'response_type': 'token',
              'redirect_uri': redir,
              'client_id': cid
            }
  from urllib import urlencode
  return "%s?%s" % (baseurl, urlencode(qsdict))

def getLabel():
  url = request.base_url
  parsed = urlparse.urlparse(url)
  subdomain = parsed.hostname.split('.')[0]
  blab = globs.SHEET
  droidcut = "ppp"
  if subdomain == 'localhost':
    blab = "%s %s 8888" % (droidcut, globs.SHEET)
  elif subdomain == 'pipulate':
    blab = '%s %s' % (droidcut, globs.SHEET)
  elif subdomain:
    blab = "%s %s %s" % (droidcut, globs.SHEET, subdomain)
  return blab

def getBookmarklet():
  """Return the HTML required to create a draggable Pipulate bookmarklet link."""
  host = request.headers['Host']
  bname = globs.SHEET
  #return '''javascript:(function(){window.open('http://%s/?u='+encodeURIComponent(document.location.href)+'&d='+Date.now()+'&s='+encodeURIComponent(window.getSelection?window.getSelection():document.selection.createRange().text)+'&c='+window.btoa(unescape(encodeURIComponent(document.cookie))), '%s', 'toolbar=0,resizable=1,scrollbars=1,status=1,width=630,height=600');})();''' % (host, bname)
  return '''javascript:(function(){open('http://%s/?u='+encodeURIComponent(document.location.href)+'&d='+Date.now()+'&s='+encodeURIComponent(window.getSelection?window.getSelection():document.selection.createRange().text)+'&c='+window.btoa(unescape(encodeURIComponent(document.cookie))));})();''' % (host)

def getLogoutlink():
  """Return the HTML required to clear and expire the current OAuth2 token."""
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

def RefreshConfig(gdoc, sheetname):
  #!!! Needs optimization

  stop = True
  for x in range(5):
    try:
      onesheet = gdoc.worksheet(sheetname)
      stop = False
      break
    except:
      out("Retry %s of %s" %(x, 5))
      time.sleep(2)
  if stop:
    Stop()

  stop = True
  for x in range(5):
    try:
      names = onesheet.col_values(1)
      stop = False
      break
    except:
      out("Retry %s of %s" %(x, 5))
      time.sleep(2)
  if stop:
    Stop()

  stop = True
  for x in range(5):
    try:
      values = onesheet.col_values(2)
      stop = False
      break
    except:
      out("Retry %s of %s" %(x, 5))
      time.sleep(2)
  if stop:
    Stop()

  return ziplckey(names, values)

def ziplckey(keys, values):
  keys = lowercaselist(keys)
  return dict(zip(keys, values))

def lowercaselist(onelist):
  for index, item in enumerate(onelist):
    try:
      onelist[index] = item.lower().strip()
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
  if 'repeatjobevery' in globs.config:
    intervallanguage = globs.config['repeatjobevery'].strip()
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
    try:
      tick = datetime.datetime.strptime(amiinnewtimewindow, "%m/%d/%Y %H:%M:%S")
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

def InitTab(gdoc2, tabname, headerlist, listoflists=[]):
  initsheet = None
  isSheet1 = False
  for x in range(3): #not too many times here (always tried for new tabs too)
    if tabname == "sheet1":
      isSheet1 = True
      try:
        initsheet = gdoc2.sheet1
      except:
        out("Retrying connecting to Sheet 1")
        time.sleep(1)
    else:
      try:
        initsheet = gdoc2.worksheet(tabname)
        out("%s Tab exists." % tabname)
        break
      except:
        out("Retrying make %s Tab %s of %s" % (tabname, x, 3))
        time.sleep(1) #not too long here

  if isSheet1 or not initsheet:
    numcols = len(headerlist)
    if listoflists and len(listoflists) > 1 and '*' in listoflists[1]:
      numrows = len(listoflists)+1
    elif listoflists:
      numrows = len(listoflists)+2
    else:
      numrows = 2
    endletter = globs.letter[numcols]
    if isSheet1:
      newtab = gdoc2.sheet1
    else:
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

    stop = True
    for x in range(5):
      try:
        newtab.update_cells(CellList)
        stop = False
        break
      except:
        out("Retry %s of %s" % (x, 5))
        time.sleep(5)
    if stop:
      Stop()
    return True
  else:
    return False

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
    path = urlparse.urlparse(url).path
    ext = os.path.splitext(path)[1]
    if ext not in globs.texttypes:
      try:
        defend = requests.head(url)
      except:
        return None
      if 'Content-Type' in defend.headers:
        ct = defend.headers['Content-Type']
      else:
        return None
      if ct != '' and 'text' not in ct:
        return None
    try:
      globs.hobj = requests.get(url, timeout=(5, 10))
    except:
      return None
    globs.html = globs.hobj.text
  return globs.html

def html(url):
  return gethtml(url)

def convertisotime(timestamp):
  i = datetime.datetime(*map(int, re.split('[^\d]', timestamp)[:-1]))
  return i.strftime("%m/%d/%Y %H:%M:%S")

def timestamp():
  i = datetime.datetime.now()
  return i.strftime("%m/%d/%Y %H:%M:%S")

def datestamp():
  now = datetime.datetime.now()
  now = now.strftime("%B %d, %Y")
  return now

def extension(url):
  """Return the file extension, given (typically) a URL."""
  if url:
    path = urlparse.urlparse(url).path
    ext = os.path.splitext(path)[1]
    return ext
  else:
    return None

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
    return "r'%s'" % (aval) #ALMOST everything else should be quoted.

def stringify_children(node):
  from lxml.etree import tostring
  from itertools import chain
  parts = ([node.text] + list(chain(*([c.text, tostring(c, with_tail=False), c.tail] for c in node.getchildren()))) + [node.tail])
  # filter removes possible Nones in texts and tails
  return ''.join(filter(None, parts))


