from flask import Flask
app = Flask(__name__)

from pipulate import *
from flask import request

@app.route("/")
def hello():
  if "go" in request.args:
    main() 
    return "Replaced questionmarks"
  return "Doing nothing"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
