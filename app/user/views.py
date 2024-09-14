"""Views for User API"""

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


from django.contrib.auth import get_user_model

from .serializers import CustomAuthtokenSerializer, UserSerializer


class UserApiView(generics.GenericAPIView):
    """Create a new user in the system."""

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(data=request.data)
        serialized_data.is_valid(raise_exception=True)

        new_user = get_user_model().objects.create_user(
            **serialized_data.validated_data
        )
        serialized_data = self.serializer_class(new_user)

        return Response(data=serialized_data.data, status=status.HTTP_201_CREATED)


class ManageUserApiView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class CustomAuthTokenView(ObtainAuthToken):
    """Create a new auth token for user."""

    serializer_class = CustomAuthtokenSerializer
    render_classes = api_settings.DEFAULT_RENDERER_CLASSES
