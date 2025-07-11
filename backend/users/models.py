from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

class CustomUser(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    skills = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    experience_years = models.PositiveIntegerField(default=0)
    education = models.CharField(max_length=255, blank=True)
