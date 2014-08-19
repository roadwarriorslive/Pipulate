import shelve
s = shelve.open('drows.db')
try:
  s['drows'] = {1:'foo',2:'bar',3:'Lumberjack',4:'I work all day'}
finally:
  s.close()

s = shelve.open('drows.db')
drow = s['drows']

for item in drow:
  print(drow[item])
