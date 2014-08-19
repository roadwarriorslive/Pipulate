def main():
  import shelve
  # https://www.youtube.com/watch?v=RQPBXNUwsRM Make our data persistent
  s = shelve.open('drows.db')
  # https://www.youtube.com/watch?v=q1kLEat9iFw Created first dict
  # https://www.youtube.com/watch?v=9jbTN9I-ce0 And made a dict of dicts
  try:
    # https://www.youtube.com/watch?v=iZOKsHzDaWg For efficient iteration
    # https://www.youtube.com/watch?v=efL6qgVxfz0 Defined meaning of these dicts
    s['0'] = {1:'foo',2:'bar',3:'Lumberjack'}
    s['Hello'] = {'foo':'Hello','bar':'World','Lumberjack':'?'}
    s['Spam'] = {'foo':'Spam','bar':'Eggs','Lumberjack':'?'}
  finally:
    s.close()

  s = shelve.open('drows.db')

  for item in s['0']:
    fname = s['0'][item]
    if fname in globals():
      from inspect import signature, _empty
      # https://www.youtube.com/watch?v=WLW1-G56q1c Get the function's args
      sig = signature(eval(fname))
      print("%s is a function with arguments %s" % (fname, sig))
      for param in sig.parameters.values():
        pname = param.name
        pdefault = param.default
        #print(pdefault is _empty)
        #print('%s %s' % (pname, pdefault))
        if pdefault is _empty:
          print('Required parameter: %s %s' % (fname, pname))
        else:
          print('I have default value for: %s %s %s' % (fname, pname, pdefault))

  # https://www.youtube.com/watch?v=iZOKsHzDaWg Efficiently iterating
  for item in s:
    if item != '0':
      print("%s: %s" % (item, s[item]))

def delrow(s, rowkey):
  # https://www.youtube.com/watch?v=5oCRfOndrvY Deleting item from dictionary
  # https://www.youtube.com/watch?v=fe5QFldVzh4 Breaking into its own function
  try:
    del s[rowkey]
  except:
    pass

def Lumberjack(job, play='', status='Okay'):
  return "I'm okay"

# https://www.youtube.com/watch?v=G8T1BmIw3Hs Created point-of-entry for main
if __name__ == "__main__":
  main()
