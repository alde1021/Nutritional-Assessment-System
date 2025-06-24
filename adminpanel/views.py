from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.contrib import messages
from .forms import AssessmentScheduleForm
from .models import AssessmentSchedule
from django.template.loader import render_to_string
User = get_user_model()  # This will now point to CustomUser

def user_list(request):
    users = User.objects.all()
    return render(request, 'adminpanel/user.html', {'users': users})

def assessment_schedule_view(request):
    if request.method == 'POST':
        form = AssessmentScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Schedule created successfully!")
            return redirect('adminpanel:assessment_schedule')  # or wherever you want
        else:
            print("FORM ERRORS:", form.errors)
    else:
        form = AssessmentScheduleForm()
    schedules = AssessmentSchedule.objects.all()  # 🟩 add this line
    return render(request, 'adminpanel/schedules.html', {
        'form': form,
        'schedules': schedules 
        }, )

def SignupPage(request):
    mem = User.objects.all()  # Get all user records
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('adminpanel:signup')
        else:
            print("FORM ERRORS:", form.errors)
            
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def add_user_ajax(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})