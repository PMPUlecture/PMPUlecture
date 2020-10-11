from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import lecturer, Subject

# Create your views here.


def index(req):
    return render(req, 'index.html')


def get_lecturer(req):
    lecturers = lecturer.objects.all()
    #response_data = serializers.serialize('json', lecturers)
    return JsonResponse({'lecturers': [obj.as_dict() for obj in lecturers]}, safe=False)

