from django.urls import include, path
from . import views
app_name = "gym_user"
urlpatterns = [
    path('', views.userhome, name='userhome'),
    
    path('feedback', views.feedback, name='feedback'),
    path('viewroutine', views.viewroutine, name='viewroutine'),
    path('viewdiet', views.viewdiet, name='viewdiet'),
    path('viewplan', views.viewplan, name='viewplan'),
    path('viewmachinery', views.viewmachinery, name='viewmachinery'),
    path('workoutsummary/<int:id>', views.workoutsummary, name='workoutsummary'),
    path('healthstatus', views.healthstatus, name='healthstatus'),
    path('routineplan', views.routineplan, name='routineplan'),
    
]