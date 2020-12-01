from django.http import JsonResponse
from django.views import View
from ..models import Lecturer, Subject, Programme, Materials
from django.core.exceptions import ValidationError
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
        id_subject_for_material :id
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

        id_subject = request.GET.get('id_subject_for_material') or None
        print(id_subject)

        resp = JsonResponse([lector.as_dict(subjects=is_subjects, apmath=is_apmath, materials=is_materials,
                                            photo=is_photo, vk=is_vk, id_subject_for_material=id_subject) for lector in self.lecturers], safe=False)
        resp.setdefault('Access-Control-Allow-Origin', '*')
        return resp

    def post(self, request):
        # if not request.user.is_authenticated:
        #     resp = JsonResponse({'status': 'error', 'error': 'Permission denied'})
        #     resp.setdefault('Access-Control-Allow-Origin', '*')
        #     resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT')
        #     resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
        #     return resp

        data = json.loads(request.body)
        subjects = Subject.objects.filter(id__in=list(map(int, data['subjects'])))
        if not subjects:
            resp = JsonResponse({'status': 'error', 'error': 'there is no such subjects'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp
        del data['subjects']

        if not data['apmath_url'].startswith('http://') and not data['apmath_url'].startswith('https://'):
            data['apmath_url'] = "http://" + data['apmath_url']
        if not data['vk_discuss_url'].startswith('http://') and not data['vk_discuss_url'].startswith('https://'):
            data['vk_discuss_url'] = "http://" + data['vk_discuss_url']
        if 'photo_url' in data and not data['photo_url'].startswith('http://') and not data['photo_url'].startswith('https://'):
            data['photo_url'] = "http://" + data['photo_url']

        new_lecturer = Lecturer.objects.create(**data)
        new_lecturer.subject.set(subjects)

        try:
            new_lecturer.clean_fields()
        except ValidationError as e:
            resp = JsonResponse({'status': 'error', 'error': e.message_dict})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        resp = JsonResponse({'status': 'ok'}, safe=False)
        resp.setdefault('Access-Control-Allow-Origin', '*')
        resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT')
        resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
        return resp

    def put(self, request):
        if not request.user.is_authenticated:
            resp = JsonResponse({'status': 'error', 'error': 'Permission denied'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        data = json.loads(request.body)
        lecturer = Lecturer.objects.filter(id=int(data['id'])).first()
        if not lecturer:
            resp = JsonResponse({'status': 'error', 'error': 'there is no such lecturer'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        data['subjects'] = Subject.objects.filter(id__in=list(map(int, data['subjects'])))
        if not data['subjects']:
            resp = JsonResponse({'status': 'error', 'error': 'there is no such subjects'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        if not data['apmath_url'].startswith('http://') and not data['apmath_url'].startswith('https://'):
            data['apmath_url'] = "http://" + data['apmath_url']
        if not data['vk_discuss_url'].startswith('http://') and not data['vk_discuss_url'].startswith('https://'):
            data['vk_discuss_url'] = "http://" + data['vk_discuss_url']
        if 'photo_url' in data and not data['photo_url'].startswith('http://') and not data['photo_url'].startswith('https://'):
            data['photo_url'] = "http://" + data['photo_url']

        lecturer.name = data['name']
        lecturer.subject.set(data['subjects'])
        lecturer.apmath_url = data['apmath_url']
        lecturer.vk_discuss_url = data['vk_discuss_url']
        if 'photo_url' in data:
            lecturer.photo_url = data['photo_url']

        try:
            lecturer.clean_fields()
        except ValidationError as e:
            resp = JsonResponse({'status': 'error', 'error': e.message_dict})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        lecturer.save()

        resp = JsonResponse({'status': 'ok'})
        resp.setdefault('Access-Control-Allow-Origin', '*')
        resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT')
        resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
        return resp


class UserDetail(View):
    def get(self, request):
        response = {"is_authenticated": request.user.is_authenticated}
        if response["is_authenticated"]:
            response.update(email=request.user.email,
                            first_name=request.user.first_name,
                            last_name=request.user.last_name,
                            is_admin=request.user.groups.filter(name='admin').exists()),

        resp = JsonResponse(response)
        resp.setdefault('Access-Control-Allow-Origin', '*')
        return resp


class MaterialView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            resp = JsonResponse({'status': 'error', 'error': 'Permission denied'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        data = json.loads(request.body)

        if not data['link'].startswith('http://') and not data['link'].startswith('https://'):
            data['link'] = "http://" + data['link']

        data['subject'] = Subject.objects.filter(id=int(data['subject'])).first()
        if not data['subject']:
            resp = JsonResponse({'status': 'error', 'error': 'there is no such subject'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        data['lecturer'] = Lecturer.objects.filter(id=int(data['lecturer'])).first()
        if not data['lecturer']:
            resp = JsonResponse({'status': 'error', 'error': 'there is no such lecturer'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        if request.user.is_authenticated:
            data['author'] = request.user

        if 'year_of_relevance' in data:
            data['year_of_relevance'] = int(data['year_of_relevance'])

        material = Materials.objects.create(**data)
        try:
            material.clean_fields()
        except ValidationError as e:
            if 'link' in e.message_dict:
                resp = JsonResponse({'status': 'error', 'error': e.message_dict['link'][0]})
            else:
                resp = JsonResponse({'status': 'error', 'error': e.message_dict})
                return resp
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        resp = JsonResponse({'status': 'ok'})
        resp.setdefault('Access-Control-Allow-Origin', '*')
        resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
        resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
        return resp

    def put(self, request):
        if not request.user.is_authenticated:
            resp = JsonResponse({'status': 'error', 'error': 'Permission denied'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        data = json.loads(request.body)
        material = Materials.objects.filter(id=int(data['id'])).first()
        if not material:
            resp = JsonResponse({'status': 'error', 'error': 'there is no such material'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        if material.author != request.user:
            resp = JsonResponse({'status': 'error', 'error': 'Permission denied'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        data['subject'] = Subject.objects.filter(id=int(data['subject'])).first()
        if not data['subject']:
            resp = JsonResponse({'status': 'error', 'error': 'there is no such subject'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        data['lecturer'] = Lecturer.objects.filter(id=int(data['lecturer'])).first()
        if not data['lecturer']:
            resp = JsonResponse({'status': 'error', 'error': 'there is no such lecturer'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        if not data['link'].startswith('http://') and not data['link'].startswith('https://'):
            data['link'] = "http://" + data['link']

        if 'year_of_relevance' in data:
            data['year_of_relevance'] = int(data['year_of_relevance'])

        material.name = data['name']
        material.type = data['type']
        material.subject = data['subject']
        material.lecturer = data['lecturer']
        material.link = data['link']
        material.year_of_relevance = data['year_of_relevance']

        try:
            material.clean_fields()
        except ValidationError as e:
            if 'link' in e.message_dict:
                resp = JsonResponse({'status': 'error', 'error': e.message_dict['link'][0]})
            else:
                resp = JsonResponse({'status': 'error', 'error': e.message_dict})
                return resp
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        material.save()

        resp = JsonResponse({'status': 'ok'})
        resp.setdefault('Access-Control-Allow-Origin', '*')
        resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
        resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
        return resp

    def delete(self, request):
        if not request.user.is_authenticated:
            resp = JsonResponse({'status': 'error', 'error': 'Permission denied'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        data = json.loads(request.body)
        material = Materials.objects.filter(id=int(data['id'])).first()
        if not material:
            resp = JsonResponse({'status': 'error', 'error': 'there is no such material'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        if material.author != request.user:
            resp = JsonResponse({'status': 'error', 'error': 'Permission denied'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        material.delete()

        resp = JsonResponse({'status': 'ok'})
        resp.setdefault('Access-Control-Allow-Origin', '*')
        resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
        resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
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

    def post(self, request):
        if not request.user.is_authenticated:
            resp = JsonResponse({'status': 'error', 'error': 'Permission denied'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        data = json.loads(request.body)
        data['programme'] = Programme.objects.filter(id=data['programme']).first()
        if not data['programme']:
            resp = JsonResponse({'status': 'error', 'error': 'there is no such programme'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp
        data['term'] = int(data['term'])
        if data['term'] not in range(1, 9):
            resp = JsonResponse({'status': 'error', 'error': 'term should be between 1 and 8'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        new_subject = Subject.objects.create(**data)
        try:
            new_subject.clean_fields()
        except ValidationError as e:
            resp = JsonResponse({'status': 'error', 'error': e.message_dict})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        resp = JsonResponse({'status': 'ok'})
        resp.setdefault('Access-Control-Allow-Origin', '*')
        resp.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
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
