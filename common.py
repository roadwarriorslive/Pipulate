import globs

def gotcha(x=''):
  print('''
                   ____       _       _             _   _   _ 
                  / ___| ___ | |_ ___| |__   __ _  | | | | | |
                 | |  _ / _ \| __/ __| '_ \ / _` | | | | | | |
                 | |_| | (_) | || (__| | | | (_| | |_| |_| |_|
                  \____|\___/ \__\___|_| |_|\__,_| (_) (_) (_)
  ''')
  if x:
    if type(x) == list or type(x) == dict or type(x) == tuple:
      import pprint
      print("\n")
      pprint.pprint(x)
      print("\n")
    else:
      out("Gotcha !!! %s !!! </%s>" % (x, globs.nest[-1:]))
  else:
    out("Gotcha!!! </%s>" % globs.nest[-1:])
  globs.nest = globs.nest[:-2]
  raise SystemExit

def InsertRows(onesheet, listoflists, lastrowused=''):
  numnewrows = len(listoflists)
  if not lastrowused:
    lastrowused = globs.numrows
  numrowsneeded = len(listoflists)
  allrowsevenempty = onesheet.row_count
  availableblankrows = allrowsevenempty - lastrowused
  if availableblankrows < numrowsneeded:
    rowstoadd = numrowsneeded - availableblankrows
    onesheet.add_rows(rowstoadd)
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

  stop = True
  for x in range(5):
    try:
      CellList = onesheet.range(rowrange)
      stop = False
      break
    except:
      out("Retry %s of %s" % (x, 5))
      time.sleep(5)
  if stop:
    Stop()
      
  for index, onecell in enumerate(CellList):
    try:
      onecell.value = flattenitlist[index]
    except:
      pass

  for x in range(5):
    try:
      onesheet.update_cells(CellList)
      stop = False
      break
    except:
      out("Retry %s of %s" % (x, 5))
      time.sleep(5)
  if stop:
    Stop()
    
  return

