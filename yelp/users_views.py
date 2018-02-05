# python imports
from flask import jsonify, request

# app imports
from yelp import app


@app.route('/')
def index():
    return jsonify({'message' : 'Hello World 2'})


@app.route('/search/<alias>', methods=['GET'])
def search_alias(alias):
    """ searches if the alias is usable """
    pass


@app.route('/signup', methods=['POST'])
def signup(data):
    """ registers a user to the system """
    pass
