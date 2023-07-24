
from django.urls import include, path
from . import views
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
app_name = "gym_admin"
urlpatterns = [
    path('', views.adminhome, name='adminhome'),
    path('traineeregistration', views.traineeregistration, name='traineeregistration'),
    path('plann', views.plann, name='plann'),
    path('viewalluserregistration/<int:id>', views.viewalluserregistration, name='viewalluserregistration'),
    path('viewregister', views.viewregister, name='viewregister'),
    path('addclass', views.addclass, name='addclass'),
    path('viewcreatedplan', views.viewcreatedplan, name='viewcreatedplan'),
    path('addworkoutsummary/<int:id>', views.addworkoutsummary, name='addworkoutsummary'),
    path('addmachinery', views.addmachinery, name='addmachinery'),
    path('viewfeedback', views.viewfeedback, name='viewfeedback'),
    path('viewtrainee', views.viewtrainee, name='viewtrainee'),
    path('traineeviewall', views.traineeviewall, name='traineeviewall'),
    path('addhealthstatus', views.addhealthstatus, name='addhealthstatus'),
    path('viewallcreatedplans/<int:id>', views.viewallcreatedplans, name='viewallcreatedplans'),
    path('adminviewmachinery', views.adminviewmachinery, name='adminviewmachinery'),
    
] 