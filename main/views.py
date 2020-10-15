from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Lecturer, Subject, Programme

# Create your views here.


def index(req):
    return render(req, 'index.html')


def get_lecturer(req):
    lecturers = Lecturer.objects.all()

    return JsonResponse({'lecturers': [obj.as_dict() for obj in lecturers]}, safe=False)

def set_struct(req):
    programme = Programme.objects.filter(name=req.GET.get('programme').rstrip('/')).first()
    if not programme:
        return JsonResponse({'error': 'there is no such programme'})

    return JsonResponse([{'term': term, 'subjects': [{'id': subject.id, 'name': subject.name, 'lecturers': [{'id': lecturer.id, 'name': lecturer.name} for lecturer in Lecturer.objects.filter(subject=subject)]} for subject in Subject.objects.filter(term=term, programme=programme)]} for term in range(1, 9)], safe=False)
