
from django.urls import include, path
from . import views
app_name = "gym_admin"
urlpatterns = [
    path('', views.adminhome, name='adminhome'),
    path('traineeregistration', views.traineeregistration, name='traineeregistration'),
    path('diet', views.diet, name='diet'),
    path('plann', views.plann, name='plann'),
    path('seemore/<int:id>', views.seemore, name='seemore'),
    path('viewregister', views.viewregister, name='viewregister'),
    path('addclass', views.addclass, name='addclass'),
    path('adminviewplan', views.adminviewplan, name='adminviewplan'),
    path('workoutsummary/<int:id>', views.workoutsummary, name='workoutsummary'),
    path('addmachinery', views.addmachinery, name='addmachinery'),
    path('viewfeedback', views.viewfeedback, name='viewfeedback'),
    path('viewtrainee', views.viewtrainee, name='viewtrainee'),
    path('traineeviewall', views.traineeviewall, name='traineeviewall'),
    path('addhealthstatus', views.addhealthstatus, name='addhealthstatus'),
    
]