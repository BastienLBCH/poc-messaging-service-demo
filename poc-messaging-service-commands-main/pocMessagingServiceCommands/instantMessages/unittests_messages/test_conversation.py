from django.test import TestCase, Client
from rest_framework import status
from django.conf import settings
from django.urls import reverse
import uuid
import json


import requests
import jwt

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


class CreateConversationTestCase(TestCase):
    def setUp(self):
        self.token = get_jwt_token()

    def test_authenticated_user_create_conversation(self):
        """
        Test that an authenticated user is able to create a conversation
        Expecting 201 created
        :return:
        """
        user_id = jwt.decode(self.token, options={"verify_signature": False})["sub"]
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        body = {
            "name": "conversation_test"
        }
        r = client.post(reverse("instantMessages:createconversations"), body, headers=headers)

        self.assertIs(r.status_code, status.HTTP_201_CREATED)

    def test_authenticated_user_create_conversation_with_missing_field(self):
        """
        Test user creates a conversation but fields are missing.
        expecting 400 bad request
        :return:
        """
        user_id = jwt.decode(self.token, options={"verify_signature": False})["sub"]

        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        body = {
        }

        r = client.post(reverse("instantMessages:createconversations"), body, headers=headers)

        self.assertIs(r.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteConversationTestCase(TestCase):
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

    def test_authenticated_user_delete_conversation(self):
        """
        Test that an authenticated user is able to create a conversation
        Expecting 201 created
        :return:
        """
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        body = {}
        r = client.delete(
            reverse(
                "instantMessages:deleteconversation",
                kwargs={'conversation_id': self.conversation_id}
            ),
            headers=headers
        )

        self.assertIs(r.status_code, status.HTTP_201_CREATED)


class AddParticipantTestCase(TestCase):
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

    def test_user_add_participant_to_conversation(self):
        """
        Test user add a valid participant to a valid conversation
        :return:
        """

        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        body = {
            "participant_id": "d8c2ec28-b43a-4259-99fa-924be1bf4ac0"
        }
        r = client.post(
            reverse(
                "instantMessages:addparticipant",
                kwargs={'conversation_id': self.conversation_id}
            ),
            body,
            headers=headers
        )

        self.assertIs(r.status_code, status.HTTP_201_CREATED)

    def test_user_add_participant_to_conversation_with_missing_field(self):
        """
        Test user add a valid participant to a valid conversation
        :return:
        """

        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        body = {}
        r = client.post(
            reverse(
                "instantMessages:addparticipant",
                kwargs={'conversation_id': self.conversation_id}
            ),
            body,
            headers=headers
        )

        self.assertIs(r.status_code, status.HTTP_400_BAD_REQUEST)


class RemoveParticipantTestCase(TestCase):
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

    def test_user_remove_participant_to_conversation(self):
        """
        Test user remove a valid participant to a valid conversation
        :return:
        """

        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        body = {
            "participant_id": "d8c2ec28-b43a-4259-99fa-924be1bf4ac0",
            "conversation_id": self.conversation_id
        }
        r = client.post(
            reverse(
                "instantMessages:removeparticipant",
                kwargs={
                    'conversation_id': self.conversation_id,
                    'participant_id': "d8c2ec28-b43a-4259-99fa-924be1bf4ac0"
                }
            ),
            body,
            headers=headers
        )

        self.assertIs(r.status_code, status.HTTP_201_CREATED)












