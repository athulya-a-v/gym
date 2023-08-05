from django.contrib import admin
from .models import CreatePlan, TraineeRegister, AddMachineryDetails

# Register your models here.
admin.site.register(CreatePlan)
admin.site.register(TraineeRegister)
admin.site.register(AddMachineryDetails)
