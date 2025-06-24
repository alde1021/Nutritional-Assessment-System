from django.db import models
from django.contrib.auth.models import User
from datetime import date
import math
from django import forms
from django.conf import settings
from adminpanel.models import CustomUser

class Student(models.Model):
    id_no= models.IntegerField(unique=True)
    last = models.CharField(max_length=25)
    first = models.CharField(max_length=25)
    middle = models.CharField(max_length=25)
    age = models.CharField(max_length=25)     # Consider using IntegerField
    birthday = models.DateField()
    weight = models.FloatField()  # kg
    height = models.FloatField()  # m
    gender = models.CharField(max_length=25)
    grade_level = models.CharField(max_length=50)   
    section = models.CharField(max_length=50)       

    # Inherited from user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    grade_level = models.CharField(max_length=20, default='Unknown')
    section = models.CharField(max_length=20, default='Unknown')
     # New fields
    assessment_type = models.CharField(
        max_length=20,
        choices=[('Baseline', 'Baseline'), ('Terminal', 'Terminal')],
        blank=False,
        null=False
    )
    school_year = models.CharField(max_length=9,  
        blank=False,
        null=False
    )
    date_of_weighing = models.DateField(blank=False,
        null=False
        )

    def clean_id_no(self):
        id_no = self.cleaned_data['id_no']
        if Student.objects.filter(id_no=id_no).exists():
            raise forms.ValidationError("This ID Number already exists.")
        return id_no
    
    def height_m(self):
        return round(float(self.height), 2)

    def height_squared(self):
        h = float(self.height)
        return round(h ** 2, 4)

    def bmi(self):
        try:
            h_m = float(self.height) 
            return round(float(self.weight) / (h_m ** 2), 2) if h_m else 0
        except (ValueError, TypeError):
            return 0

    def age_years_months(self):
        today = date.today()
        years = today.year - self.birthday.year
        months = today.month - self.birthday.month
        if today.day < self.birthday.day:
            months -= 1
        if months < 0:
            years -= 1
            months += 12
        return f"{years}, {months}"

    def nutritional_status(self):
        bmi = self.bmi()
        if bmi < 12.5:
            return "Severely Wasted"
        elif bmi < 15:
            return "Wasted"
        elif bmi <= 18.5:
            return "Normal"
        else:
            return "Overweight"

    def height_for_age(self):
        try:
            height_cm = float(self.height) * 100  # convert meters to cm

            if height_cm < 110:
                return "Sev. Stunted"
            elif height_cm < 120:
                return "Stunted"
            elif height_cm < 140:
                return "Normal"
            else:
                return "Tall"
        except (ValueError, TypeError):
            return "Unknown"