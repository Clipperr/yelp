# --- core python imports
import uuid

# python imports
from flask import jsonify, request

# app imports
from yelp import app
from yelp.auth import expects
from yelp.utils import posted, generate_otp
from yelp.users import create

@app.route('/')
def index():
    return jsonify({'message' : 'Hello World 2'})


@app.route('/user/send_otp', methods=['POST'])
@expects(['phone_number'])
def send_user_otp(data):
    ''' send otp for verification '''

    phone_number = data['phone_number']
    
    otp, repeat = generate_otp(phone_number)
    if not repeat:
        print('sending an sms to: ' + phone_number + ' with an OTP: ' + otp)
    
    _ = create(phone_number)
    return jsonify(status='OK')



@app.route('/user/verify_otp', methods=['POST'])
@expects(['phone_number', 'otp'])
def verify_user_otp(data):
    ''' verification route for user '''

    phone_number = data['phone_number']
    
    # verification
    # mark user phone_verified

    return ''


#@app.route('/user/signup', methods=['POST'])
#@expects(['first_name', 'last_name', 'alias', 'phone_number'])
#def signup(data):
#    ''' registers a user to the system '''
#
#    data = posted()
#    first_name = data['first_name']
#    last_name = data['last_name']
#    alias = data['alias']
#    phone_number = data['phone_number']
#
#    if database_read_user_by_alias(alias):
#        pass #raise error
#
#    user = database_create_user(first_name, last_name, alias, phone_number)
#
#    return jsonify(status='OK')
