"""
Urls for user app.
"""

from django.urls import path


from .views import CustomAuthTokenView, UserApiView, ManageUserApiView


app_name = "user"

urlpatterns = [
    path("create", UserApiView.as_view(), name="create"),
    path("token", CustomAuthTokenView.as_view(), name="token"),
    path("me", ManageUserApiView.as_view(), name="me"),
]
