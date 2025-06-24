from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'adminpanel'  # <-- Add this line

urlpatterns = [ 
    path('users/', views.user_list, name='user_list'),
    path('schedules/', views.assessment_schedule_view, name='assessment_schedule'),
    path('signup/',views.SignupPage,name='signup'),
    path('add-user/', views.add_user_ajax, name='add_user_ajax'),
]