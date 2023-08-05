from django.db import models
from fitness.models import Register

# Create your models here.


class UserHealthStatus(models.Model):
    user_fk = models.ForeignKey(Register, on_delete=models.CASCADE)
    user_healthstatus = models.CharField(max_length=100, default="")
    uploading_date = models.DateField()

class UserAttendance(models.Model):
    user_fk = models.ForeignKey(Register, on_delete=models.CASCADE)
    attendance = models.CharField(max_length=10, default="absent")
    timestamp = models.DateTimeField(auto_now_add=True)

class UploadRoutine(models.Model):
    excercise_type = models.CharField(max_length=50, default="")
    day_1 = models.CharField(max_length=50, default="")
    day_2 = models.CharField(max_length=50, default="")
    day_3 = models.CharField(max_length=50, default="")
    day_4 = models.CharField(max_length=50, default="")
    day_5 = models.CharField(max_length=50, default="")
    day_6 = models.CharField(max_length=50, default="")
    day_7 = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.name

class FitnessDietPlan(models.Model):
    user_fk = models.ForeignKey(Register, on_delete=models.CASCADE)
    food_to_add = models.JSONField(blank=True, default=list)
    food_to_avoid =  models.JSONField(blank=True, default=list)
    pre_workout_food =  models.JSONField(blank=True, default=list)
    post_workout_food =  models.JSONField(blank=True, default=list)

    class Meta():
        db_table = 'fitnessdietplan'
