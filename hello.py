from flask import Flask
app = Flask(__name__)

from pipulate import *

@app.route("/")
def hello():
  main() 

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
