from django import forms
from accounts.models import Student


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['user', 'grade_level', 'section']
