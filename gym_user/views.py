from django.shortcuts import render, redirect
from gym_admin.models import CreatePlan, AddMachineryDetails 
from .models import EnterFeedback
from gym_trainee.models import *

# Create your views here.
def userhome(request):
    user_id = request.session['user_id']
    user = Register.objects.get(id=user_id)
    return render(request, 'userhome.html', {"user":user})

    
def feedback(request):
      if request.method == 'POST':
        feed_name = request.POST['feedname']
        feed_mail = request.POST['feedmail']
        feed_text = request.POST['feedtext']

        register = EnterFeedback(f_name=feed_name, f_mail=feed_mail, f_feedback=feed_text)
        register.save()
        print("saved")
        return redirect('gym_user:feedback')

      return render(request,'feedback.html/')
def viewroutine(request):
    return render(request,'viewroutine.html/')
def viewdiet(request):
    user_id = request.session['user_id']
    dietplan = UserHealthStatus.objects.filter(user_fk=user_id).first()

    return render(request,'viewdiet.html/', {"dietplan":dietplan})
def viewplan(request):
    userplan = CreatePlan.objects.all()
    return render(request,'viewplan.html/', {"userplan":userplan},)
def viewmachinery(request):
    machineries = AddMachineryDetails.objects.all()

    return render(request,'viewmachinery.html/', {"machineries":machineries})
def workoutsummary(request, id):
    planuser = CreatePlan.objects.get(id=id)
    return render(request,'workoutsummary.html/', {"planuser":planuser})

def healthstatus(request):
    user_id = request.session['user_id']
    users_name = Register.objects.get(id=user_id)
    health_status = UserHealthStatus.objects.filter(user_fk=user_id).first()
    return render(request, 'healthstatus.html', {"health_status":health_status, "users_name":users_name})
def routineplan(request):
    exc_type = UploadRoutine.objects.all()

    return render(request,'routineplan.html/', {"exc_type":exc_type})



       