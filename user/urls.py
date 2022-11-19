from core import views
from django.urls import path

from user import views

app_name = "user"

urlpatterns = [
    path("signup/", views.UserCreateView.as_view(), name="user_signup"),
    path("login/", views.UserLoginView.as_view(), name="user_login"),
    path("logout/", views.UserLogoutView.as_view(), name="user_logout"),
       # profile
    path("profile/create", views.ProfileCreateView.as_view(), name="profile_create"),
    path("profile/<int:pk>/detail", views.ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/<int:pk>/update/",views.ProfileUpdateView.as_view(),name="profile_update"), 
    
]
