"""
Serializers for users app.
"""

from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):
    """
    Serialzier for user object.
    """

    class Meta:
        model = get_user_model()
        fields = ("email", "name")

class UserCreateSerializer(ModelSerializer):
    """
    Serialzier for creating user object.
    """

    class Meta:
        model = get_user_model()
        fields = ("email", "password", "name")
        extra_kwargs = {
            "password": {
                "min_length": 5,
            }
        }
