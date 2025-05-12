from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello world"

@app.route('/play')
def play():
  subprocess.Popen(["mpc", "play"])
  return 'play - ok'

@app.route('/pause')
def pause():
  subprocess.Popen(["mpc", "pause"])
  return 'pause - ok'

@app.route('/repeat')
def repeat():
  subprocess.Popen(["mpc", "repeat", "on"])
  return 'repeat - ok'