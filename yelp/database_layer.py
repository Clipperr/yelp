''' An abtraction layer for the database.py module '''

# --- python imports
import uuid

# --- app module imports
from yelp.database import database_read_one, database_insert, database_update_one


# collection name constants
COLLECTION_OTP = 'otp'
COLLECTION_USER = 'user'



def database_read_unexpired_otp(key, ts):
    ''' reads otp from db agains the given key '''

    return database_read_one(COLLECTION_OTP, {'key' : key, 'expiration_time' : {'$gt' : ts}})


def database_read_otp(key, otp):
    ''' reads otp from db agains the given key '''

    return database_read_one(COLLECTION_OTP, {'key' : key, 'otp' : otp})




def database_add_otp(key, otp, generation_time, expiration_time):
    ''' adds a new otp in db against the give key'''

    otp = {
        'id' : '{0}'.format(uuid.uuid4()),
        'otp' : otp,
        'key' : key,
        'expiration_time' : expiration_time,
        'last_sms_sent' : generation_time
    }

    database_insert(COLLECTION_OTP, otp)



def database_update_otp_time(ts, otp):
    ''' updates last_sms_sent_time '''

    otp.update({
        'last_sms_sent' : ts
    })

    database_update_one(COLLECTION_OTP, otp)



def database_read_user_by_phone(phone_number):
    ''' read user by phone number '''

    return database_read_one(COLLECTION_USER, {'phone_number' : phone_number})


def database_create_unverified_user(phone_number):
    
    user = {
        'id' : '{0}'.format(uuid.uuid4()),
        'first_name' : '',
        'last_name' : '',
        'alias' : '',
        'full_name' : '',
        'phone_number' : phone_number,
        'phone_verified' : False,
        'signup_time' : 0,
        'pass_hash' : '',
        'pass_salt' : '',
        'session_id' : '',
        'r_id' : []
    }

    database_insert(COLLECTION_USER, user)

    return user


def database_update_user_registration(phone_number, first_name, last_name, alias, signup_time):
    
    user = database_read_one(COLLECTION_USER, {'phone_number' : phone_number})

    if user:
        user.update({
            'first_name' : first_name,
            'last_name' : last_name,
            'full_name' : ' '.join([first_name, last_name]),
            'alias' : alias,
            'signup_time' : signup_time
        })

        database_update_one(COLLECTION_USER, user)
        return user

    return None


def database_update_user_phone_verified(user):
    ''' updates user status to phone verified '''
    
    user.update({
        'phone_verified' : True
    })

    database_update_one(COLLECTION_USER, user)


def database_check_alias_availability(alias):
    ''' checks availability of alais '''

    if database_read_one(COLLECTION_USER, {'alias' : alias}):
        return False

    return True
