import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_url = "https://api.pushover.net/1/messages.json"

def send_pushover_notification(message):
    payload = {
        "user": pushover_user,
        "token": pushover_token,
        "message": message
    }
    response = requests.post(pushover_url, data=payload)
    print(response.text)
    return response.status_code == 200
