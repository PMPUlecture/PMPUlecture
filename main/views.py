from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Lecturer, Subject, Programme, Materials

# Create your views here.


def index(req):
    return render(req, 'index.html')


def get_lecturer(req):
    lecturers = Lecturer.objects.all()
    print(lecturers)
    #response_data = serializers.serialize('json', lecturers)
    return JsonResponse({'lecturers': [obj.as_dict() for obj in lecturers]}, safe=False)


def get_programmes(req):
    progr = Programme.objects.filter(degree='bachelor')
    print(progr)
    resp = JsonResponse({'programmes': [obj.as_dict() for obj in progr]})
    resp.setdefault('Access-Control-Allow-Origin', '*')
    #resp.setdefault('Access-Control-Allow-Headers', 'Access-Control-Allow-Headers')
    return resp

