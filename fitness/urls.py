from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginn, name='login'),
    path('register', views.register, name='register'),
    path('attend', views.attend, name='attend'),
    path('machinery', views.machinery, name='machinery'),
    path('plan', views.plan, name='plan'),
    path('userhome', views.userhome, name='userhome'),
    path('feedback', views.feedback, name='feedback'),
    path('viewdiet', views.viewdiet, name='viewdiet'),
    path('viewclass', views.viewclass, name='viewclass'),
    path('viewplan', views.viewplan, name='viewplan'),
     path('diet', views.diet, name='diet'),




]