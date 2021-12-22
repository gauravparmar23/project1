from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Departments
from EmployeeApp.serializers import DepartmentSerializer

@csrf_exempt
def departmentApi(request,id=0):
    if request.method == "POST":
        department_data =JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Sucessfully",safe=False)
        return JsonResponse("failed to add",safe=False)