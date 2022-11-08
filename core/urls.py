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
    path("payment/",views.PaymentView.as_view(),name="payment"),


]