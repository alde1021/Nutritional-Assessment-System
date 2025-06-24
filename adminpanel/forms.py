from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import AssessmentSchedule

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'last_name', 'first_name', 'middle_name',
            'grade_level', 'section', 'position',
            'email', 'username', 'password1', 'password2'
        ]

class AssessmentScheduleForm(forms.ModelForm):
    class Meta:
        model = AssessmentSchedule
        fields = '__all__'
        widgets = {
            'assessment_type': forms.Select(attrs={'class': 'form-control'}),
            'school_year': forms.TextInput(attrs={'class': 'form-control'}),
            'principal_name': forms.TextInput(attrs={'class': 'form-control'}),
            'school_name': forms.TextInput(attrs={'class': 'form-control'}),
            'school_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }