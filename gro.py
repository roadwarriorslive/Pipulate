import globs

def main():
  funcs = [x for x in globals().keys() if x[:2] != '__']
  globs.funcslc = [x.lower() for x in funcs]
  globs.transfunc = dict(zip(globs.funcslc, funcs)) 
  #print(globs.gfuncs)
  #return
  for dbsource in ['gdocs', 'local']:
    dosheet(dbsource)
    print()

def dosheet(dbsource):
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
      dorow(rowkey, allrows[rowkey])
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
        dorow(str(rowdex), arow)
      else:
        break
  else:
    pass

def dorow(rownum, arow):
  if rownum == '1':
    globs.row1 = [x.lower() for x in arow]
    #print(globs.row1)
    #return
    row1funcs(arow)
  else:
    for coldex, acell in enumerate(arow):
      if globs.row1[coldex] in globs.funcslc:
        if acell == '?':
          evalfunc(coldex, arow)

def evalfunc(coldex, arow):
  fname = globs.transfunc[globs.row1[coldex]]
  #print(globs.fargs)
  #return
  fargs = globs.fargs[coldex]
  evalme = "%s(" % fname
  if fargs:
    #print(fname, fargs)
    for anarg in fargs:
      anarg = anarg.lower()
      argval = getargval(anarg, fargs[anarg], arow)
      evalme = "%s%s=%s, " % (evalme, anarg, argval)
      #if fargs[anarg] == None: 
        #print(fname, anarg)
    evalme = evalme[:-2] + ')'
  else:
    evalme = evalme + ')'
  print('%s: %s' % (evalme, eval(evalme)))

def getargval(anarg, defargval, arow):
  for coldex, acol in enumerate(globs.row1):
    if acol == anarg:
      if arow[coldex]:
        return adq(arow[coldex])
  if defargval:
    return adq(defargval)
  else:
    return None
  
def adq(aval):
  if aval == None:
    return None
  else:
    return "'%s'" % (aval)

def row1funcs(arow):
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
  #print(fargs)
  globs.fargs = fargs

def Func1():
  return "No arguments here"

def Func2(param1, param2='', status='Okay'):
  return "My params are: %s, %s" % (param1, param2)

if __name__ == "__main__":
  main()
