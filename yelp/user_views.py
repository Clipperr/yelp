# --- core python imports
import uuid

# python imports
from flask import jsonify, request

# app imports
from yelp import app
from yelp.auth import expects


@app.route('/')
def index():
    return jsonify({'message' : 'Hello World 2'})


@app.route('/search/<alias>', methods=['GET'])
def search_alias(alias):
    ''' searches if the alias is usable '''
    pass 


@app.route('/user/signup', methods=['POST'])
@expects(['first_name', 'last_name'])
def signup(data):
    ''' registers a user to the system '''
    return 'Welcome user' 
