from dapipulate import *

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
    while True:
      for onedoc in doclist:
        dockey = onedoc.get_id_fields()['spreadsheet_id']
        print(dockey)
        STREAMIT = Pipulate(username, password, dockey)
        for thebits in STREAMIT:
          print(thebits)
      print("*******************************************")
      time.sleep(10)
  else:
    print("Please run: python configure.py")

if __name__ == '__main__':
  socket.setdefaulttimeout(25)
  globs.mode = "cli"
  filename = "../opt/pipulate.pkl"
  Scheduler(filename)
