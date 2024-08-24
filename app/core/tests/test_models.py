"""
Tests for models.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    """Test models."""

    def test_user_created_successfully(self):
        """
        Test to check that user is created successfully,
        upon providing valid user credentials.
        """

        email = "test@example.com"
        password = "test12345"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_without_email(self):
        """Test for creating user without email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email="", password="test123")

    def test_create_superuser(self):
        """Test to create a superuser"""
        superuser = get_user_model().objects.create_superuser(
            email="superuser@example.com", password="test123"
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
