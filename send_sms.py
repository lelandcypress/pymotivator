from motivator import *

# Downloom ad the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def dialer(message_text):
    account_sid = 
    auth_token = 
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=message_text,
            from_='+15137902745',
            to='+18432594904'
        )

    print(message.sid)


dialer(message_to_self)
