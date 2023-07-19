from django.db import models

# Create your models here.
class DoctorModel(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    qualification=models.CharField(max_length=100)
    adhaar=models.CharField(max_length=12)