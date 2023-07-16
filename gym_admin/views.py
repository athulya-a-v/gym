from django.shortcuts import render, redirect
from fitness.models import *
from . models import CreatePlan, CreatePassword
from gym_user.models import EnterFeedback
from gym_trainee.models import TraineeRegister
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def adminhome(request):
    return render(request,'adminhome.html/')
def traineeregistration(request):
    msg = ''
    if request.method == 'POST':
     t_fname = request.POST['tfname']
     t_lname = request.POST['tlname']
     t_username = request.POST['tusername']
     t_password = request.POST['tpassword']
     t_mail = request.POST['temail']
     user_exist = CreatePassword.objects.filter(trainne_password = t_password)
     username_exist = CreatePassword.objects.filter(trainee_username = t_username)
     email_exist = CreatePassword.objects.filter(trainee_mail= t_mail)
     if user_exist:
         msg = 'password already exist'
     elif username_exist:
         msg = 'username already exist'
     elif email_exist:
         msg = 'email already exist'
     else:
         register= CreatePassword(trainee_firstname=t_fname, trainee_lastname=t_lname, trainne_password=t_password, trainee_username=t_username, trainee_mail=t_mail)
         subject = "Fitness Club Trainee Registration"
         message = f"Hi {t_fname}, \n\n your Fitness Club login credentials is, \n\nUsername : {t_username}, \n\npassword : {t_password}"
         email_from = settings.EMAIL_HOST_USER
         email_to = [t_mail]
         send_mail(subject, message, email_from, email_to)

         register.save()
         print("saved")
         msg = "Trainee Registration Successfull"
         return render(request,"gym_admin/traineeregistration.html", {"msg":msg})

    return render(request,'gym_admin/traineeregistration.html/')
def diet(request):
    return render(request,'diet.html/')
def plann(request):
    msg = ''
    if request.method == 'POST':
     p_name = request.POST['planname']
     p_description = request.POST['plandescription']
     p_validity = request.POST['planvalidity']
     p_amount = request.POST['planamount']
     w_type = request.POST['workouttype']
     day_week = request.POST['daysperweek']
     time_workout = request.POST['timeperworkout']
     equip_required = request.POST['equipmentrequired']
     t_gender = request.POST['targetgender']


     user_exist = CreatePlan.objects.filter(plan_name=p_name, plan_validity=p_validity)

     if user_exist:
         msg = "Plan already exist"
     else:
        register = CreatePlan(plan_name = p_name, plan_description = p_description, plan_validity = p_validity, plan_amount = p_amount, workout_type=w_type, days_per_week=day_week, time_per_workout=time_workout, equipment_required=equip_required, target_gender=t_gender)
        register.save()
        print('saved')
        return redirect('gym_admin:plann')

    return render(request,'plann.html/')
def seemore(request, id):
    user = Register.objects.get(id=id)

    return render(request,'seemore.html/',{"user":user})
def viewregister(request):

    query = Register.objects.all()

    return render(request,'viewregister.html/', {"query":query})

def adminviewplan(request):
    ad_viewplan = CreatePlan.objects.all()

    return render(request,'adminviewplan.html/', {"ad_viewplan": ad_viewplan})
def addclass(request):
    return render(request,'addclass.html/')
def workoutsummary(request):
   
    return render(request,'workoutsummary.html/')
def addmachinery(request):
    return render(request,'addmachinery.html/')
def viewfeedback(request):
    v_feedback = EnterFeedback.objects.all()
    return render(request,'viewfeedback.html/', {"v_feedback":v_feedback})
def viewtrainee(request):
    traineeview = CreatePassword.objects.all()
    return render(request,'viewtrainee.html/', {'traineeview':traineeview})
def traineeviewall(request):
    return render(request,'traineeviewall.html/')
def addhealthstatus(request):
    return render(request,'addhealthstatus.html/')