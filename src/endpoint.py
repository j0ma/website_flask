# endpoint.py
# this is the main application powering the website
# (c) jonne saleva, 2018

# imports
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from src.helpers import *
import logging
import os

# set up application
app = Flask(__name__)
CORS(app)

###### ROUTES ######
@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    return 'Hello World'
