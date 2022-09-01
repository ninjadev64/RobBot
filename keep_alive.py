from flask import Flask
from threading import Thread
app = Flask("RobBot GD")

@app.route("/")
def home():
	return "Go play Geometry Dash!"

def run():
	from waitress import serve
	serve(app, host = '0.0.0.0', port = 8080)

def keep_alive():
    Thread(target = run).start()