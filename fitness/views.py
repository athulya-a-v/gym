from django.shortcuts import render

# Create your views here.
 
def home(request):
    return render(request,'fitness/home.html')

def loginn(request):
     return render(request,'fitness/login.html')
def register(request):
     return render(request,'fitness/register.html')
def attend(request):
     return render(request,'fitness/attend.html')
def machinery(request):
     return render(request,'fitness/machinery.html')
def plan(request):
     return render(request,'fitness/plan.html')
def userhome(request):
     return render(request,'fitness/userhome.html')
def feedback(request):
     return render(request,'fitness/feedback.html')
def viewdiet(request):
     return render(request,'fitness/viewdiet.html')
def viewclass(request):
     return render(request,'fitness/viewclass.html')
def viewplan(request):
     return render(request,'fitness/viewplan.html')
def diet(request):
     return render(request,'fitness/diet.html')
