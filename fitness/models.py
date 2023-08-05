from django.db import models

# Create your models here.


#class MachDetail(models.Model):
    #mach_name=models.CharField(max_length=100)
    #mach_description=models.TextField()
    #mach_image=models.ImageField(upload_to ='mechdetail')

class Register(models.Model):
    
    register_fname=models.CharField(max_length=100)
    register_lname=models.CharField(max_length=100)
    register_username=models.CharField(max_length=100)
    register_email=models.CharField(max_length=100)
    register_password=models.CharField(max_length=8)
    user_type=models.CharField(max_length=100)
    register_address=models.TextField()
    register_pin=models.BigIntegerField()
    register_state=models.CharField(max_length=100)
    register_city=models.CharField(max_length=100)
    register_gender=models.CharField(max_length=20)
    register_dob=models.DateField()
    register_phone=models.BigIntegerField()
    register_selectplan=models.CharField(max_length=100)
    blood_group = models.CharField(max_length=20, default="")
    user_height = models.CharField(max_length=25, default="")
    user_weight = models.CharField(max_length=25, default="")
    user_photo = models.ImageField(upload_to ='userphoto', default="")
    time_stamp = models.DateTimeField(auto_now_add=True)


    


    