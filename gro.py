import globs

def main():
  '''This main function could have been the entire dosheet function, but this
  extra level allows for looping trough multiple worksheet sources and serves
  as a hook for future automation like scheduled tasks.'''
  funcs = [x for x in globals().keys() if x[:2] != '__']
  globs.funcslc = [x.lower() for x in funcs]
  globs.transfunc = dict(zip(globs.funcslc, funcs)) 
  for dbsource in ['gdocs', 'local']:
    dosheet(dbsource)
    print()

def dosheet(dbsource):
  '''The purpose of this function is to feed Python lists representing rows of
  a spreadsheet into the processrow function, which handles question mark
  replacement. This is the outer loop of that process representing the entire
  spreadsheet. In the first case, data can be loaded into a shelve object from
  csv and other sources for processing large datasets and scheduled tasks, or
  from Google Spreadsheets for lesser data, but a more interactive approach.'''
  allrows = ''
  if dbsource == 'local':
    import shelve, csv
    allrows = shelve.open('drows.db')
    with open('sample.csv', newline='') as f:
      reader = csv.reader(f)
      for rowdex, arow in enumerate(reader):
        allrows[str(rowdex + 1)] = arow
    allrows.close()
    allrows = shelve.open('drows.db')
    for rowkey in sorted(allrows):
      processrow(rowkey, allrows[rowkey])
  elif dbsource == 'gdocs':
    import pickle, gspread
    login = pickle.load(open('temp.pkl', 'rb'))
    gc = gspread.login(login['username'], login['password'])
    try:
      wks = gc.open("Use This").sheet1
    except:
      print("Couldn't reach Google Docs")
      return
    for rowdex in range(1, wks.row_count):
      arow = wks.row_values(rowdex)
      if arow:
        processrow(str(rowdex), arow)
      else:
        break
  else:
    pass

def dorow(rownum, arow):
  '''Called on each row of a worksheet and either initializes functions when
  it's row 1, or steps cell by cell along each subsequent (fed-in) row and when
  encountering a question mark, it determines whether to invoke the function
  indicated by the column label, using values from the active row as parameter
  values if available, parameter defaults if not, and None if no defaults.'''
  if rownum == '1':
    globs.row1 = [x.lower() for x in arow]
    row1funcs(arow)
  else:
    for coldex, acell in enumerate(arow):
      if globs.row1[coldex] in globs.funcslc:
        if acell == '?':
          evalfunc(coldex, arow)

def evalfunc(coldex, arow):
  '''Once a question mark is found in a cell belonging to a function-named
  column, the exact invocation that's needed must be built, keeping in mind
  default values provided by function itself, as well as parameter values
  provided in the provided row. Because rows are being handled as lists, order
  is important, and the column index allows function name lookup.'''
  fname = globs.transfunc[globs.row1[coldex]]
  fargs = globs.fargs[coldex]
  evalme = "%s(" % fname
  if fargs:
    for anarg in fargs:
      anarg = anarg.lower()
      argval = getargval(anarg, fargs[anarg], arow)
      evalme = "%s%s=%s, " % (evalme, anarg, argval)
    evalme = evalme[:-2] + ')'
  else:
    evalme = evalme + ')'
  print('%s: %s' % (evalme, eval(evalme)))

def getargval(anarg, defargval, arow):
  '''This function returns which value should be used as the arguments to the
  function invocation string being built. The value found on the row always
  beats the default provided by the function. Lacking values on the row and a
  default, the Python value of None will be returned.'''
  for coldex, acol in enumerate(globs.row1):
    if acol == anarg:
      if arow[coldex]:
        return adq(arow[coldex])
  if defargval:
    return adq(defargval)
  else:
    return None
  
def adq(aval):
  '''This handles the value quoting details when building argument part of the
  function invocation string when replacing a question mark. For example, the
  keyword None must not become quoted. Typically, numbers shouldn't be quoted
  either, but we're feeding everything but None around as strings for now.'''
  if aval == None:
    return None
  else:
    return "'%s'" % (aval)

def row1funcs(arow):
  '''This is only invoked on row 1 of a spreadsheet, where the names of
  functions and parameters are expected to be discovered. By the end, we've
  created a dictionary of dictionaries called globs.fargs which plays an
  important role in building the code necessary for question mark
  replacement.'''
  fargs = {}
  for coldex, fname in enumerate(arow):
    if fname.lower() in globs.funcslc:
      fargs[coldex] = {}
      from inspect import signature, _empty
      sig = signature(eval(fname))
      for param in sig.parameters.values():
        pname = param.name
        pdefault = param.default
        if pdefault is _empty:
          fargs[coldex][pname] = None
        else:
          fargs[coldex][pname] = pdefault
  globs.fargs = fargs

def Func1():
  return "No arguments here"

def Func2(param1, param2='', status='Okay'):
  return "My params are: %s, %s" % (param1, param2)

if __name__ == "__main__":
  main()
