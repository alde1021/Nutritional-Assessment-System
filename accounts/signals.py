from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Student

@receiver(pre_save, sender=Student)
def copy_grade_section(sender, instance, **kwargs):
    if instance.user:
        instance.grade_level = instance.user.grade_level
        instance.section = instance.user.section