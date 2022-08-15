from motivator import *

# Downloom ad the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def dialer(message_text):
    account_sid = 'AC8ae0953d36eced92c7c5500ae87b757b'
    auth_token = '6c907b420ff737c7d00318c80a8d07e7'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=message_text,
            from_='+17629000264',
            to='+18432594904'
        )

    print(message.sid)
