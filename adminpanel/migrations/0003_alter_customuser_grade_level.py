# Generated by Django 5.2 on 2025-06-13 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_assessmentschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='grade_level',
            field=models.CharField(choices=[('kindergarten', 'Kindergarten'), ('Grade1', 'Grade 1'), ('Grade2', 'Grade 2'), ('Grade3', 'Grade 3'), ('Grade4', 'Grade 4'), ('Grade5', 'Grade 5'), ('Grade6', 'Grade 6')], default='kindergarten', max_length=20),
        ),
    ]
