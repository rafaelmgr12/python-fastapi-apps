import onesignal_sdk
import onesignal_sdk.client
from notifications.models import Notification
from dotenv import load_dotenv
import os

load_dotenv()


ONESIGNAL_APP_ID = os.getenv("ONESIGNAL_APP_ID")
ONESIGNAL_API_KEY = os.getenv("ONESIGNAL_API_KEY")


onesignal_client = onesignal_sdk.client.Client(app_id=ONESIGNAL_APP_ID, rest_api_key=ONESIGNAL_API_KEY)

def send_notification(notification: Notification):
    notification_body = {
        'headings': {'en': notification.title},
        'contents': {'en': notification.message},
        'include_player_ids': [notification.user_id]
    }

    response = onesignal_client.send_notification(notification_body)
    return response.status_code == 200