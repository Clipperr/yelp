''' Main connection building and access to the database for Polygon application '''

# --- pymongo imports
from pymongo import MongoClient

# --- module imports
from config import DB_USER, DB_PASS, DB_URL, DB_DB

# make a connection to the db
client = MongoClient('mongodb+srv://' + DB_USER + ':' + DB_PASS + DB_URL + '/' + DB_DB)
polygon_db = client[DB_DB]



def database_insert(collection, data):
    ''' executes the insert call from pymongo for inserting the data to the db '''

    db_collection = polygon_db[collection]
    
    if isinstance(data, list):
        # insert all the documents in a list via a bulk insert
        db_collection.insert_many(data)
    
    else:
        # single insert
        db_collection.insert_one(data)




def database_read_one(collection, read_filter={}):
    ''' executes read command in pymongo to read data '''

    db_collecton = polygon_db[collection]

    return db_collecton.find_one(read_filter, {'_id' : 0})


def database_read_many(collection, read_filter={}):
    ''' reads many documents from the collection based on the read filter '''
    
    data = None

    db_collecton = polygon_db[collection]
    data = db_collection.find(read_filter, {'_id' : 0})

    return list(data) if data else None

