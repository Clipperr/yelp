''' Functions related to users '''
# --- application module imports
from yelp.database_layer import database_read_user_by_phone, database_create_unverified_user


def create(phone_number):
    ''' creates a new user '''

    user = database_read_user_by_phone(phone_number)

    if user:
        return user

    return database_create_unverified_user(phone_number)

