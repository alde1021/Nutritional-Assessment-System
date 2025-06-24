from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import AssessmentSchedule  # import your model

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = (
        'username', 'email', 'last_name', 'first_name', 'middle_name',
        'grade_level', 'section', 'position'
    )

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('middle_name', 'grade_level', 'section', 'position')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('middle_name', 'grade_level', 'section', 'position')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(AssessmentSchedule)  # register it here


