"""
Urls for user app.
"""

from django.urls import path


from .views import UserApiView


app_name = "user"

urlpatterns = [
    path("create", UserApiView.as_view(), name="create")
]
