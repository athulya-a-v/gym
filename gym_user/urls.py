from django.urls import include, path
from . import views
app_name = "gym_user"
urlpatterns = [
    path('', views.userhome, name='userhome'),
    path('feedback', views.feedback, name='feedback'),
    path('viewclass', views.viewclass, name='viewclass'),
    path('viewdiet', views.viewdiet, name='viewdiet'),
    path('viewplan', views.viewplan, name='viewplan'),
    path('viewmachinery', views.viewmachinery, name='viewmachinery'),
    path('workoutsummary/<int:id>', views.workoutsummary, name='workoutsummary'),
    
]