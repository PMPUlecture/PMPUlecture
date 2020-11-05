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
    if req.GET.get('programme'):
        programme = Programme.objects.filter(name=req.GET.get('programme').rstrip('/')).first()
        if not programme:
            resp = JsonResponse({'error': 'there is no such programme'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            return resp
    else:
        resp = JsonResponse({'error': 'you should give a programme'})
        resp.setdefault('Access-Control-Allow-Origin', '*')
        return resp

    resp = JsonResponse([{'term': term, 'subjects':
        [{'id': subject.id, 'name': subject.name, 'lecturers':
            [{'id': lecturer.id, 'name': lecturer.name} for lecturer in Lecturer.objects.filter(subject=subject)]}
         for subject in Subject.objects.filter(term=term, programme=programme)]} for term in range(1, 9)], safe=False)
    resp.setdefault('Access-Control-Allow-Origin', '*')
    return resp


def get_programmes(req):
    queryset = Programme.objects.all()
    response_raw = dict()
    for degree in Programme.TypeOfDegrees.choices:
        response_raw[degree[0]] = [obj.as_dict() for obj in queryset.filter(degree=degree[0])]
    # resp = JsonResponse({'programmes': {'bachelor': [obj.as_dict() for obj in progrb], 'master': [obj.as_dict() for obj in progrm]}})
    resp = JsonResponse(response_raw)
    resp.setdefault('Access-Control-Allow-Origin', '*')
    return resp
