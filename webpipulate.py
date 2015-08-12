#   __        __   _       ____  _     _
#   \ \      / /__| |__   / ___|| |__ (_)_ __ ___
#    \ \ /\ / / _ \ '_ \  \___ \| '_ \| | '_ ` _ \
#     \ V  V /  __/ |_) |  ___) | | | | | | | | | |
#      \_/\_/ \___|_.__/  |____/|_| |_|_|_| |_| |_|
#
#  What brought the kindred spider to that height,
# Then steered the white moth thither in the night?
#      What but design of darkness to appall?--
#       If design govern in a thing so small.
#              -- Robert Frost, Design

from pipulate import *
import os
import globs, common
print(r'''
                      Welcome to Pipulate, running on:
      ____        _   _                    _______ _           _
     |  _ \ _   _| |_| |__   ___  _ __    / /  ___| | __ _ ___| | __
     | |_) | | | | __| '_ \ / _ \| '_ \  / /| |_  | |/ _` / __| |/ /
     |  __/| |_| | |_| | | | (_) | | | |/ / |  _| | | (_| \__ \   <
     |_|    \__, |\__|_| |_|\___/|_| |_/_/  |_|   |_|\__,_|___/_|\_\
            |___/
 
Hello World! I am a native Python webserver: no Apache, nginx or node.js.
Pipulate is designed for exclusive access to the webserver, giving you the
chance to watch the webserver's console output like a log file. Here's how the
process generally looks. Feel free to crack it open and customize.

  THIS IS     THIS IS YOUR BROWSER                  THIS IS PIPULATE
    YOU            ____ ____                      (disposable servers)
               ,__/site\____\___.  ...which       ,------------------.
     O         |                ||     SENDS      |   ...to the      |
    /|\---1.-----> bookmarklet -----------2.-------> Pipulate Server |
    ( ) CLICK  | with a website ||      URL and   |   | which checks |
   =====       |   displaying.  ||       context  '---|----|--|--|---'
     |         |                ||                    |    |  |  |
     5.        |                ||                    |    |  |  '-----> ?
     |         '----------------'|      then sends    |    |  '--------> ?
   SEE THE--->  |to Google sheet<----------4.---------'    '-----3.----> ?
   RESULTS      '----------------'   a response           ...stuff on net

''')

if __name__ == "__main__":
  globs.WEB = True
  if 'pipulate' in socket.gethostname():
    globs.PCOM = True
    app.run(host='0.0.0.0', port=80, debug=True)
  else:
    app.run(host='0.0.0.0', port=8888, debug=False)

