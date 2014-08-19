def main():
  import shelve
  # https://www.youtube.com/watch?v=RQPBXNUwsRM Make our data persistent
  s = shelve.open('drows.db')
  try:
    # https://www.youtube.com/watch?v=q1kLEat9iFw Created first dict
    # https://www.youtube.com/watch?v=9jbTN9I-ce0 And made a dict of dicts
    s['drows'] = {
      'foo':{1:'foo',2:'bar',3:'Lumberjack',4:'I work all day'},
      'bar':{1:'foo',2:'bar',3:'Lumberjack',4:'I work all day'}
      }
  finally:
    s.close()

  s = shelve.open('drows.db')
  drow = s['drows']

  for item in drow:
    print(drow[item])

if __name__ == "__main__":
  main()
