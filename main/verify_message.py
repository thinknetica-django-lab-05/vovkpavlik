import os
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()


def send_verify_code():
    account_sid = os.getenv("ACCOUNT_SID_TWILIO")
    auth_token = os.environ['AUTH_TOKEN_TWILIO']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="2165",
        from_='+15156051635',
        to='+79788432861'
    )

    return message.sid
