from django.http import JsonResponse
from django.views import View
from ..models import Lecturer, Subject, Programme, Materials
import json


class DetailLecturer(View):
    def get(self, request, id):
        lecturer = Lecturer.objects.filter(pk=id).first()
        if not lecturer:
            resp = JsonResponse({'error': 'there is no such lecturer'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            return resp

        return JsonResponse(lecturer.as_dict(materials=True), safe=False)

    def post(self, request):
        data = json.loads(request.body)
        subject = Subject.objects.filter(id__in=list(map(int, data['subject'])))
        del data['subject']

        new_lecturer = Lecturer.objects.create(**data)
        new_lecturer.subject.set(subject)

        return JsonResponse(new_lecturer.as_dict(subjects=True, apmath=True, photo=True, vk_discuss=True), safe=False)


class DetailMaterial(View):
    def post(self, request):
        data = json.loads(request.body)
        data['subject'] = Subject.objects.filter(id=int(data['subject'])).first()
        data['lecturer'] = Lecturer.objects.filter(id=int(data['lecturer'])).first()

        new_material = Materials.objects.create(**data)

        return JsonResponse(new_material.as_dict(), safe=False)


class DetailProgramme(View):
    def get(self, request):
        if request.GET.get('programme'):
            programme = Programme.objects.filter(name=request.GET.get('programme').rstrip('/')).first()
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


class Programmes(View):
    def get(self, request):
        queryset = Programme.objects.all()
        response_raw = dict()
        for degree in Programme.TypeOfDegrees.choices:
            response_raw[degree[0]] = [obj.as_dict() for obj in queryset.filter(degree=degree[0])]
        resp = JsonResponse(response_raw, safe=False)
        resp.setdefault('Access-Control-Allow-Origin', '*')
        return resp
