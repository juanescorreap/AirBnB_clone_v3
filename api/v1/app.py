#!/usr/bin/python3
"""
returnS the status of the API
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": ["0.0.0.0"]}})

@app.teardown_appcontext
def close_session():
    """Closes current context"""
    storage.close()


@app.errorhandler(404)
def error_404():
    """Handles 404 errors"""
    return (jsonify({"error": "Not found"}))


if __name__ == "__main__":
    app_host = os.getenv("HBNB_API_HOST", default="0.0.0.0")
    app_port = os.getenv("HBNB_API_PORT", default=5000)
    app.run(host=app_host, port=int(app_port))
