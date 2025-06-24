from django.urls import path, include
from django.contrib import admin
from accounts import views

urlpatterns = [ 
    path('',views.LoginPage,name='login'),
    path('index/',views.index,name="index"),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('student_list/', views.student_list, name='list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('Add/', views.Add_student, name='add'),
    path('update/<int:id_no>/', views.update_student, name='update'),
    path('delete/<int:id_no>/', views.delete_student, name='delete'),
    path('reports/', views.report_view, name='report'),
    path('student-progress/', views.student_progress_search, name='student_progress'),
]
