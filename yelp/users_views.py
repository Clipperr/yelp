# python imports
from flask import jsonify, request

# app imports
from yelp import app


@app.route('/')
def index():
    return jsonify({'message' : 'Hello World 2'})
