from django.db import models

# Create your models here.
class EnterFeedback(models.Model):
    f_name = models.CharField(max_length=25)
    f_mail = models.CharField(max_length=25)
    f_feedback = models.CharField(max_length=100)
