from django import forms

from core import models


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.FeedbackModel
        exclude = ("status",)


class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.ServiceModel
        fields = ["type", "vehicle", "date"]
