# --- core python imports
import uuid

# python imports
from flask import jsonify, request

# app imports
from yelp import app
from yelp.errors import InvalidUsage
from yelp.auth import expects
from yelp.utils import posted, generate_otp, verify_otp, current_time
from yelp.users import create
from yelp.database_layer import database_update_user_phone_verified, database_read_user_by_phone, database_check_alias_availability
from yelp.database_layer import database_update_user_registration


@app.route('/')
def index():
    return jsonify({'message' : 'Hello World 2'})


@app.route('/user/send_otp', methods=['POST'])
@expects(['phone_number'])
def send_user_otp(data):
    ''' send otp for verification '''

    phone_number = data['phone_number']
    _ = create(phone_number)
    
    otp, repeat = generate_otp(phone_number)
    if not repeat:
        print('sending an sms to: ' + phone_number + ' with an OTP: ' + otp)
    
    return jsonify(status='OK')



@app.route('/user/verify_otp', methods=['POST'])
@expects(['phone_number', 'otp'])
def verify_user_otp(data):
    ''' verification route for user '''

    phone_number = data['phone_number']
    otp = data['otp']
     
    response_code = verify_otp(phone_number, otp)
    if response_code != 200:
        if response_code == 401:
            raise InvalidUsage(message='Wrong OTP sent.', status_code=response_code)
        raise InvalidUsage(message='This OTP has expired', status_code=response_code)
    
    user = database_read_user_by_phone(phone_number)
    if not user:
        raise InvalidUsage(message='Invalid user.', status_code=401)

    if user.get('phone_verified') == False:
        database_update_user_phone_verified(user)

    return jsonify(status='OK')



@app.route('/user/signup', methods=['POST'])
@expects(['phone_number', 'first_name', 'last_name', 'alias'])
def user_signup(data):
    ''' updates user information '''

    first_name = data['first_name']
    last_name = data['last_name']
    alias = data['alias']
    phone_number = data['phone_number']
    
    if database_check_alias_availability(alias):
        return InvalidUsage(message='Alias taken', status_code=452)


    user = database_update_user_registration(phone_number, first_name.title(), last_name.title(), alias, current_time())
    
    if user:
        return jsonify(status='OK')

    raise InvalidUsage(message='Cannot signup', status_code=452)
