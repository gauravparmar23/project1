from django.db import models
from django.db.models import fields
from rest_framework import serializers
from EmployeeApp.models import Departments

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=("DepartmentId","DepartmentItem")