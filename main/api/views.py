from django.db import IntegrityError
from django.core.validators import URLValidator
from django.http import JsonResponse
from django.views import View
from ..models import Lecturer, Subject, Programme, Materials
from django.core.exceptions import ValidationError
import json


def check_authorization(func):
    def wrapper(self, request, *args):
        if not request.user.is_authenticated:
            return {'status': 'error', 'error': 'Permission denied'}
        return func(self, request, *args)
    return wrapper


def check_blacklist(func):
    def wrapper(self, request, *args):
        if request.user.groups.filter(name='black list').exists():
            return {'status': 'error', 'error': 'Blacklisted user'}
        return func(self, request, *args)
    return wrapper


# headers for CORS
def JSON_response(func):
    def wrapper(*args):
        response = JsonResponse(func(*args), safe=False)
        response.setdefault('Access-Control-Allow-Origin', '*')
        response.setdefault('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, DELETE')
        response.setdefault('Access-Control-Allow-Headers', 'Content-Type')
        return response
    return wrapper


def list_of_fields(string: str):
    return string.replace(' ', '').split(',')


class LecturerView(View):
    lecturers = Lecturer.objects.all()

    @JSON_response
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
            return {'error': 'there is no such lecturer'}

        self.lecturers = self.lecturers.order_by('name')

        fields = list_of_fields(request.GET.get("fields")) if request.GET.get("fields") else []
        is_subjects = "subjects" in fields
        is_materials = "materials" in fields
        is_apmath = "apmath" in fields
        is_photo = "photo" in fields
        is_vk = "vk" in fields

        id_subject = request.GET.get('id_subject_for_material') or None

        return [lector.as_dict(subjects=is_subjects, apmath=is_apmath, materials=is_materials,
                               photo=is_photo, vk=is_vk, id_subject_for_material=id_subject,
                               author=request.user) for lector in self.lecturers]

    @JSON_response
    @check_authorization
    @check_blacklist
    def post(self, request):
        data = json.loads(request.body)
        
        subjects = None
        if 'subjects' in data:
            subjects = Subject.objects.filter(id__in=list(map(int, data['subjects'])))
            if not subjects:
                return {'status': 'error', 'error': 'there is no such subjects'}
            del data['subjects']

        if 'apmath_url' in data and not data['apmath_url'].startswith('http://') and not data['apmath_url'].startswith('https://'):
            data['apmath_url'] = "http://" + data['apmath_url']
        if 'vk_discuss_url' in data and not data['vk_discuss_url'].startswith('http://') and not data['vk_discuss_url'].startswith('https://'):
            data['vk_discuss_url'] = "http://" + data['vk_discuss_url']
        if 'photo_url' in data and not data['photo_url'].startswith('http://') and not data['photo_url'].startswith('https://'):
            data['photo_url'] = "http://" + data['photo_url']

        new_lecturer = Lecturer.objects.create(**data)
        if subjects:
            new_lecturer.subject.set(subjects)

        try:
            new_lecturer.clean_fields()
        except ValidationError as e:
            return {'status': 'error', 'error': e.message_dict}

        return {'status': 'ok'}

    @JSON_response
    #@check_authorization
    @check_blacklist
    def put(self, request):
        data = json.loads(request.body)
        lecturer = Lecturer.objects.filter(id=int(data['id'])).first()
        if not lecturer:
            resp = JsonResponse({'status': 'error', 'error': 'there is no such lecturer'})
            resp.setdefault('Access-Control-Allow-Origin', '*')
            resp.setdefault('Access-Control-Allow-Methods', 'PUT')
            resp.setdefault('Access-Control-Allow-Headers', 'Content-Type')
            return resp

        if request.user.groups.filter(name='admin').exists(): # Изменение всех полей доступно только админам
            if data.get('apmath_url') and not data['apmath_url'].startswith('http://') and not data['apmath_url'].startswith('https://'):
                data['apmath_url'] = "http://" + data['apmath_url']
            if data.get('vk_discuss_url') and not data['vk_discuss_url'].startswith('http://') and not data['vk_discuss_url'].startswith('https://'):
                data['vk_discuss_url'] = "http://" + data['vk_discuss_url']
        if data.get('photo_url') and 'photo_url' in data and not data['photo_url'].startswith('http://') and not data['photo_url'].startswith('https://'):
            data['photo_url'] = "http://" + data['photo_url']

            lecturer.name = data.get('name') or lecturer.name

            lecturer.apmath_url = data.get('apmath_url') or lecturer.apmath_url
            lecturer.vk_discuss_url = data.get('vk_discuss_url') or lecturer.vk_discuss_url
            lecturer.photo_url = data.get('photo_url') or lecturer.photo_url

        if data.get('subjects'):
            try:
                lecturer.subject.add(*data['subjects'])
            except IntegrityError:
                return {'status': 'error', 'error': 'there is no such subjects'}

        try:
            lecturer.clean_fields()
        except ValidationError as e:
            return {'status': 'error', 'error': e.message_dict}

        lecturer.save()
        return {'status': 'ok'}


