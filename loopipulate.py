from dapipulate import *

def Scheduler():
  import pickle
  unpickleme = open("../opt/pipulate.pkl", "rb")
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

if __name__ == '__main__':
  Scheduler()
