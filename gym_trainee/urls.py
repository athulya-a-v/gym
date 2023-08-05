from django.urls import path
from . import views

app_name = "gym_trainee"
urlpatterns = [
    path('', views.traineehome, name='traineehome'),
    path('traineeform/<int:id>', views.traineeform, name='traineeform'),
     path('uploadhealthstatus/<int:id>', views.uploadhealthstatus, name='uploadhealthstatus'),
     path('uploadroutine', views.uploadroutine, name='uploadroutine'),
     path('traineeviewuserregister', views.traineeviewuserregister, name='traineeviewuserregister'),
     path('markattendance', views.markattendance, name='markattendance'),
     path('dietplan/<int:id>', views.dietplan, name='dietplan'),
]