''' Custom exception module '''

# --- python module imports
from flask import jsonify

# --- local module imports
from yelp import app

class InvalidUsage(Exception):

    def __init__(self, message, status_code=None, payload=None):
        
        # initialize the base Exception class
        Exception.__init__(self)

        self.message = message
        
        if status_code is not None:
            self.status_code = status_code
        
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status_code'] = self.status_code
        return rv




@app.errorhandler(InvalidUsage)
def handle_invalid_usage_error(error):
    ''' Global error handler on application error '''

    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

