"""Views for User API"""

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import authentication, permissions



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


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user

class CustomAuthTokenView(ObtainAuthToken):
    """Create a new auth token for user."""

    serializer_class = CustomAuthtokenSerializer
    render_classes = api_settings.DEFAULT_RENDERER_CLASSES
