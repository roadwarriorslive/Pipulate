#   ____                   ____  _     _           
#  / ___|_ __ ___  _ __   / ___|| |__ (_)_ __ ___  
# | |   | '__/ _ \| '_ \  \___ \| '_ \| | '_ ` _ \ 
# | |___| | | (_) | | | |  ___) | | | | | | | | | |
#  \____|_|  \___/|_| |_| |____/|_| |_|_|_| |_| |_|
#                                                  
#   It'd be a cryin' shame to tie timing things
#                 To schedule-APIs
#     When a mere cron shim is much more sane
#            For tasks that death defies!

from pipulate import *
import globs

def freshtoken(picklefile):
  import pickle
  tdict = pickle.load(open(picklefile, "rb"))
  token = tdict['access_token']
  return token

def Scheduler():
  import os.path
  if os.path.isfile(globs.TOKEN) and os.path.getsize(globs.TOKEN) > 0:
    token = freshtoken(globs.TOKEN)
    creds = Credentials(access_token=token)
    import gspread
    gsp = gspread.authorize(creds)
    doclist = gsp.openall()
    for x in range(2): #Accomodate for API failures
      for onedoc in doclist:
        dockey = onedoc.get_id_fields()['spreadsheet_id']
        print(dockey)
        STREAMIT = Pipulate(dockey, token)
        for thebits in STREAMIT:
          print(thebits)
      print("*"*50)
  else:
    print("Please configure Pipulate by visiting from a browser.")

if __name__ == '__main__':
  socket.setdefaulttimeout(25)
  globs.mode = "cli"
  Scheduler()
