"""Views for User API"""

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model

from .serializers import UserSerializer, UserCreateSerializer


class UserApiView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serialized_data = UserCreateSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)

        new_user = get_user_model().objects.create_user(
            **serialized_data.validated_data
        )
        serialized_data = UserSerializer(new_user)

        return Response(data={**serialized_data.data}, status=status.HTTP_201_CREATED)
