from django.db import models

# Create your models here.
class CreatePlan(models.Model):
    plan_name = models.CharField(max_length=100)
    plan_description = models.TextField()
    plan_validity = models.CharField(max_length=100)
    plan_amount = models.BigIntegerField()
    workout_type = models.CharField(max_length=50)
    days_per_week = models.CharField(max_length=25)
    time_per_workout = models.CharField(max_length=25)
    equipment_required = models.CharField(max_length=50)
    target_gender = models.CharField(max_length=7)

class CreatePassword(models.Model):
    trainee_firstname = models.CharField(max_length=50, default="")
    trainee_lastname = models.CharField(max_length=20, default="")
    trainee_username = models.CharField(max_length=20, default="")
    trainee_mail = models.CharField(max_length=50, default="")
    trainne_password = models.CharField(max_length=8, default="")





    