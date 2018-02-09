''' Authentication and validation middlewares '''

# --- core python imports
from functools import wraps


def expects(fields):
    ''' middleware for validation of request data requirements '''

    def decorator(view_function):
        '''' decorating around the view_function '''
        @wraps(view_function)
        def wrapper(*args, **kwargs):
            
            if not fields:
                return view_function({}, *args, **kwargs)

            
            from .utils import posted
            from .errors import InvalidUsage
            data = posted()

            # convert the received fields into a key value pair by getting their values from the data
            received = {key : data.get(key) for key in fields if data.get(key) not in [None, '']}

            if set(received.keys()) != set(fields):
                # raise exception
                raise InvalidUsage(message='Missing expected fields: ' + str(set(fields) - set(received.keys())))
               

            return view_function(received, *args, **kwargs)

        return wrapper
    return decorator


