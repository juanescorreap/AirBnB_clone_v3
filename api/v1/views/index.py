#!/usr/bin/python3
"""
Route that returns status of the API
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def api_status():
    """JSON with the status of the API"""
    return (jsonify({"status": "OK"}))


@app_views.route('/api/v1/stats', strict_slashes=False)
def class_objects():
    """retrieves the number of each objects by type"""
    objects_dict = {"amenities": storage.count('Amenity'),
                    "cities": storage.count('City'),
                    "places": storage.count('Place'),
                    "reviews": storage.count('Review'),
                    "states": storage.count('State'),
                    "users": storage.count('User')}
    return(jsonify(objects_dict))
