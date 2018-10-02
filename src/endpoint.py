# endpoint.py
# this is the main application powering the website

# imports
from flask import Flask, request, jsonify, abort, render_template, redirect
from flask_cors import CORS
from src.helpers import *
import logging
import os

# constant
RESUME_URL = 'https://j0ma.keybase.pub/resume/resume.pdf'

# set up application
app = Flask(__name__)
CORS(app)

###### ROUTES ######
@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template('index.html')

@app.route('/research', strict_slashes=False)
def research():
    return render_template('research.html')

@app.route('/portfolio', strict_slashes=False)
def portfolio():
    return render_template('portfolio.html')

@app.route('/resume', strict_slashes=False)
def resume():
    return redirect(RESUME_URL)

@app.route('/baconipsum', methods=['POST'], strict_slashes=False)
def load_baconipsum():
    request_json = request.get_json()
    username = request_json['username']
    pw = request_json['username']
    assert username == 'sampleuser'
    assert password == 'samplepassword'
    with open('~/corpus_preprocessing_auth/baconipsum_document_corpus.csv', 'r') as f:
        txt = f.read()
    response = {}
    response['result'] = txt
    return jsonify(response)
