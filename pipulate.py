"""    Because life's too short to not collect  ABOUT THE AUTHOR:      # From Pipulate, Import *
       data in the same place you work with it  http://mikelev.in
        _____ _             _       _           http://levinux.com     - What is Pipulate and why? It's...
       |  __ (_)           | |     | |          http://pipulate.com    - An attempt to scratch my own itch
       | |__) | _ __  _   _| | __ _| |_ ___    ___ ___  _ __ ___       - So that I can structure my mind better
       |  ___/ | '_ \| | | | |/ _` | __/ _ \  / __/ _ \| '_ ` _ \      - So that I can structure my behavior better
       | |   | | |_) | |_| | | (_| | ||  __/ | (_| (_) | | | | | |     - So that I can remember more and forget less
       |_|   |_| .__/ \__,_|_|\__,_|\__\___|(_)___\___/|_| |_| |_|     - So that I can achieve more while straining less
               | |                                                     - So that I can improve my life and impact the world
          THIS |IS YOUR BROWSER                                        - So that I can help teach others to do the same
 THIS IS      \   /                               THIS IS PIPULATE     - So that I can turn a life's work into legacy
   YOU         \ / ___ ____                     (disposable servers)   - So that I can get the kick of a performer
              ,_V_/site\___\___. ...which       ,------------------.   - So that the rewards become compounding
    O         |                ||    SENDS      |   ...to the      |   - Attracting a nice growing community
   /|\---1.-----> bookmarklet ----------2.-------> Pipulate Server |   - To chat with a bit as I get old
   ( ) CLICK  | with a website ||      URL and  |   | which checks |   - Because, we make our own why.
  =====       |   displaying.  ||       context '---|---|--|--|----'
    |         |                ||                   |   |  |  |              # THE PIPULATE TO-DO LIST HIT PARADE:
    5.        '----------------'|      then sends   |   |  |  '-------> ?    - Auto Setup Departmential Processes
  SEE THE--->  | to Google Sheet|<-------4.---------'   |  '----3.----> ?    - Cytoscape visualization of crawl data
  RESULTS      '----------------'  a response           '-------------> ?    - Video-per-feature links from Docs tab
                                                          ...stuff on net    - Email support

 If you like what you see expressed here in this project, there is countless more where that came from. Though I hate the
 notion of yet another platform or framework or architecture, that is indeed exactly what I've built here, but lightweight
 and pragmatic and in a "ready-position" for change. I love the never-ending fight against obsolessence, marginalzing and
 disnintermediation. A good fight with naysayers also intensifies the heat in which this product is forged, and makes it
 better overall. Follow my antics, from a Catskills Geek-Dad to seasoned SEO-pro in highly competitive NYC. Join me here.
 {'more' : ['https://twitter.com/miklevin', 'https://www.linkedin.com/in/miklevin', 'https://instagram.com/miklevin/']}

"""
#  _                            _     _   _     _       While it may look it, this is not the entry-point for Pipulate.
# (_)_ __ ___  _ __   ___  _ __| |_  | |_| |__ (_)___   Both webpipulate.py (the Flask context) and loopipulate.py (the
# | | '_ ` _ \| '_ \ / _ \| '__| __| | __| '_ \| / __|  command-line context for cron) import this file as one of their
# | | | | | | | |_) | (_) | |  | |_  | |_| | | | \__ \  first steps. It does it with "from pipulate import *" so that
# |_|_| |_| |_| .__/ \___/|_|   \__|  \__|_| |_|_|___/  everything here is running in top-level scope. The next few lines
#             |_|                                       are most of the early-load ubiquitous libraries used throughout.

import sys, os, socket, urlparse, re, gspread
import requests, traceback, datetime, time, json
import globs                                                                # An Ode To Style
from common import *
from flask import (Flask,                                                   # This is not DRY.
                  stream_with_context,                                      # I'll tell you why
                  render_template,
                  Response,                                                 # Though you may fret,
                  request,                                                  # I like it WET.
                  session,
                  redirect,                                                 # But like a champ,
                  url_for,                                                  # I make it DAMP!
                  flash)
from functions import *

#                          _          __  __    This ain't PHP. It's kinda like a .NET codebehind, but way more awesome
#   __ _ _ __  _ __    ___| |_ _   _ / _|/ _|   because it's Python. But Python resisting doing things like plugging whole
#  / _` | '_ \| '_ \  / __| __| | | | |_| |_    high-level web frameworks in the core product relies on 3rd party developers
# | (_| | |_) | |_) | \__ \ |_| |_| |  _|  _|   to fill the void--and in this case, it happens to be Flask. And Flask
#  \__,_| .__/| .__/  |___/\__|\__,_|_| |_|     happens to be Werkzeug to handle "web routing" and Jinja2 to handle
#       |_|   |_|                               PHP-style web templates. It takes time to grok, but is worth it.
#
socket.setdefaulttimeout(10.0)
app = Flask(__name__) #                         <-- This is a rather big moment in this application's lifecycle.

def stream_template(template_name, **context):  # There's a rather awesome bit of Python magic going on here. This is
  """Open inexpensive Flask-based streaming.""" # essentially a replacement for render_template() but which repeatedly
  app.update_template_context(context)          # "flushes" streaming output to the user. Part of the context expected
  t = app.jinja_env.get_template(template_name) # is data=somegeneratorinstance. Something inside a Flask object are
  rv = t.stream(context)                        # instructions what to do if it gets a generator object on a parameter
  return rv                                     # named data. And THIS is how the entire app is kept so lightweight.

@app.context_processor
def templateglobals():
  """Make functions usable in templates."""
  return dict(loginlink=getLoginlink(),
  bookmarklet=getBookmarklet(),
  blabel=getLabel(),
  logoutlink=getLogoutlink(),
  cyclemotto=cyclemotto()
  )

from managelists import *

@app.route("/v")
def visualize():
  if session and 'oa2' in session:
    out("Session")
    creds = Credentials(access_token=session['oa2'])
    gsp = gspread.authorize(creds)
    gdoc = gsp.open_by_key(request.args['k'])
    try:
      sheet = gdoc.worksheet("Visualizations")
      out("We're in business!")
    except:
      out("Visualizatons not found")
  return render_template('visualize.html')

