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


class PaymentForm(forms.Form):
    PAYMENT_CHOICES = (("UPI", "UPI"), ("NETBANK", "Net Banking"))
    amount = forms.DecimalField(
        min_value=1, widget=forms.NumberInput(attrs={"readonly": "true"})
    )
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES)
