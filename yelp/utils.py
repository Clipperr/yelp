''' Utility functions for application '''

# -- python imports
import random
import time

# --- python module imports
from flask import request

# --- app module imports
from yelp.config.config import OTP_LEN, OTP_EXPIRATION_TIME, SMS_THROTLE_TIME
from yelp.database_layer import database_update_otp_time, database_add_otp, database_read_otp

TIME_SEC = 60 # seconds

def posted():
    ''' return request data or an empty dict '''

    return request.get_json(force=True, silent=True) or {}


def current_time():
    ''' get current timestamp '''
    return time.time()



def generate_otp(key):
    ''' generate otp against a key '''

    ts = current_time()
    otp = database_read_otp(key, ts)

    if otp:
        if otp['last_sms_sent'] + (TIME_SEC * SMS_THROTLE_TIME) > ts:
            return (otp['otp'], True)
        else:
            database_update_otp_time(ts, otp)
            return (otp['otp'], False)
    
    # generate an OTP of specified length
    otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
    
    expiration_time = ts + (TIME_SEC * OTP_EXPIRATION_TIME)

    # add OTP into db
    database_add_otp(key, otp, ts, expiration_time)

    return (otp, False)
