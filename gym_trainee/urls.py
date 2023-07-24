from django.urls import path
from . import views

app_name = "gym_trainee"
urlpatterns = [
    path('', views.traineehome, name='traineehome'),
    path('traineeform/<int:id>', views.traineeform, name='traineeform'),
     path('uploadhealthstatus/<int:id>', views.uploadhealthstatus, name='uploadhealthstatus'),
     path('uploaddiet', views.uploaddiet, name='uploaddiet'),
]