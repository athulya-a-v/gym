from django.urls import path
from . import views

app_name = "fitness"
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('payment', views.payment, name='payment'),
   
] 

