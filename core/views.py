from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from core import forms as core_forms
from core import models as core_models
from django.contrib import messages


class HomeView(views.TemplateView):
    template_name = "core/home.html"


class AboutView(views.TemplateView):
    template_name = "core/about.html"


# feedback createview
def feedback_createview(request):
    template_name = "core/feedback_create.html"
    form_class = core_forms.FeedbackForm
    success_url = reverse_lazy("core:home")

    if request.method == "GET":
        context = {"form": core_forms.FeedbackForm()}
        return render(request, template_name, context)

    elif request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            # fields = form.cleaned_data
            # feedback = FeedbackModel.objects.create(**fields)
            form.save()
            return redirect(success_url)
        return render(request, template_name, {"form": form})


# feedback listview
def feedback_listview(request):
    template_name = "core/feedback_list.html"
    model = core_models.FeedbackModel

    if request.method == "GET":
        feedbacks = model.objects.all()
        context = {"feedbacks": feedbacks}
    return render(request, template_name, context)


# bookservice view
class BookServiceView(LoginRequiredMixin, views.CreateView):
    template_name = "core/service.html"
    form_class = core_forms.ServiceForm
    success_url = reverse_lazy("core:payment")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request,"succesfully submitted")
        return super().form_valid(form)


# payment view
class PaymentView(views.TemplateView):
    template_name = "core/payment.html"
