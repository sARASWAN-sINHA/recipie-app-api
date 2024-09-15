"""
Urls for user app.
"""

from django.urls import path


from .views import CustomAuthTokenView, UserApiView, ManageUserView


app_name = "user"

urlpatterns = [
    path("create", UserApiView.as_view(), name="create"),
    path("token", CustomAuthTokenView.as_view(), name="token"),
    path("me", ManageUserView.as_view(), name="me"),
]
