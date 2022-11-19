from django.contrib.auth import authenticate
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from user.forms import UserRegisterForm
from user.forms import ProfileForm
from user import models as user_models

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


# ================= Profile View Start ===============================#


class ProfileCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = "core/profile_create.html"
    model = user_models.ProfileModel
    form_class = ProfileForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# profile updateview
class ProfileUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = "core/profile_update.html"
    model = user_models.ProfileModel
    form_class = ProfileForm
    success_url = reverse_lazy("user:profile_detail")


class ProfileDetailView(auth_mixins.LoginRequiredMixin, views.DetailView):
    template_name = "core/profile.html"
    model = user_models.ProfileModel
    context_object_name = "profile"


# ================= Profile View end ===============================#
