from django.db import models
from django.db.models import fields
from rest_framework import serializers
from app.models import School

class schoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields=("SchoolID","SchoolItem")