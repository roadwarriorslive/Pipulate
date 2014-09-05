import globs

def main():

  allrows = ''
  globs.DBSOURCE = 'gdocs'
  if globs.DBSOURCE == 'local':
    import shelve, csv
    allrows = shelve.open('drows.db')
    with open('sample.csv', newline='') as f:
      reader = csv.reader(f)
      for rowdex, row in enumerate(reader):
        allrows[str(rowdex)] = row
    allrows.close()
    allrows = shelve.open('drows.db')
    for rowkey in allrows:
      print(allrows[rowkey])
  elif globs.DBSOURCE == 'gdocs':
    import pickle, gspread
    login = pickle.load(open('temp.pkl', 'rb'))
    gc = gspread.login(login['username'], login['password'])
    wks = gc.open("Use This").sheet1
    for rowdex in range(1, wks.row_count):
      arow = wks.row_values(rowdex)
      if arow:
        print(str(arow))
      else:
        break
  else:
    pass

  return

  '''
  fargs = {}
  for item in allrows['0']:
    fname = allrows['0'][item]
    if fname in globals():
      fargs[fname] = {}
      from inspect import signature, _empty
      sig = signature(eval(fname))
      # print("%s is a function with arguments %s" % (fname, sig))
      for param in sig.parameters.values():
        pname = param.name
        pdefault = param.default
        #print(pdefault is _empty)
        #print('%s %s' % (pname, pdefault))
        if pdefault is _empty:
          fargs[fname][pname] = None
          # print('Required parameter: %s %s' % (fname, pname))
        else:
          fargs[fname][pname] = pdefault
          #print('I have default value for: %s %s %s' % (fname, pname, pdefault))
  # print(fargs)
  '''

  for item in allrows:
    if item != '0':
      print("%s: %s" % (item, allrows[item]))

def delrow(allrows, rowkey):
  try:
    del allrows[rowkey]
  except:
    pass

def Knights():
  return "Ni"

def Lumberjack(job, play='', status='Okay'):
  return "I'm okay"

if __name__ == "__main__":
  main()
