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

if __name__ == "__main__":
  globs.mode = "web"
  if 'pipulate' in socket.gethostname():
    globs.PCOM = True
    app.run(host='0.0.0.0', port=80, debug=True)
  else:
    app.run(host='0.0.0.0', port=8888, debug=False)
  if os.path.isfile(globs.FILE) and os.path.getsize(globs.FILE) > 0:
    app.config.from_pyfile(globs.FILE, silent=False)


