from django.http import JsonResponse
from django.views import View
from ..models import Lecturer, Subject, Programme, Materials
import json


def list_of_fields(string: str):
    return string.replace(' ', '').split(',')


class LecturerView(View):
    lecturers = Lecturer.objects.all()

    def get(self, request):
        """params:
        fields=subjects,materials,apmath,photo,vk
        id :id
        name :string
        subject :id
        """
        if request.GET.get("id"):
            self.lecturers = self.lecturers.filter(pk=request.GET.get("id"))
        if request.GET.get("name"):
            self.lecturers = self.lecturers.filter(name__icontains=request.GET.get("name"))
        if request.GET.get("subject"):
            self.lecturers = self.lecturers.filter(subject=request.GET.get("subject"))

        if not self.lecturers:
            resp = JsonResponse({'error': 'there is no such lecturer'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            return resp

        fields = list_of_fields(request.GET.get("fields")) if request.GET.get("fields") else []
        is_subjects = "subjects" in fields
        is_materials = "materials" in fields
        is_apmath = "apmath" in fields
        is_photo = "photo" in fields
        is_vk = "vk" in fields

        resp = JsonResponse([lector.as_dict(subjects=is_subjects, apmath=is_apmath, materials=is_materials,
                                            photo=is_photo, vk=is_vk) for lector in self.lecturers], safe=False)
        resp.setdefault('Access-Control-Allow-Origin', '*')
        return resp

    def post(self, request):
        data = json.loads(request.body)
        subject = Subject.objects.filter(id__in=list(map(int, data['subject'])))
        del data['subject']

        new_lecturer = Lecturer.objects.create(**data)
        new_lecturer.subject.set(subject)

        resp = JsonResponse({'ok': 'ok'}, safe=False)
        resp.setdefault('Access-Control-Allow-Origin', '*')
        return resp


class UserDetail(View):
    def get(self, request):
        response = {"is_authenticated": request.user.is_authenticated}
        if response["is_authenticated"]:
            response.update(email=request.user.email,
                            first_name=request.user.first_name,
                            last_name=request.user.last_name)

        resp = JsonResponse(response)
        resp.setdefault('Access-Control-Allow-Origin', '*')
        return resp


class MaterialView(View):
    def post(self, request):
        data = json.loads(request.body)
        data['subject'] = Subject.objects.filter(id=int(data['subject'])).first()
        if not data['subject']:
            resp = JsonResponse({'error': 'there is no such subject'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            return resp
        data['lecturer'] = Lecturer.objects.filter(id=int(data['lecturer'])).first()
        if not data['lecturer']:
            resp = JsonResponse({'error': 'there is no such lecturer'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            return resp

        Materials.objects.create(**data)

        resp = JsonResponse({'ok': 'ok'})
        resp.setdefault('Access-Control-Allow-Origin', '*')
        return resp


class SubjectsView(View):
    subjects = Subject.objects.all()

    def get(self, request):
        """params:
        fields=lecturers,term,programme
        lecturer :id
        term :int
        programme :id
        """
        if request.GET.get('lecturer'):
            self.subjects = self.subjects.filter(lecturer=request.GET.get('lecturer'))
        if request.GET.get('term'):
            self.subjects = self.subjects.filter(term=request.GET.get('term'))
        if request.GET.get('programme'):
            self.subjects = self.subjects.filter(programme=request.GET.get('programme'))

        fields = []
        if request.GET.get('fields'):
            fields = list_of_fields(request.GET.get('fields'))
        is_lecturers = 'lecturers' in fields
        is_term = 'term' in fields
        is_programme = 'programme' in fields

        if self.subjects:
            output = dict()
            if request.GET.get('programme'):
                try:
                    output['programme'] = Programme.objects.get(pk=request.GET.get('programme')).name
                except:
                    resp = JsonResponse({'error': 'there are no such programme'})
                    resp.setdefault('Access-Control-Allow-Origin', '*')
                    return resp
            if is_term:
                output["terms"] = [{'term': term, 'subjects':
                    [subj.as_dict(lecturer=is_lecturers, programme=is_programme) for subj in self.subjects.filter(term=term)]}
                                   for term in range(1, 9)]
            else:
                output['subjects'] = [subj.as_dict(lecturer=is_lecturers, programme=is_programme)
                                      for subj in self.subjects]
            resp = JsonResponse(output)
            resp.setdefault('Access-Control-Allow-Origin', '*')
            return resp
        else:
            resp = JsonResponse({'error': 'there are no such subjects'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            return resp


class ProgrammeView(View):
    def get(self, request):
        """params: fields=img_url"""
        is_img_url = bool(request.GET.get('fields'))
        queryset = Programme.objects.all()
        response_raw = dict()
        for degree in Programme.TypeOfDegrees.choices:
            response_raw[degree[0]] = [obj.as_dict(img_url=is_img_url) for obj in queryset.filter(degree=degree[0])]
        resp = JsonResponse(response_raw, safe=False)
        resp.setdefault('Access-Control-Allow-Origin', '*')
        return resp
