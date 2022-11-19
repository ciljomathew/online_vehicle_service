import razorpay
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.http import HttpResponse

from core import forms as core_forms
from core import models as core_models
from django.conf import settings
import core.payment as payment
from core.models import payment


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

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "succesfully submitted")
        return super().form_valid(form)

    def get_success_url(self):
        service = self.object
        url = reverse_lazy("core:checkout", kwargs={"pk": service.id})
        return url


# Checkout view
class CheckoutView(views.DetailView):
    template_name = "core/checkout.html"
    model = core_models.ServiceModel
    context_object_name = "service"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        amount = self.object.cost
        context["form"] = core_forms.PaymentForm(initial={"amount": amount})
        return context


# Payment View
class PaymentView(views.View):
    template_name = "core/payment.html"

    success_url = ""

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        service = core_models.ServiceModel.objects.get(id=pk)
        context = {"service": service}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = core_forms.PaymentForm(request.POST)
        return render(request, self.template_name)


class ServiceView(views.ListView):
    template_name = "core/Payment.html"
    model = core_models.ServiceModel
    context_object_name = "services"


class PaymentView(views.View):
    def get(self, request):

        client = razorpay.Client(
            auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
        )
        payment = client.order.create(  # type: ignore
            {"amount": 10000, "currency": "INR", "payment_capture": "1"}
        )


def payment(request):
    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
    )
    payment = client.order.create(  # type: ignore
        {"amount": 10000, "currency": "INR", "payment_capture": "1"}
    )
    print(payment)
    return HttpResponse(f"Success {payment}")



# ================================================ #
# Payment Realated views                           #
# ================================================ #
# Payment view
class PaymentView(LoginRequiredMixin, views.View):
    template_name = "core/pay.html"

    def get(self, request):
        context = {
            "razorpay_order_id": order.id,
            "razorpay_merchant_key": settings.RAZORPAY_KEY_ID,
            "razorpay_amount": order.amount,
            "razorpay_currency": order.currency,
            "razorpay_callback_url": reverse_lazy("core:payment_handler"),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get("razorpay_payment_id", "")
            razorpay_order_id = request.POST.get("razorpay_order_id", "")
            signature = request.POST.get("razorpay_signature", "")
            params_dict = {
                "razorpay_order_id": razorpay_order_id,
                "razorpay_payment_id": payment_id,
                "razorpay_signature": signature,
            }

            order = Order.objects.filter(id=razorpay_order_id).last()

            # verify the payment signature.
            result = RAZORPAY_CLIENT.utility.verify_payment_signature(params_dict)
            if result is not None:
                amount = order.amount
                try:

                    # capture the payment
                    RAZORPAY_CLIENT.payment.capture(payment_id, amount)

                    Payment.objects.create(
                        id=payment_id,
                        order=order,
                        status=Payment.PaymentStatusChoices.completed,
                        mode="",
                    )

                    # render success page on successful caputre of payment
                    return render(request, "core/paymentsuccess.html")
                except:

                    # if there is an error while capturing payment.
                    return render(request, "core/paymentfail.html")
            else:

                # if signature verification fails.
                return render(request, "core/paymentfail.html")
        except:

            # if we don't find the required parameters in POST data
            return redirect(reverse_lazy("core:payment_handler"))

        
        # Payment List view
class PaymentListView(LoginRequiredMixin, views.ListView):
    template_name = "core/payment_list.html"
    model = Payment
    context_object_name = "payments"

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs = qs.filter(order__cart__user=user)
        return qs
