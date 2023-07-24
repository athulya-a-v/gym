from django.shortcuts import render, redirect
from gym_admin.models import CreatePlan, AddMachineryDetails 
from .models import EnterFeedback

# Create your views here.
def userhome(request):
    return render(request,'userhome.html/')
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
def viewclass(request):
    return render(request,'viewclass.html/')
def viewdiet(request):
    return render(request,'viewdiet.html/')
def viewplan(request):
    userplan = CreatePlan.objects.all()
    return render(request,'viewplan.html/', {"userplan":userplan},)
def viewmachinery(request):
    machineries = AddMachineryDetails.objects.all()

    return render(request,'viewmachinery.html/', {"machineries":machineries})
def workoutsummary(request, id):
    planuser = CreatePlan.objects.get(id=id)
    return render(request,'workoutsummary.html/', {"planuser":planuser})

