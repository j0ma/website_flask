# endpoint.py
# this is the main application powering the website

# imports
from flask import Flask, request, jsonify, abort, render_template, redirect
from flask_cors import CORS
import src.helpers as h
import logging
import os

# constant
RESUME_URL = 'https://j0ma.keybase.pub/resume/resume.pdf'
YI_LREC_URL = 'https://gitlab.com/jonnesaleva/yiddish-lrec-2020'
YI_LREC_PAPER_URL = "https://bit.ly/37xrPX4"
YI_CORPUS_URL = 'https://j0ma.keybase.pub/datasets/multi_orthography_parallel_corpus_of_yiddish_nouns.csv'
BLOG_PATH='blog'

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

@app.route('/blog', strict_slashes=False)
def blog():
    try:
        posts = h.load_blog_posts(BLOG_PATH)
        return render_template('blog.html', posts=posts)
    except:
        return abort(404)

@app.route('/blog/<identifier>', strict_slashes=False)
def blog_post(identifier="001-hello-world"):
    try:
        with open(f'blog/{identifier}.txt', 'r') as f:
            blog_post_content = f.read()
            header_info, post = h.process_blog_post(blog_post_content)
            title = header_info['title']
        return render_template('blog-post.html', 
                                post_title=title, 
                                post_content=post)
    except:
        return abort(404)

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
