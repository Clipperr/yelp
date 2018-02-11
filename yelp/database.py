''' Main connection building and access to the database for Polygon application '''

# --- pymongo imports
from pymongo import MongoClient

# --- module imports
from config import DB_USER, DB_PASS, DB_URL, DB_DB

# make a connection to the db
client = MongoClient('mongodb+srv://' + DB_USER + ':' + DB_PASS + DB_URL + '/' + DB_DB)


