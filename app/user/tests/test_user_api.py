from rest_framework.test import APIClient

"""
Tests for user apis.
"""


from rest_framework import status

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


USER_CREATE_URL = reverse("user:create")


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTest(TestCase):
    """
    Test the public features of user API.
    """

    def setUp(self) -> None:
        self.client = APIClient()

    def test_user_created_successfully(self):
        payload = {
            "email": "test123@gmail.com",
            "password": "test12345",
            "name": "SRS1206",
        }

        result = self.client.post(USER_CREATE_URL, data=payload)
        user = get_user_model().objects.get(email=payload.get("email"))

        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(payload.get("email"), user.email)
        self.assertTrue(user.check_password(payload.get("password")))
        self.assertNotIn(payload.get("password"), result)

    def test_user_already_exists(self):
        payload = {
            "email": "test123@gmail.com",
            "password": "test12345",
            "name": "SRS1206",
        }

        create_user(**payload)
        result = self.client.post(USER_CREATE_URL, data=payload)

        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_smaller_than_five_characters(self):
        payload = {
            "email": "test123@gmail.com",
            "password": "test",
            "name": "SRS1206",
        }
        result = self.client.post(USER_CREATE_URL, data=payload)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(
            get_user_model().objects.filter(email=payload.get("email")).exists()
        )
