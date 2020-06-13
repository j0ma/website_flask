# endpoint.py
# this is the main application powering the website

# imports
from flask import Flask, request, jsonify, abort, render_template, redirect
from flask_cors import CORS
import logging
import os

# constant
RESUME_URL = 'https://j0ma.keybase.pub/resume/resume.pdf'
YI_LREC_URL = 'https://gitlab.com/jonnesaleva/yiddish-lrec-2020'
YI_LREC_PAPER_URL = "http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.119.pdf"
YI_CORPUS_URL = 'https://j0ma.keybase.pub/datasets/multi_orthography_parallel_corpus_of_yiddish_nouns.csv'

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

@app.route('/yi-lrec', strict_slashes=False)
def yiddish():
    return redirect(YI_LREC_URL)

@app.route('/yi-lrec-paper', strict_slashes=False)
def yiddish_paper():
    return redirect(YI_LREC_PAPER_URL)

@app.route('/discourse-relation-classification', strict_slashes=False)
def discourse_relation_classification():
    return render_template('discourse-relation-classification.html')

@app.route('/yelp-sentiment-analysis', strict_slashes=False)
def yelp_sentiment_analysis():
    return render_template('yelp-sentiment-analysis.html')

@app.route('/multi-orthography-yiddish-corpus', strict_slashes=False)
def corpus():
    return redirect(YI_CORPUS_URL)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
