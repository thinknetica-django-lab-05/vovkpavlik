# import os
# from dotenv import load_dotenv
# from twilio.rest import Client
#
# load_dotenv()
#
#
# account_sid = os.getenv("ACCOUNT_SID_TWILIO")
# auth_token = os.environ['AUTH_TOKEN_TWILIO']
# client = Client(account_sid, auth_token)
#
# message = client.messages \
#                 .create(
#                      body="2165",
#                      from_='+15156051635',
#                      to='+79788432861'
#                  )
#
# print(message.sid)
import random

def get_random_code():
    random_code = random.randint(1000, 9999)
    return str(random_code)


print(type(get_random_code()))
