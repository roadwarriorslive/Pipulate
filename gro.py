import globs

def main():
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
    wks = gc.open("Use This").sheet1
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
    dofuncs(arow)
  else:
    print(arow)

def dofuncs(arow):
  fargs = {}
  for rowdex, fname in enumerate(arow):
    rowdex = rowdex + 1
    if fname in globals():
      fargs[rowdex] = {}
      from inspect import signature, _empty
      sig = signature(eval(fname))
      # print("%s is a function with arguments %s" % (fname, sig))
      for param in sig.parameters.values():
        pname = param.name
        pdefault = param.default
        #print(pdefault is _empty)
        #print('%s %s' % (pname, pdefault))
        if pdefault is _empty:
          fargs[rowdex][pname] = None
          # print('Required parameter: %s %s' % (fname, pname))
        else:
          fargs[rowdex][pname] = pdefault
          #print('I have default value for: %s %s %s' % (fname, pname, pdefault))
  print(fargs)

def Func1():
  return "Ni"

def Func2(param1, param2='', status='Okay'):
  return "I'm okay"

if __name__ == "__main__":
  main()
