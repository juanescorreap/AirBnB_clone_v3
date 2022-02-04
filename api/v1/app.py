#!/usr/bin/python3
"""
returnS the status of the API
"""
from operator import imod
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session():
	"""Closes current context"""
	storage.close()

if __name__ == "__main__":
	host = os.getenv('HBNB_API_HOST')
	port = os.getenv('HBNB_API_PORT')
	if host is None:
		host = "0.0.0.0"
	if port is None:
		port = '5000'
	app.run(threaded=True)

