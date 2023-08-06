from django.shortcuts import render, redirect
from gym_admin.models import CreatePlan, AddMachineryDetails 
from .models import EnterFeedback
from gym_trainee.models import *
import datetime
from django.utils import timezone

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
    users = Register.objects.get(id=user_id)
    health_status = UserHealthStatus.objects.filter(user_fk=user_id).first()
    today = timezone.now()
    print("today: ",today)
    one_week_ago = today - datetime.timedelta(days=7)
    print("one_week_ago: ",one_week_ago)
    print("user: ",users.time_stamp)
    total_days_to_work = (today - users.time_stamp).days // 7 * 6
    print("total_days_to_work: ",total_days_to_work)
    present_days = UserAttendance.objects.filter(
        user_fk=users,
        timestamp__gte=one_week_ago,
        timestamp__lt=today,
        attendance="present"
    ).count()
    return render(request, 'healthstatus.html', {"health_status":health_status, "users_name":users, "total_days_to_work":total_days_to_work, "present_days": present_days})
def routineplan(request):
    exc_type = UploadRoutine.objects.all()

    return render(request,'routineplan.html/', {"exc_type":exc_type})



       