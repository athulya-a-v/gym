from django.shortcuts import render, redirect
from django.template import Template, Context
from . models import Register
from fitness.models import *
from gym_admin.models import CreatePlan

# Create your views here.


def home(request):
    return render(request, 'fitness/home.html')


def login(request):
     msg = ''
     if request.method == 'POST':
          log_username=request.POST['login_name']
          log_password=request.POST['login_userpassword']
          log_usertype=request.POST['usertype']

          user_exist = Register.objects.filter(register_email=log_username, register_password=log_password ).exists()

          if user_exist:
              user_detail = Register.objects.get(register_email=log_username, register_password=log_password)
              request.session['user_id'] = user_detail.id
              return redirect("gym_user:userhome")
          else:
              msg = 'invalid email or password'
              return render(request, 'fitness/login.html', {'err_msg': msg,})



     return render(request, 'fitness/login.html', {'err_msg': msg, })


def register(request):
     plans = CreatePlan.objects.all()
     msg = ''
     if request.method == 'POST':
          reg_firstname = request.POST['regname1']
          reg_secondname = request.POST['regname2']
          reg_username = request.POST['regusername']
          reg_email = request.POST['regemail']
          reg_password = request.POST['password1']
          reg_password2 = request.POST['password2']
          reg_address = request.POST['regaddress']
          reg_pin = request.POST['regpin']
          reg_state = request.POST['regstate']
          reg_city = request.POST['regcity']
          reg_gender = request.POST['gender']
          reg_dob = request.POST['regdob']
          reg_phone = request.POST['regphone']
          user_bloodgroup = request.POST['bloodgroup']
          u_height = request.POST['userheight']
          u_weight = request.POST['userweight']

          username_exist = Register.objects.filter(register_username=reg_username)
          email_exist = Register.objects.filter(register_email=reg_email)
          user_type='usertype'

        
          if username_exist:
               msg = "Username already exist"
          elif email_exist:
               msg = "Email already exist"
          else:
               register = Register(register_fname=reg_firstname, register_lname=reg_secondname,register_username=reg_username,register_email=reg_email, register_password=reg_password, register_address=reg_address,
                         register_pin=reg_pin, register_state=reg_state, register_city=reg_city, register_gender=reg_gender, register_dob=reg_dob, register_phone=reg_phone, user_type=user_type, blood_group=user_bloodgroup, user_height=u_height, user_weight=u_weight)
               register.save()
               print("saved")
               return redirect('fitness:login')
     return render(request, 'fitness/register.html', {'msg': msg, 'plans':plans,})
def payment(request):
    return render(request, 'fitness/payment.html')
