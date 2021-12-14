import os
from twilio.rest import Client


account_sid = "AC9ab0eaa0a832e1e000e2b02c59bfa3a2"
auth_token = "3e30137d779ab4d7da9fd7a54681b56d"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

print(message.sid)