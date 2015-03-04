from pipulate import *

def Scheduler(filename):
  import os.path
  if os.path.isfile(filename) and os.path.getsize(filename) > 0:
    import pickle
    unpickleme = open(filename, "rb")
    answers = pickle.load(unpickleme)
    unpickleme.close()
    username = answers['username']
    password = answers['password']
    import gspread

    # Login with your Google account
    gc = gspread.login(username, password)
    doclist = gc.openall()
    for x in range(2): #Accomodate for API failures
      for onedoc in doclist:
        dockey = onedoc.get_id_fields()['spreadsheet_id']
        print(dockey)
        STREAMIT = Pipulate(username, password, dockey)
        for thebits in STREAMIT:
          print(thebits)
      print("*******************************************")
  else:
    print("Please run: python configure.py")

if __name__ == '__main__':
  socket.setdefaulttimeout(25)
  globs.mode = "cli"
  filename = "/var/opt/pipulate.pkl"
  Scheduler(filename)
