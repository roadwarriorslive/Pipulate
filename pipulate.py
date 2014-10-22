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
https://www.youtube.com/watch?v=SdzDaohx-GA&list=PLy-AlqZFg6G8tBTB6FFN68mryG4JlCaf-"""

import globs #Create objects that don't have to be passed as arguments.
from flask import Flask, request, render_template
from flask_wtf import Form
from flask_wtf.file import FileField
from wtforms import validators, StringField
from wtforms.validators import DataRequired, Optional, Required

app = Flask(__name__, static_folder='../uploads', static_url_path='/files')

class RequiredIf(object):
  """Validates field conditionally.

  Usage::

    login_method = StringField('', [AnyOf(['email', 'facebook'])])
    email = StringField('', [RequiredIf(login_method='email')])
    password = StringField('', [RequiredIf(login_method='email')])
    facebook_token = StringField('', [RequiredIf(login_method='facebook')])
  """
  def __init__(self, *args, **kwargs):
    self.conditions = kwargs

  def __call__(self, form, field):
    for name, data in self.conditions.items():
      if name not in form._fields:
        Optional(form, field)
      else:
        condition_field = form._fields.get(name)
        if condition_field.data == data and not field.data:
          Required()(form, field)
    Optional()(form, field)

class PipForm(Form):
  gkey = StringField('Your Google Spreadsheet Key', [RequiredIf(csvfile='')])
  csvfile = FileField('Your CSV File', [RequiredIf(gkey='')])

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1] in globs.ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def main():
  if request.method == 'POST':
    form = PipForm(csrf_enabled=False)
    if form.validate_on_submit():
      if form.gkey.data:
        globs.GKEY = form.gkey.data
        pipulate('gdocs')
        return render_template('pipulate.html', form=form)
      if form.csvfile.data:
        import os
        from werkzeug import secure_filename        
        app.config['UPLOAD_FOLDER'] = globs.UPLOAD_FOLDER
        file = request.files['csvfile']
        if file and allowed_file(file.filename):
          globs.filename = secure_filename(file.filename)
          file.save(os.path.join(globs.UPLOAD_FOLDER, globs.filename))
        pipulate('local')
        return render_template('pipulate.html', form=form)
    return render_template('pipulate.html', form=form)
  else:
    form = PipForm(csrf_enabled=False)
    return render_template('pipulate.html', form=form)

def pipulate(dbsource):
  """Allows processing of multiple worksheets.

  During testing, this is set to process one Google Spreadsheet and one local
  csv file. It also creates a list of global functions and translation table to
  their lower-case versions for recognizing function names in column labels.
  A Pythonic switch statement calls dbgdocs once and dblocal once."""
  funcs = [x for x in globals().keys() if x[:2] != '__'] #List all functions
  globs.funcslc = [x.lower() for x in funcs] #Lower-case all function names
  globs.transfunc = dict(zip(globs.funcslc, funcs)) #Keep translation table
  dbmethod = {'local': dblocal, 'gdocs': dbgdocs}
  dbmethod[dbsource]()

def dblocal():
  """Loads a local csv file and dumps it into shelve object for processing.

  While support for csv files will be very useful for many people, using the
  shelve API here is to leave a hook for the external shove library which will
  allow this to run on MUCH larger datasets by connecting it to Redis, Amazon
  S3, Berkeley DB, Postgres or other backend databases."""
  import shelve, csv, os
  try:
    os.remove('drows.db')
  except OSError:
    pass
  allrows = shelve.open('drows.db')
  with open(os.path.join(globs.UPLOAD_FOLDER, globs.filename), newline='') as f:
    reader = csv.reader(f)
    for rowdex, arow in enumerate(reader): #Dump entire csv into shelve.
      allrows[str(rowdex + 1)] = arow
  allrows.close()
  #We can add support for much more than csv here through "shove" module.
  allrows = shelve.open('drows.db')
  for rowkey in sorted(allrows): #Process each row (list) from the shelve.
    newrow = processrow(rowkey, allrows[rowkey])
    allrows[rowkey] = newrow
  with open(os.path.join(globs.UPLOAD_FOLDER, globs.filename),'w', newline='') as f:

    w = csv.writer(f)
    for rowkey in sorted(allrows):
      w.writerow(list(allrows[rowkey]))

def dbgdocs():
  """Keeps a Google Spreadsheet open for row-by-row processing.

  While Google Spreadsheets is not the most efficient or scalable way to manage
  this process, it provides a ready-made user interface for convenient
  interactive sessions with smaller datasets. Demonstrating this approach to
  people is impressive and has a compelling charm."""
  import pickle, gspread
  login = pickle.load(open('temp.pkl', 'rb'))
  gc = gspread.login(login['username'], login['password'])
  try:
    wks = gc.open_by_key(globs.GKEY).sheet1 #HTTP connection errors happen here.
    # https://docs.google.com/spreadsheets/d/182yAd0VYBhY30IW1sGXUg110aWh0pMaQa4nVtWXgNBo/edit?usp=sharing
  except:
    print("Couldn't reach Google Docs")
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
      from inspect import signature, _empty
      sig = signature(eval(fname))
      for param in sig.parameters.values(): #Build dict of function reqirements
        pname = param.name
        pdefault = param.default
        if pdefault is _empty: #Catch when an argument has no default value
          fargs[coldex][pname] = None
        else:
          fargs[coldex][pname] = pdefault
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

def Func1():
  return "Out from func1"

def Func2(param1, param2='', status='Okay'):
  return "%s %s" % (param1, param2)

#if __name__ == "__main__":
#  main()

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
