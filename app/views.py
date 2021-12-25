from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from app.models import School
from app.serializers import schoolSerializer

@csrf_exempt
def schoolApi(request,id=0):
    if request.method == "POST":
        School_data =JSONParser().parse(request)
        School_serializer=schoolSerializer(data=School_data)
        if School_serializer.is_valid():
            School_serializer.save()
            return JsonResponse("Added Sucessfully",safe=False)
        return JsonResponse("failed to add",safe=False)