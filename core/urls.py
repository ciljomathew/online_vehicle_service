from django.urls import path
from core import views
app_name= "core"
urlpatterns= [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),

    #feedback
    path("feedback/create", views.feedback_createview, name="feedback_create"),
    path("feedback/list/",views.feedback_listview, name="feedback_list"),
    # service booking
    path("service/",views.BookServiceView.as_view(),name="book_service"),
    # payment
    path("service/<int:pk>/checkout/",views.CheckoutView.as_view(),name="checkout"),
    path("service/<int:pk>/payment/",views.PaymentView.as_view(),name="payment"),
    path("service/<int:pk>/payment/completed/",views.PaymentCompletedView.as_view(),name="payment_completed"),
    # Payment
    path("payment/list/", views.PaymentListView.as_view(), name="payment_list"),


]