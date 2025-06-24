from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['id_no','last','first','middle', 'age', 'birthday', 'weight', 'height', 'gender',
        'grade_level', 'section', 'assessment_type', 'school_year', 'date_of_weighing']


admin.site.register(Student,StudentAdmin)
