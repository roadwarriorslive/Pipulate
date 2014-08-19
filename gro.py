def main():
  import shelve
  # https://www.youtube.com/watch?v=RQPBXNUwsRM Make our data persistent
  s = shelve.open('drows.db')
  # https://www.youtube.com/watch?v=q1kLEat9iFw Created first dict
  # https://www.youtube.com/watch?v=9jbTN9I-ce0 And made a dict of dicts
  try:
    # https://www.youtube.com/watch?v=iZOKsHzDaWg For efficient iteration
    s['0'] = {1:'foo',2:'bar',3:'Lumberjack'}
    s['Hello'] = {'foo':'Hello','bar':'World','Lumberjack':'?'}
    s['Spam'] = {'foo':'Spam','bar':'Eggs','Lumberjack':'?'}
  finally:
    s.close()

  s = shelve.open('drows.db')

  for item in s['0']:
    fname = s['0'][item]
    if fname in globals():
      print("%s is a function" % (fname))
    else:
      print("%s is not a function" % (fname))

  for item in s:
    if item != '0':
      print("%s: %s" % (item, s[item]))

def delrow(s, rowkey):
  try:
    del s[rowkey]
  except:
    pass

def Lumberjack():
  return "I'm okay"

# https://www.youtube.com/watch?v=G8T1BmIw3Hs Created point-of-entry for main
if __name__ == "__main__":
  main()
