import requests

from django.test import TestCase, Client
from rest_framework import status
from django.conf import settings
from django.urls import reverse

client = Client()


def get_jwt_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = f"client_id={settings.CLIENT_ID}&username={settings.USERNAME_TEST}&password={settings.PASSWORD_TEST}&grant_type=password"

    r = requests.post(headers=headers, data=data, url=settings.KEYCLOAK_TOKEN_URL)
    return r.json()["access_token"]


class AuthentificationTestCase(TestCase):
    def test_user_send_unauthenticated_request(self):
        """
        Test that a request is not executed if the JWT is not valid
        :return:
        """
        response = client.get(reverse("instantMessages:test"))
        self.assertIs(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_send_authenticated_request(self):
        """
        Test that a request is executed if the JWT is valid
        :return:
        """
        token = get_jwt_token()
        headers = {'Authorization': f'Bearer {token}'}

        response = client.get(reverse("instantMessages:test"), headers=headers)
        self.assertIs(response.status_code, status.HTTP_200_OK)


