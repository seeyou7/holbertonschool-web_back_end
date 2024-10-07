#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
# Import the Auth class
from api.v1.auth.auth import Auth  


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize the auth variable based on the AUTH_TYPE environment variable
auth = None
if getenv("AUTH_TYPE") == "auth":
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_error(error):
    """ Custom handler for 401 Unauthorized errors """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error):
    """ Custom handler for 403 Forbidden errors """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_handler():
    """ Handler for filtering requests before they reach the view functions """
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']

    # If the request path does not require auth, continue
    if not auth.require_auth(request.path, excluded_paths):
        return

    # If there is no authorization header, abort with 401 Unauthorized
    if auth.authorization_header(request) is None:
        abort(401)

    # If the current user is not found, abort with 403 Forbidden
    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
