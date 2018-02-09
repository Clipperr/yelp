''' Utility functions for application '''

# --- python module imports
from flask import request


def posted():
    ''' return request data or an empty dict '''

    return request.get_json(force=True, silent=True) or {}
    
