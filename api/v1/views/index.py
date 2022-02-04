#!/usr/bin/python3
"""
Route that returns status of the API
"""
from api.v1.views import app_views
from flask import jsonify

app_views.route('/status')


def api_status():
    return (jsonify({"status": "OK"}))
