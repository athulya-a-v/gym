from django.contrib import admin
from .models import CreatePlan, CreatePassword, AddMachineryDetails

# Register your models here.
admin.site.register(CreatePlan)
admin.site.register(CreatePassword)
admin.site.register(AddMachineryDetails)
