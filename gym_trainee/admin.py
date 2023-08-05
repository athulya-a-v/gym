from django.contrib import admin
from .models import  UserHealthStatus, UserAttendance, UploadRoutine

# Register your models here.

admin.site.register(UserHealthStatus)
admin.site.register(UserAttendance)
admin.site.register(UploadRoutine)
