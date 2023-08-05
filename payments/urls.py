from django.urls import path
from . import views
from payments.views import  PaymentPageView



urlpatterns = [
   path('payment', PaymentPageView.as_view(), name="Payment-Page"),
    
    
    path('charge', views.charge, name="charge"),
     path('error', views.error, name="error"),
]