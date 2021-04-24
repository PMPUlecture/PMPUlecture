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