class UserDetail(View):
    @JSON_response
    def get(self, request):
        response = {"is_authenticated": request.user.is_authenticated}
        if response["is_authenticated"]:
            response.update(email=request.user.email,
                            first_name=request.user.first_name,
                            last_name=request.user.last_name,
                            is_admin=request.user.groups.filter(name='admin').exists()),

        return response


class MaterialView(View):
    @JSON_response
    @check_authorization
    @check_blacklist
    def post(self, request):

        data = json.loads(request.body)
        validator = URLValidator()
        try:
            validator(data.get('link'))
        except ValidationError as e:
            return {'status': 'error', 'error': e.message}

        data['subject'] = Subject.objects.filter(id=int(data['subject'])).first()
        if not data['subject']:
            return {'status': 'error', 'error': 'there is no such subject'}

        data['lecturer'] = Lecturer.objects.filter(id=int(data['lecturer'])).first()
        if not data['lecturer']:
            return {'status': 'error', 'error': 'there is no such lecturer'}

        if request.user.is_authenticated:
            data['author'] = request.user

        if 'year_of_relevance' in data:
            data['year_of_relevance'] = int(data['year_of_relevance'])

        Materials.objects.create(**data)

        return {'status': 'ok'}

    @JSON_response
    @check_authorization
    @check_blacklist
    def put(self, request):
        data = json.loads(request.body)
        material = Materials.objects.filter(id=int(data['id'])).first()
        if not material:
            return {'status': 'error', 'error': 'there is no such material'}

        if material.author != request.user and not request.user.groups.filter(name='admin').exists():
            return {'status': 'error', 'error': 'Permission denied'}

        if 'subject' in data:
            data['subject'] = Subject.objects.filter(id=int(data['subject'])).first()
            if not data['subject']:
                return {'status': 'error', 'error': 'there is no such subject'}
            material.subject = data['subject']

        if 'lecturer' in data:
            data['lecturer'] = Lecturer.objects.filter(id=int(data['lecturer'])).first()
            if not data['lecturer']:
                return {'status': 'error', 'error': 'there is no such lecturer'}
            material.lecturer = data['lecturer']

        if 'link' in data:
            if not data['link'].startswith('http://') and not data['link'].startswith('https://'):
                data['link'] = "http://" + data['link']
            material.link = data['link']

        if 'year_of_relevance' in data:
            if 'year_of_relevance' in data:
                data['year_of_relevance'] = int(data['year_of_relevance'])
            material.year_of_relevance = data['year_of_relevance']

        if 'name' in data:
            material.name = data['name']

        if 'type' in data:
            material.type = data['type']

        try:
            material.clean_fields()
        except ValidationError as e:
            if 'link' in e.message_dict:
                return {'status': 'error', 'error': e.message_dict['link'][0]}
            else:
                return {'status': 'error', 'error': e.message_dict}

        material.save()
        return {'status': 'ok'}

    @JSON_response
    @check_authorization
    @check_blacklist
    def delete(self, request):
        data = json.loads(request.body)
        material = Materials.objects.filter(id=int(data['id'])).first()
        if not material:
            return {'status': 'error', 'error': 'there is no such material'}

        if material.author != request.user and not request.user.groups.filter(name='admin').exists():
            return {'status': 'error', 'error': 'Permission denied'}

        material.delete()

        return {'status': 'ok'}


class SubjectsView(View):
    subjects = Subject.objects.all()

    @JSON_response
    def get(self, request):
        """params:
        fields=lecturers,term,programme
        lecturer :id
        term :int
        programme :id
        id :id
        """
        if request.GET.get("id"):
            self.subjects = self.subjects.filter(pk=request.GET.get("id"))
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
                except Programme.DoesNotExist:
                    return {'error': 'there are no such programme'}
            if is_term:
                output["terms"] = [{'term': term, 'subjects':
                    [subj.as_dict(lecturer=is_lecturers, programme=is_programme) for subj in self.subjects.filter(term=term)]}
                                   for term in range(1, 9)]
            else:
                output['subjects'] = [subj.as_dict(lecturer=is_lecturers, programme=is_programme)
                                      for subj in self.subjects]
            return output
        else:
            return {'error': 'there are no such subjects'}

    @JSON_response
    @check_authorization
    @check_blacklist
    def post(self, request):
        data = json.loads(request.body)
        data['programme'] = Programme.objects.filter(id=data['programme']).first()
        if not data['programme']:
            return {'status': 'error', 'error': 'there is no such programme'}

        data['term'] = int(data['term'])
        if data['term'] not in range(1, 9):
            return {'status': 'error', 'error': 'term should be between 1 and 8'}

        new_subject = Subject.objects.create(**data)
        try:
            new_subject.clean_fields()
        except ValidationError as e:
            return {'status': 'error', 'error': e.message_dict}

        return {'status': 'ok'}


class ProgrammeView(View):
    @JSON_response
    def get(self, request):
        """params: fields=img_url"""
        is_img_url = bool(request.GET.get('fields'))
        queryset = Programme.objects.all()
        output = dict()
        for degree in Programme.TypeOfDegrees.choices:
            output[degree[0]] = [obj.as_dict(img_url=is_img_url) for obj in queryset.filter(degree=degree[0])]
        return output
