#!/usr/bin/env python3

from twilio.rest import Client

account_sid = 'YOUR_ID'
auth_token = 'YOUR_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+YOUR_NUMBER',
  body='Hello from Twilio',
  to='+TO_NUMBER'
)

print(message.sid)
