from django.shortcuts import render,redirect
from gym_admin.models import CreatePassword
from gym_trainee.models import TraineeRegister, UserHealthStatus
from fitness.models import Register

# Create your views here.
def traineehome(request):
    return render(request, 'traineehome.html')
def traineeform(request, id):
     traineereg = CreatePassword.objects.get(id=id)
     msg=""
     if request.method == 'POST':
          t_address = request.POST['taddress']
          t_pincode = request.POST['tpincode']
          t_state = request.POST['tstate']
          t_city = request.POST['tcity']
          t_gender = request.POST['tgender']
          t_phone = request.POST['tphone']
          t_dob = request.POST['tdob']
          register = TraineeRegister(trainee_addrress=t_address, trainee_pincode=t_pincode, trainee_state=t_state, trainee_city=t_city, trainee_dob=t_dob, register_phone=t_phone, trainee_gender=t_gender)
          register.save()
          print('saved')
          return redirect('gym_trainee:traineehome')
          
     return render(request, 'traineeform.html', {"traineereg":traineereg})
def uploadhealthstatus(request, id):
    user_status = Register.objects.get(id=id)
    if request.method == 'POST':
     user_health_status = request.POST['healthstatus']
     register = UserHealthStatus(user_healthstatus=user_health_status)
     register.save()
     print('saved')
     return redirect('gym_trainee:traineehome')
    return render(request, 'uploadhealthstatus.html', {"user_status":user_status})
def uploaddiet(request):
    return render(request,'uploaddiet.html')
