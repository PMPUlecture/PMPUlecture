from django.test import TestCase
from django.test.client import Client
import json

from main.models import Programme, Subject, Lecturer, Materials
from account.models import User


class SubjectTestCase(TestCase):
    def setUp(cls):
        Programme.objects.create(name="programme", degree="bachelor")
        User.objects.create_superuser("r@r.com", "password")

    def test_create_subject(self):
        c = Client()
        r = c.post('/api/subjects/', data=json.dumps({'programme': 1, 'term': 1, 'name': 'subject1'}),
                   content_type="application/json").json()
        self.assertDictEqual(r, {'status': 'error', 'error': 'Permission denied'}, msg='not auth')

        subjects = Subject.objects.filter(name='subject1').all()
        self.assertEqual(len(subjects), 0)


        c.login(email="r@r.com", password="password")

        r = c.post('/api/subjects/', data=json.dumps({'programme': 1, 'term': 1, 'name': 'subject1'}),
                   content_type="application/json").json()
        self.assertDictEqual(r, {'status': 'ok'}, msg='auth')

        subjects = Subject.objects.filter(name='subject1').all()
        programme = Programme.objects.get(id=1)
        self.assertEqual(len(subjects), 1)
        self.assertEqual(subjects[0].programme, programme)

    def test_trying_create_incorrect_subject(self):
        c = Client()
        c.login(email="r@r.com", password="password")
        r = c.post('/api/subjects/', data=json.dumps({'programme': 5, 'term': 1, 'name': 'subject1'}),
                   content_type="application/json").json()

        self.assertDictEqual(r, {'status': 'error', 'error': 'there is no such programme'}, msg="incorrect programme")
        subjects = Subject.objects.filter(name='subject1').all()
        self.assertEqual(len(subjects), 0)

        r = c.post('/api/subjects/', data=json.dumps({'programme': 1, 'term': 10, 'name': 'subject1'}),
                   content_type="application/json").json()
        self.assertDictEqual(r, {'status': 'error', 'error': 'term should be between 1 and 8'}, msg="incorrect term")
        subjects = Subject.objects.filter(name='subject1').all()
        self.assertEqual(len(subjects), 0)

class LecturerTestCase(TestCase):
    def setUp(self) -> None:
        programme = Programme.objects.create(name="programme", degree="bachelor")
        Subject.objects.create(name='subject1', term=1, programme=programme)
        Subject.objects.create(name='subject2', term=2, programme=programme)
        User.objects.create_superuser("r@r.com", "password")

    def test_create_leccturer(self):
        c = Client()
        r = c.post('/api/lecturers/', data=json.dumps({
            'name': 'lecturer',
            'subjects': [1, 2],
            'photo_url': 'https://picsum.photos/500',
            'apmath_url': 'https://apmath.ru',
            'vk_discuss_url': 'https://vk.com'
        }), content_type="application/json").json()
        self.assertDictEqual(r, {'status': 'error', 'error': 'Permission denied'}, msg='not auth')
        lecturers = Lecturer.objects.all()
        self.assertEqual(len(lecturers), 0, msg="not auth")

        c.login(email="r@r.com", password="password")
        r = c.post('/api/lecturers/', data=json.dumps({
            'name': 'lecturer',
            'subjects': [1, 2],
            'photo_url': 'https://picsum.photos/500',
            'apmath_url': 'https://apmath.ru',
            'vk_discuss_url': 'https://vk.com'
        }), content_type="application/json").json()
        self.assertDictEqual(r, {'status': 'ok'}, msg='auth')
        lecturers = Lecturer.objects.all()
        self.assertEqual(len(lecturers), 1, msg='auth')

    def test_create_incorrect_lecturers(self):
        c = Client()
        c.login(email="r@r.com", password="password")

        r = c.post('/api/lecturers/', data=json.dumps({
            'name': 'lecturer22',
            'subjects': [],
            'photo_url': 'https://picsum.photos/500',
            'apmath_url': 'https://apmath.ru',
            'vk_discuss_url': 'https://vk.com'
        }), content_type="application/json").json()
        self.assertDictEqual(r, {'status': 'error', 'error': 'there is no such subjects'}, msg='no subjects')
        lecturers = Lecturer.objects.all()
        self.assertEqual(len(lecturers), 0, msg='auth')

        r = c.post('/api/lecturers/', data=json.dumps({
            'name': 'lecturer',
            'subjects': [1, 2],
            'photo_url': 'picsumphotos/500',
            'apmath_url': 'https://apmath.ru',
            'vk_discuss_url': 'https://vk.com'
        }), content_type="application/json").json()
        self.assertEqual(r['status'], 'error', msg='invalid url')
        lecturers = Lecturer.objects.all()
        self.assertEqual(len(lecturers), 0, msg='invalid url')

        r = c.post('/api/lecturers/', data=json.dumps({
            'name': 'lecturer',
            'subjects': [],
            'photo_url': 'picsumphotos/500',
            'apmath_url': 'apmathu',
            'vk_discuss_url': 'vk.om'
        }), content_type="application/json").json()
        self.assertEqual(r['status'], 'error', msg='invalid url')
        lecturers = Lecturer.objects.all()
        self.assertEqual(len(lecturers), 0, msg='invalid url')

        r = c.post('/api/lecturers/', data=json.dumps({
            'name': 'lecturer22',
            'subjects': [4,6],
            'photo_url': 'https://picsum.photos/500',
            'apmath_url': 'https://apmath.ru',
            'vk_discuss_url': 'https://vk.com'
        }), content_type="application/json").json()
        self.assertDictEqual(r, {'status': 'error', 'error': 'there is no such subjects'}, msg='no subjects')
        lecturers = Lecturer.objects.all()
        self.assertEqual(len(lecturers), 0, msg='auth')