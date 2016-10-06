import os, os.path, pickle

def askquestions(filename):
  questions = dictofquestions()
  answers = {}
  previousanswers = showanswers(filename)
  sortedquestions = sorted(questions.keys())
  for question in sortedquestions:
    if isinstance(previousanswers, dict):
      answer = raw_input(question + ' (Hit ENTER to keep "' + previousanswers[questions[question]] + '"): ')
    else:
      answer = raw_input(question + ': ')
    if answer:
      answers[questions[question]] = answer
    elif isinstance(previousanswers, dict):
      answers[questions[question]] = previousanswers[questions[question]]
    else:
      answers[questions[question]] = ''
  return answers

def saveanswers(pickleme, filename):
  output = open(filename, 'wb')
  pickle.dump(pickleme, output)
  output.close()

def showanswers(filename):
  answers = ''
  if os.path.isfile(filename) and os.path.getsize(filename) > 0:
    input = open(filename, 'rb')
    answers = pickle.load(input)
    input.close()
  else:
    answers = "Username and Password has not been assigned to this server yet."
  return answers

def dictofquestions():
  return {
    '1. GMail Username' : 'username',
    '2. GMail Password' : 'password'
  }

warning = ('''
Welcome to Pipulate. Generally, you want to avoid putting any username and
password information on a server, in case it's hacked, or in the unique case of
Pipulate, you pass your Levinux virtual machine file or Raspbery Pi SD card
image around. None-the-less, it is curreintly the best way to achieve reliable
scheduling. I recommend setting up a GMail account just for Pipulate, and then
turning on 2-Step Verification, and then selecting App-specific passwords. 
https://security.google.com/settings/security/apppasswords?pli=1
Select App: Other, Device: Other and Generate. Use the specially generated
password with Pipulate so that any time you can revoke that server's access
without having to use the GMail account's master password.
''')

if __name__ == "__main__":
  print(warning)
  topickle = askquestions("../opt/pipulate.pkl")
  saveanswers(topickle, "../opt/pipulate.pkl")
  print("\nUsername and Password recorded!")
