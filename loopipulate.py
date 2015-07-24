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

def Scheduler():
  import os.path
  if os.path.isfile(globs.TOKEN) and os.path.getsize(globs.TOKEN) > 0:
    import pickle
    tdict = pickle.load(open(globs.TOKEN, "rb"))
    token = tdict['access_token']
    creds = Credentials(access_token=token)
    import gspread
    # Login with your Google account
    gc = gspread.authorize(creds)
    doclist = gc.openall()
    for x in range(2): #Accomodate for API failures
      for onedoc in doclist:
        dockey = onedoc.get_id_fields()['spreadsheet_id']
        print(dockey)
        STREAMIT = Pipulate(dockey, token)
        for thebits in STREAMIT:
          print(thebits)
      print("*******************************************")
  else:
    print("Please run: python configure.py")

if __name__ == '__main__':
  socket.setdefaulttimeout(25)
  globs.mode = "cli"
  Scheduler()
