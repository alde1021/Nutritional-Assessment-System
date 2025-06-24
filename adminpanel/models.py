from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GRADE_LEVEL_CHOICES = [
        ('Kindergarten', 'Kindergarten'),
        ('Grade1', 'Grade 1'),
        ('Grade2', 'Grade 2'),
        ('Grade3', 'Grade 3'),
        ('Grade4', 'Grade 4'),
        ('Grade5', 'Grade 5'),
        ('Grade6', 'Grade 6'),
    ]

    middle_name = models.CharField(max_length=25, blank=True, null=True)
    grade_level = models.CharField(max_length=20, choices=GRADE_LEVEL_CHOICES)
    section = models.CharField(max_length=25, blank=True, null=True)
    position = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.username
    
class AssessmentSchedule(models.Model):
    ASSESSMENT_CHOICES = [
        ('Terminal', 'Terminal'),
        ('Baseline', 'Baseline'),
    ]

    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_CHOICES)
    school_year = models.CharField(max_length=9)  # e.g., "2024-2025"
    principal_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=150)
    school_address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    logo = models.ImageField(upload_to='school_logos/', blank=True, null=True)

    def __str__(self):
        return f"{self.school_name} - {self.assessment_type}"