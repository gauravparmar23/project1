from django.db import models

# Create your models here.
class School(models.Model):
    SchoolId=models.AutoField(primary_key=True)
    SchoolItem=models.CharField(max_length=100)