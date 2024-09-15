"""
Serializers for users app.
"""

from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework import status

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


class UserSerializer(ModelSerializer):
    """
    Serialzier for creating user object.
    """

    class Meta:
        model = get_user_model()
        fields = ("email", "password", "name")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 5,
            }
        }

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class CustomAuthtokenSerializer(Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        trim_whitespace=False,
        style={"input_style": "password"},
    )

    def validate(self, attrs):
        email = attrs.get("email", None)
        password = attrs.get("password", None)

        if email is None or password is None:
            raise ValidationError(
                detail=_("Email or password cannot be empty!"),
                code=status.HTTP_400_BAD_REQUEST,
            )
        user = authenticate(
            request=self.context.get("request"), email=email, password=password
        )
        if not user:
            raise AuthenticationFailed(
                detail=_("No user found!"),
                code=status.HTTP_400_BAD_REQUEST,
            )
        attrs["user"] = user
        return attrs
