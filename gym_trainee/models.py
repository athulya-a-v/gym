from django.db import models

# Create your models here.
class TraineeRegister(models.Model):
    trainee_addrress = models.TextField()
    trainee_pincode = models.BigIntegerField()
    trainee_state = models.CharField(max_length=30, default="")
    trainee_city = models.CharField(max_length=30, default="")
    trainee_gender = models.CharField(max_length=8, default="")
    trainee_dob = models.DateField()
    register_phone=models.BigIntegerField()

class UserHealthStatus(models.Model):
    user_healthstatus = models.CharField(max_length=100, default="")
    uploading_date = models.DateField()

