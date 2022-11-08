from core import views
from django.urls import path

from user import views

app_name = "user"

urlpatterns = [
    path("signup/", views.UserCreateView.as_view(), name="user_signup"),
    path("login/", views.UserLoginView.as_view(), name="user_login"),
    path("logout/", views.UserLogoutView.as_view(), name="user_logout"),
]
