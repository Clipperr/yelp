# pylint: disable=invalid-name,wrong-import-position
""" API Web Service """
# --- core python imports
# --- core python imports
# --- package imports
from flask import Flask
# --- package imports

# application objects
app = Flask(__name__)

# files containing views
from yelp import users_views