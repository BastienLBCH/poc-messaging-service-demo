from django.test import TestCase, Client
from rest_framework import status
from django.conf import settings
from django.urls import reverse
import json


import requests

client = Client()


def get_jwt_token():
    """
    Get a valid JWT token from keycloak
    :return:
    """
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = f"client_id={settings.CLIENT_ID}&username={settings.USERNAME_TEST}&password={settings.PASSWORD_TEST}&grant_type=password"

    r = requests.post(headers=headers, data=data, url=settings.KEYCLOAK_TOKEN_URL)
    return r.json()["access_token"]


class SendMessageTestCase(TestCase):
    def setUp(self):
        # Get JWT
        self.token = get_jwt_token()

        # Create a conversation for testing
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        body = {
            "name": "conversation_test"
        }
        r = client.post(reverse("instantMessages:createconversations"), body, headers=headers)
        self.conversation_id = json.loads(r.content.decode())["id"]

    def test_user_send_message_to_conversation(self):
        """
        Test user add a valid participant to a valid conversation
        :return:
        """

        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        body = {
            "conversation_id": self.conversation_id,
            "message_content": "Salut les copains"
        }
        r = client.post(
            reverse("instantMessages:sendmessage", kwargs={'conversation_id': self.conversation_id}),
            body,
            headers=headers
        )

        self.assertIs(r.status_code, status.HTTP_201_CREATED)

    def test_user_send_message_to_conversation_with_missing_field(self):
        """
        Test user add a valid participant to a valid conversation
        :return:
        """

        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        body = {}
        r = client.post(
            reverse("instantMessages:sendmessage", kwargs={'conversation_id': self.conversation_id}),
            body,
            headers=headers
        )

        self.assertIs(r.status_code, status.HTTP_400_BAD_REQUEST)
