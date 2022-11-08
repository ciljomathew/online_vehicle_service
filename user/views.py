from django.contrib.auth import authenticate
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from user.forms import UserRegisterForm

USER = get_user_model()

# UserCreateView
class UserCreateView(views.CreateView):
    template_name = "registration/signup.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("user:user_login")


class UserLoginView(views.View):
    form_class = auth_forms.AuthenticationForm
    success_url = reverse_lazy("core:home")
    template_name = "registration/login.html"

    def get(self, request):
        context = {
            "form": self.form_class(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request=request)
        # if form.is_valid():
        form.is_valid()
        username = request.POST.get("username")
        password = request.POST.get("password")
        # to check whether the given username and password are exists or not
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # to login user
            login(request, user)
            print("USER is valid.............LOGGED IN")
            return redirect(self.success_url)
        print("USER is not valid.............")
        print("FORM is not valid.............")

        context = {"form": form}
        return render(request, self.template_name, context)


class UserLogoutView(views.View):
    template_name = "registration/logged_out.html"

    def get(self, request):
        logout(request)
        return render(request, self.template_name)