#  _   _                                              Flask uses a routing system from another package called Werkzeug.
# | | | | ___  _ __ ___   ___ _ __   __ _  __ _  ___  Werkzeug uses decorators to "route" requests. You can read the main
# | |_| |/ _ \| '_ ` _ \ / _ \ '_ \ / _` |/ _` |/ _ \ function as: Feed the entire main() function as a parameter to the
# |  _  | (_) | | | | | |  __/ |_) | (_| | (_| |  __/ route method of the Flask app object, keeping all of Flask's "outer"
# |_| |_|\___/|_| |_| |_|\___| .__/ \__,_|\__, |\___| conext, which happens to be everying you need for a standard Python
#                            |_|          |___/       WSGI webserver. There's no Apache, nginx or even gunicorn here.
@app.route("/", methods=['GET', 'POST'])
def main():
  """Ensures config and login requirements met."""
  print('''
               ____  _             _       _   _
              |  _ \(_)_ __  _   _| | __ _| |_(_)_ __   __ _
              | |_) | | '_ \| | | | |/ _` | __| | '_ \ / _` |
              |  __/| | |_) | |_| | | (_| | |_| | | | | (_| |  _   _   _
              |_|   |_| .__/ \__,_|_|\__,_|\__|_|_| |_|\__, | (_) (_) (_)
                      |_|                              |___/
  ''')
  out("ENTERED MAIN FUNCTION", "0")
  stop = False
  streamit = False
  readytopip = False
  form = PipForm(csrf_enabled=False)
  formDict = formSwitch()
  form2 = None
  if ':' in form.options.data:
    form2 = formDict[form.options.data.split(':')[1]]
  else:
    form2 = PipForm2(csrf_enabled=False)
  if (request.method == 'POST' 
      and 'secondary' in form2 
      and form2.secondary.data == 'on'):
    form2 = formDict[form.options.data.split(':')[1]]
  menudefault = None
  selectedtext = None
  configform = ConfigForm(csrf_enabled=False)
  if (os.path.isfile(globs.FILE) and
      os.path.getsize(globs.FILE) > 0):
    app.config.from_pyfile(globs.FILE, silent=False)
    app.config['SESSION_TYPE'] = 'filesystem'
  else:
    #                                                   ____        # This traps the first time Pipulate is run on a new
    #   ___  ___ _ ____   _____ _ __    ___ ___  _ __  / _(_) __ _  # server and prompts you to enter your Google Developer
    #  / __|/ _ \ '__\ \ / / _ \ '__|  / __/ _ \| '_ \| |_| |/ _` | # Web app OAuth2 Client ID and Secret that you get from
    #  \__ \  __/ |   \ V /  __/ |    | (_| (_) | | | |  _| | (_| | # https://console.developers.google.com/project so that
    #  |___/\___|_|    \_/ \___|_|     \___\___/|_| |_|_| |_|\__, | # You never need to keep your username and password on
    #                                                        |___/  # the hard drive. In fact now, you can't anymore.
    if request.method == 'POST':
      import pickle
      pickleme = {
        'CLIENT_ID': configform.clientid.data,
        'CLIENT_SECRET': configform.clientsecret.data,
        'APP_SECRET': configform.appsecret.data
      }
      pickle.dump(pickleme, open(globs.TOKEN, 'wb'))
      redir = globs.DOMURL
      if 'Host' in request.headers:
        redir = 'http://'+request.headers['Host']
      scope = 'https://spreadsheets.google.com/feeds/'
      if globs.PCOM:
        scope = 'profile email ' + scope
      qsdict = {  'scope': scope,
                  'response_type': 'code',
                  'access_type': 'offline',
                  'redirect_uri': redir,
                  'approval_prompt': 'force',
                  'client_id': configform.clientid.data
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
    #                    _            _   _       _
    #   ___ _ __ ___  __| | ___ _ __ | |_(_) __ _| |___
    #  / __| '__/ _ \/ _` |/ _ \ '_ \| __| |/ _` | / __|
    # | (__| | |  __/ (_| |  __/ | | | |_| | (_| | \__ \
    #  \___|_|  \___|\__,_|\___|_| |_|\__|_|\__,_|_|___/
    #
    session.permanent = True
    creds = Credentials(access_token=session['oa2'])
    try:
      gsp = gspread.authorize(creds)
      gsp.openall()
      session['loggedin'] = "1"
    except:
      session.pop('loggedin', None)
    #      _                  _             _   Yes, Pipulate needs to know what spreadsheet to target,
    #  ___| |_ ___  _ __  ___(_) __ _ _ __ | |  and making a new one every time is a terrible mess.
    # / __| __/ _ \| '_ \/ __| |/ _` | '_ \| |  Been there, done that. And so, it ALWAYS targets a sheet
    # \__ \ || (_) | |_) \__ \ | (_| | | | |_|  named Pipulate unless you click the bookmarklet FROM a
    # |___/\__\___/| .__/|___/_|\__, |_| |_(_)  Google Sheet. Then, it targets that. In any case, this
    #              |_|          |___/           version is great at recycling and reducing file cruft.
    if session and 'loggedin' in session and session['loggedin'] == "1":
      needsPipulate = True
      tasteMe = None
      if request.args and 'u' in request.args and globs.SHEETS in request.args.get('u'):
        needsPipulate = False
        tasteMe = request.args.get('u')
      elif request.method == 'POST':
        needsPipulate = False
      try:
        if tasteMe:
          gdoc = gsp.open_by_url(tasteMe)
        else:
          gdoc = gsp.open(globs.NAME)
        needsPipulate = False
        globs.DOCID = gdoc.id
        globs.NAME = gdoc.title
        globs.TAB = gdoc.sheet1.title
        if gdoc.sheet1.find('?'):
          readytopip = True
          menudefault = "qmarks"
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
  globs.DOCLINK = '<a href="%s/d/%s/edit#gid=0" target="_blank">%s</a>' % (globs.SHEETS, globs.DOCID, globs.NAME)
  menutwo = False
  if request.method == 'POST':
    #  ____   ___  ____ _____   ____  _                              _   Shazam! is the block in which we create the
    # |  _ \ / _ \/ ___|_   _| / ___|| |__   __ _ ______ _ _ __ ___ | |  first instance of the Pipulate() generator
    # | |_) | | | \___ \ | |   \___ \| '_ \ / _` |_  / _` | '_ ` _ \| |  object that gets called again later as the
    # |  __/| |_| |___) || |    ___) | | | | (_| |/ / (_| | | | | | |_|  data paramater of a stream_template() call
    # |_|    \___/|____/ |_|   |____/|_| |_|\__,_/___\__,_|_| |_| |_(_)  enabling our magic streaming output. Shazam!
    #
    if form2 and form2.secondary.data == 'on':
      menutwo = True
      psKey = globs.MODE
      if 'radios' in form2:
        psKey = form2.radios.data
      elif 'checks' in form2:
        checklist = form2.checks.data
        psKey = checklist[0]
        for item in checklist:
          if ':' in item:
            psKey = item.split(':')[0]
            break
      if ':' in psKey:
        psKey = globs.MODE.split(':')[1]
      if psKey == 'cancel':
        return redirect(url_for('main', u=form2.pipurl.data))
      if psKey == 'add':
        checks = None
        try:
          checks = form2.checks.data
        except:
          pass
        if checks:
          streamit = stream_with_context(pipSwitch()[psKey](checks))
        else:
          streamit = stream_with_context(pipSwitch()[psKey]())
      else:
        streamit = stream_with_context(pipSwitch()[psKey]())
    elif form.pipurl.data:
      globs.PIPURL = form.pipurl.data
      if form.options.data:
        globs.MODE = form.options.data
        if ':' in globs.MODE:
          mode = globs.MODE.split(':')[1]
          return render_template('pipulate.html', form=form, form2=form2, mode=mode)
      if form.magicbox.data:
        globs.KEYWORDS = form.magicbox.data
        form.magicbox.data = None
      streamit = stream_with_context(Pipulate())
    else:
      flash('Please enter a URL to Pipulate.')
  else:
    #  ___                                _        _              You're here because method doesn't equal POST.
    # |__ \__ _ _   _  ___ _ __ _   _ ___| |_ _ __(_)_ __   __ _  It's a very important place to be, because
    #   / / _` | | | |/ _ \ '__| | | / __| __| '__| | '_ \ / _` | data passed on the URL is a super-reliable way
    #  |_| (_| | |_| |  __/ |  | |_| \__ \ |_| |  | | | | | (_| | to pass data between systems, sessions, or
    #  (_)\__, |\__,_|\___|_|   \__, |___/\__|_|  |_|_| |_|\__, | what have you. That's why you'll see logout
    #        |_|                |___/                      |___/  handling and client-to-server data handoffs.
    if request.args and 's' in request.args:
      form.magicbox.data = request.args.get('s')
      selectedtext = request.args.get('s')
    elif session and 's' in session:
      form.magicbox.data = session['s']
      selectedtext = session['s']
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
        return redirect(url_for('main', l='1'))
    elif request.args and 'logout' in request.args: # Logging out
      if session:
        if 'oa2' in session:
          revokeurl = 'https://accounts.google.com/o/oauth2/revoke?token=' + session['oa2']
          requests.get(revokeurl, timeout=5)
        if 'u' in request.args:
          form.pipurl.data = request.args.get('u')
          globs.PIPURL = request.args.get('u')
        session.pop('loggedin', None)
    elif request.args: # Move selected text and current url into session object.
      try:
        if 's' in request.args:
          session['s'] = request.args.get('s')
        if 'u' in request.args:
          form.pipurl.data = request.args.get('u')
          globs.PIPURL = request.args.get('u')
          session['u'] = request.args.get('u')
        if session and 'u' in session:
          form.pipurl.data = session['u']
          globs.PIPURL = session['u']
      except:
        pass
  #    ____ _____ _____                                                   What better place to "GET" messages than
  #   / ___| ____|_   _|  _ __ ___   ___  ___ ___  __ _  __ _  ___  ___   where the GET method is being used to build
  #  | |  _|  _|   | |   | '_ ` _ \ / _ \/ __/ __|/ _` |/ _` |/ _ \/ __|  the normally much more stream-y UI. But it's
  #  | |_| | |___  | |   | | | | | |  __/\__ \__ \ (_| | (_| |  __/\__ \  not needed, and Flask provides yet another
  #   \____|_____| |_|   |_| |_| |_|\___||___/___/\__,_|\__, |\___||___/  thing for the world flash to mean. Nice little
  #                                                     |___/             higher abstraction doohickey in Flask framework.
  options = menumaker()
  if request.method == 'GET':
    try:
      if menutwo:
        pass
      elif selectedtext and globs.SHEETS not in globs.PIPURL:
        menudefault = "keywords"
        session.pop('_flashes', None)
        flash("Congratulations! You have chosen to harvest keywords.")
        flash("The words filled into the above textarea will be inserted into %s." % globs.NAME)
        flash("Insert commas between keywords, and each one will get its own row.")
        flash("You can also add more keyword variations by just typing them in.")
        flash('Then select "Harvest Keywords" from the dropdown menu.')
        flash('You can then find your keywords under the Harvest tab.')
      else:
        session.pop('_flashes', None)
        flash('Pipulate will process the "%s" tab in the "%s" Google Spreadsheet.' % (globs.TAB, globs.DOCLINK))
        flash("You can target any sheet simply by clicking the bookmarklet on that Google Spreadsheet.")
        if readytopip:
          flash('The question marks in %s indicate that you are ready to Pipulate.')
          flash("So, what are you waiting for? Hit that button!")
        elif globs.sheet.row_values(1)==[] and globs.sheet.row_values(2) == []:
          flash("Because the first two rows of %s are blank, you can do one of the following:" % globs.TAB)
          flash("Visit %s and set up %s with input values, a function and question mark," % (globs.DOCLINK, globs.TAB))
          flash('Select "Crawl Website" from the menu,')
          flash('Select an "Auto Setup" from menu,')
          flash('Harvest keywords,')
          flash('Watch a demo.')
        else:
          flash("It appears %s has no queston marks." % globs.TAB)
          flash('Maybe select "Add Columns" from the menu to add some KPIs.')
    except:
      pass
  out("Selecting template method.")
  #  _                       _       _              To Stream or to Render, that is the question. 'Tis it not nobler
  # | |_ ___ _ __ ___  _ __ | | __ _| |_ ___  ___   to embrace the streamy render_temblate alternative in Flask and
  # | __/ _ \ '_ ` _ \| '_ \| |/ _` | __/ _ \/ __|  do all the ajaxy-communication tight on the same response that
  # | ||  __/ | | | | | |_) | | (_| | ||  __/\__ \  built the form in the first place? How little overhead. How few
  #  \__\___|_| |_| |_| .__/|_|\__,_|\__\___||___/  parts. How adaptable to unimaginably diverse situations in the
  #                   |_|                           future! Flask-SocketIO is not ruled it. It is just not necessary.
  if streamit:
    #Handle streaming user interface updates resulting from a POST method call.
    return Response(stream_template('pipulate.html', form=form, select=options, data=streamit)) # <-- Look Closely!!!
  else:
    #Handle non-streaming user interface build resulting from a GET method call.
    out("EXITING MAIN FUNCTION RENDER", "0", '-')
    return render_template('pipulate.html', form=form, select=options, menudefault=menudefault)
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
#  __  __                   _ _ _   _     _         ____                           _              I am a monolith until I
# |  \/  | ___  _ __   ___ | (_) |_| |__ (_) ___   / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __  fuse my defensive api
# | |\/| |/ _ \| '_ \ / _ \| | | __| '_ \| |/ __| | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__| coding trick with my
# | |  | | (_) | | | | (_) | | | |_| | | | | (__  | |_| |  __/ | | |  __/ | | (_| | || (_) | |    streaming user output
# |_|  |_|\___/|_| |_|\___/|_|_|\__|_| |_|_|\___|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|    trick. You may not get
#                                                                                                 it, but you will yield.
def Pipulate(preproc='', dockey='', targettab="", token=''):
  """Generator that streams output to a web user interface."""
  stop = False
  qset = set()
  qstart = 1
  qend = 1
  badtuple = (globs.GBAD, globs.GBAD, "", "")
  lock = ("", "", "", "+")
  unlock = ("", "", "", "-")
  spinerr = "spinerr", "", "", ""
  spinoff = "spinoff", "", "", ""
  out("PIPULATION BEGINNING", "1")
  #                                            _     _         _                Try to keep your try blocks small to isolate where the
  #   ___  _ __   ___  __   _____ _ __ _   _  | |__ (_) __ _  | |_ _ __ _   _   errors are coming from. Or do this. Python is a very
  #  / _ \| '_ \ / _ \ \ \ / / _ \ '__| | | | | '_ \| |/ _` | | __| '__| | | |  pragmatic language, and sometimes you have to take
  # | (_) | | | |  __/  \ V /  __/ |  | |_| | | |_) | | (_| | | |_| |  | |_| |  advantage of how try/exept can work in a big generotor
  #  \___/|_| |_|\___|   \_/ \___|_|   \__, | |_.__/|_|\__, |  \__|_|   \__, |  yielding instructions to a Web browser UI, which must
  #                                    |___/           |___/            |___/   be told in its final dying breath to stop spinning.
  try:
    if globs.WEB:
      yield "Beginning to Pipulate! Opening sheet...", "", "", ""
      yield "spinon", "", "", ""
    out("Reading in functions.")
    funcs = [x for x in globals().keys() if x[:2] != '__'] #List all functions
    transfuncs = ziplckey(funcs, funcs) #Keep translation table
    blankrows = 0
    gsp = None
    gdoc = None
    stop = True
    if session or (dockey and token):
      out("LOGIN ATTEMPT", "2")
      sheet = ''
      cell = None
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
            yield spinoff
        try:
          gsp = gspread.authorize(creds)
        except:
          out("Login failed.")
          if globs.WEB:
            yield "Google Login unsuccessful.", "", "", ""
            yield spinoff
          Stop()
        else:
          out("Login successful.")
        out("Opening Spreadsheet...")
        stop = True
        for x in range(10):
          if globs.WEB: yield lock
          try:
            gdoc = gsp.open_by_url(globs.PIPURL)
            globs.DOCID = gdoc.id
            globs.NAME = gdoc.title
            if targettab:
              globs.TAB = gdoc.worksheet(targettab).title
            else:
              globs.TAB = gdoc.sheet1.title
            globs.sheet = gdoc.worksheet(globs.TAB)
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
              gdoc = gsp.open(globs.NAME)
              globs.DOCID = gdoc.id
              if targettab:
                globs.sheet = gdoc.worksheet(targettab)
                globs.TAB = gdoc.worksheet(targettab).title
              else:
                globs.sheet = gdoc.sheet1
                globs.TAB = gdoc.sheet1.title
              stop = False
              break
            except gspread.httpsession.HTTPError, e:
              out("No token found, session expired. Switch to HTML5 localStorage.")
              if globs.WEB:
                yield "I am sorry, the sesson has expired. Please log back in.", "Log back in", "", ""
                yield spinerr
                break
            except:
              if globs.WEB:
                yield "I see you're on a URL that is not a Google Spreadsheet. Would you like to grab links?", "", "", ""
                yield "If so, just <a href='https://docs.google.com/spreadsheets/create' target='_blank'>create</a> a new Spreadsheet, name it \"Pipulate\" and click Pipulate again.", "Google Spreadsheet Not Found.", "", ""
                yield 'New to this odd but awesome approach? Watch the <a target="_blank" href="http://goo.gl/v71kw8">Demo</a> and read the <a target="_blank" href="http://goo.gl/p2zQa4">Docs</a>.', "", "", ""
                break
          except gspread.exceptions.SpreadsheetNotFound:
            if globs.WEB: yield "Please give the document a name to force first save.", "", "", ""
          except Exception as e:
            if globs.WEB: yield dontgetfrustrated(x)
            out("Retry login %s of %s" % (x, 10))
            time.sleep(6)
        if stop:
          if globs.WEB:
            yield badtuple
            yield spinerr
            yield unlock
          Stop() # Consider adding refresh_token logic for users (versus the scheduler)
        globs.DOCLINK = '<a href="%s/d/%s/edit#gid=0" target="_blank">%s</a>' % (globs.SHEETS, globs.DOCID, globs.NAME)
      out("END LOGIN ATTEMPT", "2", '-')

      if globs.WEB: yield unlock
      out("%s successfully opened." % globs.NAME)
      yme = "%s spreadsheet opened!" % globs.DOCLINK
      yield yme, "Spreadsheet Opened", "", ""

      if (globs.MODE == 'keywords'
        and globs.KEYWORDS
        and globs.KEYWORDS[:1] != '['
        and globs.KEYWORDS[-1:] != ']'
        and globs.KEYWORDS[:1] != '{'
        and globs.KEYWORDS[-1:] != '}'
        ):
        # Keywords Tab
        if globs.WEB: yield "Keyword Harvesting Detected", "Making Harvest Tab if needed", "", ""
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
        yme = "Harvesting %s keywords." % len(kwlist)
        if globs.WEB: yield yme, "Harvesting keywords", "", ""
        for kw in kwlist:
          kwrows.append([kw.strip(), globs.PIPURL])
        try:
          InsertRows(ksheet, kwrows, kcount)
        except:
          pass
        if globs.WEB:
          yme = "Keywords Harvested! %s" % globs.PBNJMAN
          yield yme, "Mmmmmm, more keywords.", json.dumps(kwlist), ""
          yield spinoff
        return #permissible here?
      #        _             _       _         ___ ____  __  __   The Pipulate Instruction Processor Machine (IPM)
      #  _ __ (_)_ __  _   _| | __ _| |_ ___  |_ _|  _ \|  \/  |  takes a list of tuples and interprets each
      # | '_ \| | '_ \| | | | |/ _` | __/ _ \  | || |_) | |\/| |  and interprets it as an action to take and
      # | |_) | | |_) | |_| | | (_| | ||  __/  | ||  __/| |  | |  a target aginst which to, and becomes a sort
      # | .__/|_| .__/ \__,_|_|\__,_|\__\___| |___|_|   |_|  |_|  of sequentially carried out jobs, such as
      # |_|     |_|                                               make table, fill in defaults, and pipulate.
      if preproc:
        for instruction in preproc:
          inst = instruction[0]
          if inst == 'clear':
            out('Clearing Sheet 1')
            if globs.WEB: yield "Clearing Sheet 1...", "Clearing Sheet 1", "", ""
            try:
              anything = re.compile('.+')
              CellList = gdoc.sheet1.findall(anything)
              for cell in CellList:
                cell.value = ''
              result = gdoc.sheet1.update_cells(CellList)
              if globs.WEB:
                yield "You now are ready to do something requiring Sheet1 empty, like a Crawl or a Setup.", "", "", ""
                yme = 'I recommend opening the %s Sheet in another tab so you can see the magic happen.' % (globs.DOCLINK)
                yield yme, "", "", ""
                yme = "Sheet1 Cleared! %s" % globs.PBNJMAN
                yield yme, "Now, go do something awesome!", "", ""
                yield spinoff
            except:
              yield "Failed to clear Sheet 1", "", "", ""
              yield spinerr
              Stop()
          elif inst == 'stop':
            Stop()
          elif inst == 'table':
            aobj = instruction[1]
            row1 = aobj[0]
            lol = aobj[1:]
            InitTab(gdoc, "sheet1", row1, lol)
          elif inst == 'sheet':
            tabname = instruction[1]
            aobj = instruction[2]
            row1 = aobj[0]
            lol = aobj[1:]
            InitTab(gdoc, tabname, row1, lol)
          elif inst == '?':
            if instruction[1]:
              for yieldme in Pipulate(targettab=instruction[1]):
                yield yieldme
            else:
              for yieldme in Pipulate():
                yield yieldme
          elif inst == 'fillmarks': #Fill in question marks
            if globs.WEB:
              yield "Looking for where question marks should go...", "Looking for functions and scraper names", "", ""
            if not globs.row1:
              globs.row1 = lowercaselist(gdoc.worksheet(globs.TAB).row_values(1))
            if not globs.numrows:
              globs.numrows = len(globs.sheet.col_values(1))
            gfuncs = [x for x in globals().keys() if x[:2] != '__']
            scrapers = [x[0] for x in scrapes()]
            unified = set(gfuncs + scrapers)
            colrange = None
            for acol in globs.row1:
              if acol in unified:
                yme = "?'s for %s" % acol
                if globs.WEB: yield yme, "", "", ""
                qcol = globs.letter[globs.row1.index(acol) + 1]
                nr = globs.numrows
                colrange = '%s%s:%s%s' % (qcol, 2, qcol, nr)
                CellList = globs.sheet.range(colrange)
                for cell in CellList:
                  cell.value = '?'
                result = globs.sheet.update_cells(CellList)
            yield "Question marks filled in!", "Ready for some serious pipulating", "", ""
            yme = "You're now ready for some serious pipulating!" + globs.PBNJMAN
            yield yme, "", "", ""
            yield spinoff
            Stop()
          elif inst == 'add':
            if not globs.row1:
              globs.row1 = lowercaselist(gdoc.worksheet(globs.TAB).row_values(1))
            colname = instruction[1]
            if colname not in globs.row1:
              clet = globs.letter[len(gdoc.worksheet(globs.TAB).row_values(1)) + 1]
              acell = "%s1" % clet
              globs.sheet.update_acell(acell, instruction[1])
              out(instruction)
      #                        _       _               _  ___   At some point in the future, there wil be
      #   __ _  ___   ___   __| |  ___| |__   ___  ___| ||__ \  something better than Google Spreadsheets.
      #  / _` |/ _ \ / _ \ / _` | / __| '_ \ / _ \/ _ \ __|/ /  Until that day, let us use it excessively
      # | (_| | (_) | (_) | (_| | \__ \ | | |  __/  __/ |_|_|   for precisely the things it's good at. But
      #  \__, |\___/ \___/ \__,_| |___/_| |_|\___|\___|\__(_)   it must be there, you must have access, any
      #  |___/                                                  servers in the picture must have access too.
      if globs.WEB: yield "Checking Tabs...", "Then we check for tabs...", "", ""

      # Documentation Tab
      if 'docs' in globs.SHEETS:
        if len(documentation()) > gdoc.worksheet("Docs").row_count:
          if globs.WEB:
            yield "Re-creating the Docs tab (new functions added).", "New Function Added", "", ""
          out("Re-creating Docs Tab")
          try:
            gdoc.del_worksheet(gdoc.worksheet("Docs"))
          except:
            pass
        #gotcha((gdoc.worksheet("Docs").row_count, len(documentation())))
      headers = ['Function', 'Category', 'Requirements', 'Description', 'More']
      InitTab(gdoc, 'Docs', headers, documentation()) #!!!

      # Config Tab
      headers = ['NAME', 'VALUE']
      config = []
      config.append(['RepeatJobEvery','day'])
      config.append(['MaxRowsPerHour','3'])
      config.append(['SEMRush','Paste SEMRush API key here.'])
      config.append(['MozID','Paste Moz ID here.'])
      config.append(['MozKey','Paste Moz Secret Key here.'])
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
        if globs.WEB:
          yield badtuple
          yield spinerr
          yield unlock
        Stop()
      tabs = None
      try:
        tabs = [sheet.title for sheet in gdoc.worksheets()]
      except:
        pass
      if tabs:
        out("Tabs Read!")
        if globs.WEB:
          yield "Tabs successfully found/created!", "Tabs Created", tabs, ""
      stop = True
      for x in range(5):
        if globs.WEB: yield lock
        try:
          out("Reading Config tab into globals.")
          globs.config = RefreshConfig(gdoc, "Config") #HTTPError
          stop = False
          break
        except:
          if globs.WEB: yield dontgetfrustrated(x)
          out("Retry Reading Config tab into globals %s of %s" % (x, 10))
          time.sleep(5)
      if stop:
        if globs.WEB:
          yield badtuple
          yield spinerr
          yield unlock
        Stop()
      out("Config tab copied to globals.")
      if globs.WEB:
        yme = "Counting rows in %s tab..." % globs.TAB
        yield yme, "Counting rows", '', ''
      out("Counting rows in Pipulate tab.")
      stop = True
      for x in range(5):
        if globs.WEB: yield lock
        try:
          if targettab:
            globs.sheet = gdoc.worksheet(targettab)
          else:
            globs.sheet = gdoc.sheet1
          stop = False
          break
        except:
          if globs.WEB: yield dontgetfrustrated(x)
          out("Retry get Pipulate sheet %s of %s" % (x, 10))
          time.sleep(5)
      if stop:
        if globs.WEB:
          yield badtuple
          yield spinerr
          yield unlock
        Stop()
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
        if globs.WEB:
          yield badtuple
          yield spinerr
          yield unlock
        Stop()
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
        if globs.WEB:
          yield badtuple
          yield spinerr
          yield unlock
        Stop()
      yme = "%s rows with question marks found in %s." % (globs.numrows, globs.TAB)
      out(yme)
      if globs.WEB: yield yme, "", "", ""
      if globs.numrows == 0 and globs.MODE == 'qmarks':
        if globs.WEB:
          yme = "Double-check that the %s sheet in %s is set up correctly." % (globs.TAB, globs.DOCLINK)
          yield yme, "Pipulate needs question marks to replace.", "", ""
          yield spinerr
        return #permissible here?

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
        if globs.WEB:
          yield badtuple
          yield spinerr
          yield unlock
        Stop()
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
        if globs.WEB:
          yield badtuple
          yield spinerr
          yield unlock
        Stop()
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
          #  _____       _ _   _____            _     _  _   _  Evil Eval #1
          # | ____|_   _(_) | | ____|_   ____ _| |  _| || |_/ |
          # |  _| \ \ / / | | |  _| \ \ / / _` | | |_  ..  _| | Turns string-name of a function into an actual
          # | |___ \ V /| | | | |___ \ V / (_| | | |_      _| | instance of that function. Can only do this if
          # |_____| \_/ |_|_| |_____| \_/ \__,_|_|   |_||_| |_| it was already found to exist in globals.
          #
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
          if globs.WEB:
            yield badtuple
            yield spinerr
            yield unlock
          Stop()
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
      yme = "%s trending jobs found. Analyzing frequency." % len(trendlistoflists)
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
          Stop()
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
        if globs.WEB: yield "Pipulate running in ?-replacement mode.", "", "", ""
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
          if targettab:
            globs.sheet = gdoc.worksheet(targettab)
          else:
            globs.sheet = gdoc.sheet1
        except:
          if globs.WEB:
            yield "Couldn't reach Google Docs. Try logging in again.", "", "", ""
            yield spinoff
          Stop()
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
      out("QUESTION MARK Replacement.", '2')
      if not qset and not trended:
        # Yield values that will un-nest console output
        if globs.WEB:
          yme = "No ?'s found in %s Sheet." % globs.DOCLINK
          yield yme, "", "", ""
          yme = 'New to this? Watch <a target="_blank" href="https://docs.google.com/presentation/d/10lr_d1uyLMOnWsMzbenKiPlFE5-BIt9bxVucw7O4GSI/edit?usp=sharing">Demo</a> &amp; read <a target="_blank" href="https://github.com/miklevin/pipulate/blob/master/README.md">Docs</a>. '
          yield yme, "The first worksheet in your spreadsheet needs something in it.", "", ""
          yme = "But congratulations; you found Pipulate. " + globs.PBNJMAN
          yield yme, "", "", ""
          yield "heart", "", "", ""
        return # permissible here?
      therange = range(qstart, qend)
      blankrows = 0 #Lets us skip occasional blank rows
      if globs.WEB:
        yield "Beginning to process rows with question marks...", "", "", ""
      for index, rowdex in enumerate(therange): #Start stepping through every row.
        if rowdex in qset:
          if maxrowsperhour: # if maxrowsperhour is 0, this won't trap
            if index >= int(maxrowsperhour):
              break
          yme = "Pipulating row: %s (item %s of %s)..." % (rowdex-1, index+1, len(therange))
          yield yme, yme, "", ""
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
            if globs.WEB:
              yield "GData Timed Out","Sorry, GDATA Failed. Try again.", "", ""
              yield spinerr
              yield unlock
            Stop()

          onerow = []
          for cell in CellList:
            onerow.append(cell.value)
          if '?' in onerow:
            #   _ __ _____      __  Inside the Monolithic Generator, there resides a very special location where you are
            #  | '__/ _ \ \ /\ / /  about to step through rows and actually replace any that contain a question mark.
            #  | | | (_) \ V  V /   What's so special about this place? Well, user feedback, of course! Anything you want
            #  |_|  \___/ \_/\_/    to show to the user once-per-row must yield it's output from the generator here.
            #
            out("PROCESSING ROW %s." % rowdex, '3')
            blankrows = 0
            if globs.WEB:
              yield "", "", json.dumps(onerow), ""
            rowdexstring = str(rowdex)
            newrow = onerow[:]
            if rowdexstring > 1:
              #All subsequent rows are checked for question mark replacement requests.
              for coldex, acell in enumerate(newrow):
                if questionmark(onerow, rowdexstring, coldex):
                  if 'url' in globs.row1: #Only fetch html once per row if possible
                    if globs.WEB: yield lock
                    try:
                      if 'archive' in globs.row1:
                        prehtml = onerow[globs.row1.index('archive')]
                        globs.html = unarchive(prehtml)
                      else:
                        globs.html = gethtml(onerow[globs.row1.index('url')])
                    except:
                      pass
                    if globs.WEB: yield unlock
                  collabel = globs.row1[coldex]
                  if collabel in transfuncs.keys():
                    stop = True
                    for x in range(3):
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
                        #  _____       _ _   _____            _     _  _  ____    Evil Eval #2
                        # | ____|_   _(_) | | ____|_   ____ _| |  _| || ||___ \
                        # |  _| \ \ / / | | |  _| \ \ / / _` | | |_  ..  _|__) |  Turns a function-call string signature
                        # | |___ \ V /| | | | |___ \ V / (_| | | |_      _/ __/   into an actual instance of that function
                        # |_____| \_/ |_|_| |_____| \_/ \__,_|_|   |_||_||_____|  called with those parameters. Grok it.
                        #
                        tastereturn = eval(evalme)
                        if type(tastereturn) == tuple:
                          for index2, anothercell in enumerate(CellList):
                            out("'%s': '%s'" % (globs.row1[index2], anothercell.value))
                          gotcha(tastereturn[1])
                        else:
                          newrow[coldex] = tastereturn
                        stop = False
                        out('%s worked' % collabel)
                        yme = "<li>%s</li>" % (collabel)
                        if globs.WEB:
                          yield yme, "", "", ""
                        break
                      except Exception as e:
                        print traceback.format_exc()
                        if globs.WEB:
                          yme = "We have a problem in %s." % collabel
                          yield yme, "", "", ""
                        time.sleep(10)
                    if stop == True:
                      out("Function End (Failed)", "4", '-')
                      if globs.WEB:
                        yme = "Something went wrong in the %s function. Stopping." % collabel
                        yield yme, "", "", ""
                        yield spinerr
                        yield unlock
                      Stop() #                                            <-- This is where you could keep things running
                    out("Function End", "4", '-')
                  elif collabel in transscrape.keys():
                    stop = True
                    for x in range(3):
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
                        if 'url' in globs.row1 or 'archive' in globs.row1:
                          if globs.WEB: yield lock
                          if 'archive' in globs.row1:
                            prehtml = onerow[globs.row1.index('archive')]
                            html = unarchive(prehtml)
                          else:
                            url = onerow[globs.row1.index('url')]
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
                              newrow[coldex] = globs.NONE
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
                        if globs.WEB: yield yme, "", "", ""
                        stop = False
                        break
                      except Exception as e:
                        print traceback.format_exc()
                        out("Scrape problem on row %s. Retrying." % rowdexstring)
                        time.sleep(2)
                        if globs.WEB: yield dontgetfrustrated(x)
                    if stop == True:
                      out("Scrape End (Failed)", "4", '-')
                      if globs.WEB:
                        yme = "Something went wrong in the %s scraper. Stopping." % collabel
                        yield yme, "", "", ""
                        yield spinerr
                        yield unlock
                      Stop() #                                            <-- This is where you could keep things running
                    out("Scrape End", "4", '-')
            out("DONE PROCESSING ROW %s." % rowdex, '3', '-')
            out("Finished processing row. Updating spreadsheet...")
            newrow = [globs.EMPTY if x==None else x for x in newrow]
            if len(str(newrow)) > globs.ROWMAX:
              yme = "['JSON data for %s too big to display here.']" % collabel
              if globs.WEB: yield "", "", yme, ""
            else:
              try:
                if globs.WEB: yield "", "", json.dumps(newrow), ""
              except:
                if globs.WEB: yield "", "", newrow, ""
            for index, onecell in enumerate(CellList):
              onecell.value = newrow[index]
            if globs.STOP:
              if globs.WEB:
                yme = "Pipulate deliberately stopped. Feels like a success. %s" % globs.PBNJMAN
                yield yme, "Pipulation Stopped", "", ""
                yield spinoff
              Stop()
            else:
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
                if globs.WEB:
                  yield badtuple
                  yield spinerr
                  yield unlock
                Stop()
          elif onerow.count('') == len(onerow):
            blankrows += 1
            if blankrows > 1:
              break
      out("Done question Mark Replacement.", '2', '-')
    else: #No session object found
      if globs.WEB: yield 'Please Login to Google', "", "", ""
    if globs.WEB:
      yme = 'Pipulation complete. Do a little victory dance. %s' % globs.PBNJMAN
      yield yme, 'Congratulations, pipulation complete!', "", ""
      yield spinoff
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
        if globs.MODE != 'clear':
          yield spinerr
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
  blab = globs.NAME
  droidcut = "ppp"
  if subdomain == 'localhost':
    blab = "%s %s 8888" % (droidcut, "Localhost")
  elif subdomain == 'pipulate':
    blab = '%s %s' % (droidcut, "Pipulate")
  elif subdomain:
    blab = "%s %s %s" % (droidcut, "Pipulate", subdomain)
  return blab

def getBookmarklet():
  """Return the HTML required to create a draggable Pipulate bookmarklet link."""
  host = request.headers['Host']
  bname = globs.NAME
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
    wholelist = list(headerlist) + list(initlist)
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

def convertisotime(timestamp):
  i = datetime.datetime(*map(int, re.split('[^\d]', timestamp)[:-1]))
  return i.strftime("%m/%d/%Y %H:%M:%S")

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

#                   _
#   _ __ ___   __ _(_)_ __    _ __ ___   ___ _ __  _   _
#  | '_ ` _ \ / _` | | '_ \  | '_ ` _ \ / _ \ '_ \| | | |
#  | | | | | | (_| | | | | | | | | | | |  __/ | | | |_| |
#  |_| |_| |_|\__,_|_|_| |_| |_| |_| |_|\___|_| |_|\__,_|
#
from flask_wtf import Form
from wtforms import (StringField,
                    RadioField,
                    HiddenField,
                    SelectMultipleField,
                    TextAreaField,
                    SelectField,
                    widgets)

def menumaker():
  ''' Creates the entire cadence of the system.'''
  menu = [
    ('qmarks'      , "Replace ?'s"),
    ('menu:setup'  , "Auto Templates"),
    ('menu:crawl'  , "Crawl a Website"),
    ('menu:column' , "Add Some Columns"),
    ('menu:graph'  , "See a Visualization"),
    ('keywords'    , "Harvest Keywords"),
    ('menu:clear'  , "Clear Sheet1")
  ]
  strmenu = '<option value="off">What do you want to do?</option>\n'
  for item in menu:
    strmenu += '<option value="%s">%s</options>\n' % (item[0], item[1])
  return strmenu

def formSwitch():
  """Create dict that ties screen 1 select options with what menu to show on interstitial page.
  Everything in the interstitial forms section needs an entry in this dict to activate."""
  return {
    'clear':        ClearSheet1Form(csrf_enabled=False),
    'crawl':        CrawlTypesForm(csrf_enabled=False),
    'setup':        SetupForm(csrf_enabled=False),
    'column':       AddColumnsForm(csrf_enabled=False),
    'graph':        VisualizationForm(csrf_enabled=False)
  }

def pipSwitch():
  return {
    'clear':        ClearSheet1,
    'cancel':       Cancel,
    'linksonpage':  LinksOnPage,
    'quickcrawl':   QuickCrawl,
    'linkgraph':    LinkGraph,
    'tests':        RunTests,
    'add':          AddColumns,
    'sitemap':      MakeSitemap,
    'fillmarks':    FillQMarks
  }

class PipForm(Form):
  """Define form for main Pipulate user interface."""
  pipurl = StringField('Paste a Google Sheet URL:')
  magicbox = TextAreaField("magicbox")
  options = SelectField("options")

class PipForm2(PipForm):
  """Adds a hidden field to tell the secondary menu from a dropdown menu selection."""
  secondary = HiddenField()

class ConfigForm(Form):
  """Define form for aquiring configuration values."""
  import binascii, os
  apdef = binascii.hexlify(os.urandom(24))
  appsecret = StringField('Flask app secret (auto-generated):', default=apdef)
  clientid = StringField('Client ID (from Google Dev Console):')
  clientsecret = StringField('Client secret (from Google Dev Console):')


#  _       _                _   _ _   _       _       This should set forth a familiar pattern where
# (_)_ __ | |_ ___ _ __ ___| |_(_) |_(_) __ _| |___   we open with a dict router and follow with the
# | | '_ \| __/ _ \ '__/ __| __| | __| |/ _` | / __|  things that router can invoke. In this case,
# | | | | | ||  __/ |  \__ \ |_| | |_| | (_| | \__ \  it's the mapping between the main Pipulate drop-
# |_|_| |_|\__\___|_|  |___/\__|_|\__|_|\__,_|_|___/  down menu and what form gets shown on the
#                                                     interstitial screen to follow, choices listed.

class AddColumnsForm(PipForm2):
  """Create the menu for when Clear Sheet 1 is selected."""
  choices = [
    ('add:url',       'URL'),
    ('add:keyword',   'Keyword'),
    ('add:url,title,description,h1,h2,canonical',       'Crawl stuff like Title, Metas, H1s, etc.'),
    ('add:httpcodes', 'Response Codes, Headers, Redirect Chain, etc.'),
    ('add:opengraph', 'Facebook Open Graph tags'),
    ('add:mobile',    'Mobile-friendly Check'),
    ('add:twitter',   'Twitter (multiple)'),
    ('add:facebook',  'Facebook (multiple)'),
    ('add:youtube',   'YouTube (multiple)'),
    ('add:instagram', 'Instagram'),
    ('cancel',    'Cancel')
  ]
  checks = SelectMultipleField(
    choices=choices,
    option_widget=widgets.CheckboxInput(),
    widget=widgets.ListWidget(prefix_label=False)
  )

class CrawlTypesForm(PipForm2):
  """Present user with different types of crawls they can perform."""
  radios = RadioField(choices=[
    ('linksonpage',   '1. LINKS ON PAGE: Just get the links from page, one line per link.'),
    ('quickcrawl',    '2. QUICK CRAWL: Same as above, but visits each page to get their on-page data.'),
    ('linkgraph',     '3. CRAWL, 2 DEEP: Acquires link-data for 3-Level Site Hierarchy Visualization. It requires you to do another "Replace ?\'s" afterwards.'),
    ('cancel',        'Cancel')
  ])

class SetupForm(PipForm2):
  """Create the menu for when Clear Sheet 1 is selected."""
  radios = RadioField(choices=[
    ('fillmarks', "Flood-fill ?'s (It will wipe out existing data)."),
    ('tests',   'Run Tests'),
    ('cancel',  'Cancel')
  ])

class VisualizationForm(PipForm2):
  """Offer up a few common visualizations of the type of data we're handling"""
  radios = RadioField(choices=[
    ('sitemap', 'Generate interactive hierarchal sitemap from a 2-DEEP crawl.'),
    ('cancel',  'Cancel')
  ])

class ClearSheet1Form(PipForm2):
  """Create the menu for when Clear Sheet 1 is selected."""
  radios = RadioField(choices=[
    ('clear',   'Yes, clear Sheet 1.'),
    ('cancel',  'Cancel')
  ])

#       _               _                         _         Here's a bunch of key/value pairs for ya. We open with a
#   ___| |__   ___  ___| |_   _ __ ___  _   _ ___(_) ___    very Pythonic switch that comprise the possible instructions
#  / __| '_ \ / _ \/ _ \ __| | '_ ` _ \| | | / __| |/ __|   for our Instruction Processor Machine... or "player piano"
#  \__ \ | | |  __/  __/ |_  | | | | | | |_| \__ \ | (__    such as it were. Or Loom, if you prefer. Or Turing machine.
#  |___/_| |_|\___|\___|\__| |_| |_| |_|\__,_|___/_|\___|   In any case, we just feed these instructions into the part
#                                                           of Pipulate there waiting to execute final menu choices.

def FillQMarks():
  '''Interrogates worksheet and inserts question marks wherever they can go'''
  return Pipulate([
    ('fillmarks', '')
  ])

def MakeSitemap():
  '''Offer user some visualizations to choose from.'''
  return Pipulate([
    ('sheet', 'visualizations', [
      ('viewname', 'makeview', 'sharelink', 'datestamp', 'guid', 'includecode', 'compresseddata'),
      ('sitemap', '?', '', '', '', '')
    ]),
    ('?', 'visualizations'),
    ('stop', '')
  ])

def ClearSheet1():
  '''Offer user some visualizations to choose from.'''
  return Pipulate([
    ('graph', '')
  ])

def AddColumns(checks):
  '''Ad columns to sheet from checkboxes on submitted form.'''
  out("Hey, I'm adding some columns!.")
  lot = []
  used = set()
  for acolumn in checks:
    if ',' in acolumn:
      subcols = [x.strip() for x in acolumn[4:].split(',')]
      for subcol in subcols:
        if subcol not in used:
          lot.append(('add', str(subcol)))
          used.add(subcol)
    else:
      if acolumn not in used:
        lot.append(('add', str(acolumn[4:])))
        used.add(acolumn[4:])
  # We return an instance of the Pipulate geneorator, fed the list-of-tuples. Nice! <-- leave this comment for awhile.
  # Pipulate is the player piano. It normally tries to replace question marks.
  # So when fed a list of tuples, it will interpret them as it's music instructions.
  lot.append(('fillmarks', ''))
  return Pipulate(lot)

def RunTests():
  '''Where you're going to develop everyhing these jobs can do!.'''
  out("Running tests... Just doin' a whole bunch of stuff.")
  return Pipulate([
    ('clear', ''),
    ('sheet', 'tests', [
      ('url','Title'),
      (globs.PIPURL, '?')
    ]),
    ('?', 'tests'),
    ('stop', '')
  ])

def ClearSheet1():
  '''Clear Sheet 1'''
  return Pipulate([
    ('clear', ''),
    ('stop', '')
  ])

def LinksOnPage():
  '''Collect links from displaying page.'''
  out("Getting links on page.")
  return Pipulate([
    ('clear', ''),
    ('table', [
      ('url','GetLinks'),
      (globs.PIPURL, '?')
    ])
  ])

def QuickCrawl():
  '''Collect links from displaying page and then visit each for more data..'''
  out("Getting links on page, then will visit.")
  return Pipulate([
    ('clear', ''),
    ('table', [
      ('url','GetLinks'),
      (globs.PIPURL, '?')
    ]),
    ('?', '')
  ])

def LinkGraph():
  '''Collect links from displaying page and prepare to visit each for more links..'''
  out("Getting links on page to get links on other pages.")
  return Pipulate([
    ('clear', ''),
    ('table', [
      ('url','PreCrawl'),
      (globs.PIPURL, '?')
    ])
  ])

def Cancel():
  '''Go back to default main menu.'''
  out("Cancel")
  return Pipulate()

