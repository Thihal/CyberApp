from flask import Flask
from tornado.options import define


app = Flask(__name__)
@app.route("/")
def homepage ():
    return "Hello CyberApp"


app.run(host="0.0.0.0",port=5000)
