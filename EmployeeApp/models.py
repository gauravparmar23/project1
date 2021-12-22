from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentsId=models.AutoField(primary_key=True)
    DepartmentsItem=models.CharField(max_length=100)