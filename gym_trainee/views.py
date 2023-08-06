from django.shortcuts import render,redirect
from gym_admin.models import TraineeRegister
from gym_trainee.models import UserHealthStatus, UploadRoutine
from fitness.models import Register
from .models import *
import datetime

# Create your views here.
def traineehome(request):
    return render(request, 'traineehome.html')
def traineeform(request, id):
    
          
     return render(request, 'traineeform.html')
def uploadhealthstatus(request, id):
    user_status = Register.objects.get(id=id)
    if request.method == 'POST':
        user_health_status = request.POST['healthstatus']
        status_uploading_date = request.POST['healthstatusdate']
        check_status = UserHealthStatus.objects.filter(user_fk=id).first()
        if check_status:
            UserHealthStatus.objects.filter(user_fk=id).update(user_healthstatus=user_health_status,uploading_date=status_uploading_date)
        else:
            register = UserHealthStatus(user_fk=user_status, user_healthstatus=user_health_status, uploading_date=status_uploading_date)
            register.save()
            print('saved')

        return redirect('gym_trainee:traineehome')
    return render(request, 'uploadhealthstatus.html', {"user_status":user_status})
def markattendance(request):
    user_detail = Register.objects.all()
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0,second=0, microsecond=0)
    if now > midnight and not request.user.is_anonymous:
        user_detail.update(attendance=None)
    if request.method == 'POST':
        
        for user in user_detail:
            attendance = request.POST.get("attendance_"+str(user.id), 'absent')
            if user.attendance == "present" or user.attendance == "absent":
                UserAttendance.objects.filter(user_fk=user).update(attendance=attendance)
                Register.objects.filter(id=user.id).update(attendance=attendance)
            else:
                mark_attendance = UserAttendance(user_fk=user, attendance=attendance)
                user.attendance = attendance
                user.save()
                mark_attendance.save()
        return redirect("gym_trainee:markattendance")
        # else:
        #     message = "Attendance can only be marked until 12 AM"
        #     return render(request,'markattendance.html', {"user_detail":user_detail, "message":message})
        # for  user in user_detail:
        #     user.attendance  = UserAttendance.objects.filter(user_fk=user, timestamp__gte=midnight)
    return render(request,'markattendance.html', {"user_detail":user_detail})
        

def uploadroutine(request):
    msg = 'msg'
    if request.method == 'POST':
        type_of_excercise = request.POST['ex_type']
        day_0ne = request.POST['day1']
        day_two = request.POST['day2']
        day_three = request.POST['day3']
        day_four = request.POST['day4']
        day_five = request.POST['day5']
        day_six = request.POST['day6']
        day_sev = request.POST['day7']
        excercise_type_exist =UploadRoutine.objects.filter(excercise_type=type_of_excercise) 
        if excercise_type_exist:
            msg = 'this type is already added'
        else:
            register=UploadRoutine(excercise_type=type_of_excercise, day_1=day_0ne, day_2=day_two, day_3=day_three, day_4=day_four, day_6=day_six, day_7=day_sev)
            register.save()
            return redirect('gym_trainee:uploadroutine')

   

    return render(request,'uploadroutine.html', {"msg":msg})
def traineeviewuserregister(request):
    traineeviewuser = Register.objects.all()
    return render(request, 'traineeviewuserregister.html', {"traineeviewuser":traineeviewuser})
def dietplan(request, id):
    if request.method == 'POST':
        user_fk = Register.objects.get(id=id)
        print("workint 1")
        foodto_add = request.POST.getlist('required_food[]')
        foodto_avoid = request.POST.getlist('notrequired_food[]')
        preworkout_food = request.POST.getlist('pre_workout_food[]')
        postworkout_food =request.POST.getlist('Post_workout_food[]')
        diet_check = FitnessDietPlan.objects.filter(user_fk=id).first()
        user_fk = Register.objects.get(id=id)

        #foodtoadd
        all_foodtoadd = []
        foodtoadd_dict = {}
        required_food = []
        print(foodto_add)
        for foodtoadd in foodto_add:
            foodtoadd_data = {}
            quantity_key = foodtoadd + '_type'
            quantity = request.POST[quantity_key]
            print(foodtoadd, quantity )
            foodtoadd_data["foodtoadd"] = foodtoadd
            foodtoadd_data["quantity"] = quantity
            required_food.append(foodtoadd_data)

        foodtoadd_dict["foodtoadd"] = required_food
        all_foodtoadd.append(foodtoadd_dict)

        #foodtoavoid
        all_foodtoavoid = []
        foodtoavoid_dict = {}
        notrequired_food = []
        for foodtoavoid in foodto_avoid:
            foodtoavoid_data ={}
            quantity_key = foodtoavoid + '_type'
            quantity = request.POST[quantity_key]
            print(foodtoavoid, quantity )
            foodtoavoid_data["foodtoavoid"] = foodtoavoid
            foodtoavoid_data["quantity"] = quantity
            notrequired_food.append(foodtoavoid_data)

        foodtoavoid_dict["foodtoavoid"] = notrequired_food
        all_foodtoavoid.append(foodtoavoid_dict)
        
        #preworkoutfood
        all_preworkoutfood = []
        preworkout_dict = {}
        pre_workout_food = []
        for preworkoutfood in preworkout_food:
            preworkout_data ={}
            quantity_key = preworkoutfood + '_type'
            quantity = request.POST[quantity_key]
            print(preworkoutfood, quantity )
            preworkout_data["preworkoutfood"] = preworkoutfood
            preworkout_data["quantity"] = quantity
            notrequired_food.append(preworkout_data)

        preworkout_dict["preworkoutfood"] = pre_workout_food
        all_preworkoutfood.append(preworkout_dict)

        #postworkoutfood
        all_postworkoutfood = []
        postworkout_dict = {}
        post_workout_food = []
        for postworkoutfood in postworkout_food:
            postworkout_data = {}
            quantity_key = postworkoutfood + '_type'
            quantity = request.POST[quantity_key]
            print(postworkout_data, quantity )
            postworkout_data["postworkoutfood"] = postworkout_data
            postworkout_data["quantity"] = quantity
            post_workout_food.append(postworkout_data)

        postworkout_dict["postworkoutfood"] = post_workout_food
        all_postworkoutfood.append(postworkout_dict)
        
        if diet_check:
            FitnessDietPlan.objects.filter(user_fk=id).update(food_to_add=foodtoadd_dict, food_to_avoid=foodtoavoid_dict, pre_workout_food=preworkout_dict, post_workout_food=postworkout_dict)
            return redirect("gym_trainee:traineehome")
        else:
            register = FitnessDietPlan(user_fk=user_fk, food_to_add=foodtoadd_dict, food_to_avoid=foodtoavoid_dict, pre_workout_food=preworkout_dict, post_workout_food=postworkout_dict)
            register.save()
            return redirect("gym_trainee:traineehome")

    return render(request, 'dietplan.html')