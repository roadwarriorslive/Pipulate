from pipulate import *

if __name__ == "__main__":
  globs.mode = "web"
  if 'pipulate' in socket.gethostname():
    app.run(host='0.0.0.0', port=80, debug=True)
  else:
    app.run(host='0.0.0.0', port=8888, debug=False)
