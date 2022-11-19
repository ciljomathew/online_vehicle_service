from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from user import models

USER = get_user_model()

# User Registration Form
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = USER
        fields = ["email", "username"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.ProfileModel
        exclude = ("status", "address", "user")
