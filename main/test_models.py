from django.test import TestCase

from main.models import Programme, Subject, Lecturer, Materials
from django.contrib.auth.models import AnonymousUser


class ProgrammeTestCase(TestCase):
    def setUp(self) -> None:
        prog1 = Programme.objects.create(name="First programme", degree="bachelor", img_url="https://picsum.photos/500")
        prog2 = Programme.objects.create(name="Second programme", degree="master", img_url="https://picsum.photos/500")
        s1 = Subject.objects.create(name="subject1", term=1, programme=prog1)
        s2 = Subject.objects.create(name="subject2", term=2, programme=prog2)
        lecturer1 = Lecturer.objects.create(name="Lecturer1", apmath_url="https://apmath.ru/1",
                                            vk_discuss_url="https://vk.com/1",
                                            photo_url="https://picsum.photos/200")
        lecturer1.subject.set([s1, s2])

        lecturer2 = Lecturer.objects.create(name="Lecturer2", apmath_url="https://apmath.ru/2",
                                            vk_discuss_url="https://vk.com/2",
                                            photo_url="https://picsum.photos/200")
        lecturer2.subject.set([s2])

        Materials.objects.create(name="Material1", type="abstract", subject=s1, lecturer=lecturer1,
                                 link="https://material.ru/1",
                                 year_of_relevance=2021)
        Materials.objects.create(name="Material2", type="abstract", subject=s2, lecturer=lecturer1,
                                 link="https://material.ru/2",
                                 year_of_relevance=2021)
        Materials.objects.create(name="Material3", type="questions", subject=s2, lecturer=lecturer2,
                                 link="https://material.ru/3",
                                 year_of_relevance=2020, only_authorized_users=True)

    def test_programme(self):
        programme = Programme.objects.get(name="First programme")
        self.assertEqual(programme.as_dict(), {"id": programme.id, "name": "First programme"})
        programme = Programme.objects.get(name="Second programme")
        self.assertEqual(programme.as_dict(img_url=True),
                         {"id": programme.id, "name": "Second programme", "img_url": "https://picsum.photos/500"})

    def test_subject(self):
        subj1 = Subject.objects.get(name="subject1")
        self.assertEqual(subj1.as_dict(), {"id": subj1.id, "name": "subject1"})
        self.assertEqual(subj1.as_dict(programme=True),
                         {"id": subj1.id, "name": "subject1", "programme": {
                             "id": 1, "name": "First programme"
                         }})
        subj2 = Subject.objects.get(name="subject2")
        self.assertEqual(subj2.as_dict(lecturer=True, programme=True),
                         {"id": subj2.id, "name": "subject2", "programme": {
                             "id": 2, "name": "Second programme"
                         },
                          "lecturers": [
                              {"id": 1, "name": "Lecturer1", 'the_rest_of_materials': 0},
                              {"id": 2, "name": "Lecturer2", 'the_rest_of_materials': 0}
                          ]})

    def test_lecturers(self):
        lecturer2 = Lecturer.objects.get(name="Lecturer2")
        self.assertEqual(lecturer2.as_dict(), {"id": lecturer2.id, "name": "Lecturer2", "the_rest_of_materials": 0})
        self.assertEqual(lecturer2.as_dict(subjects=True),
                         {"id": lecturer2.id, "name": "Lecturer2", "the_rest_of_materials": 0,
                          "subjects": [{"id": 2, "name": "subject2"}]})
        self.assertEqual(lecturer2.as_dict(apmath=True),
                         {"id": lecturer2.id, "name": "Lecturer2", "the_rest_of_materials": 0,
                          "apmath": "https://apmath.ru/2"})
        self.assertEqual(lecturer2.as_dict(vk=True),
                         {"id": lecturer2.id, "name": "Lecturer2", "the_rest_of_materials": 0,
                          "vk_discuss_url": "https://vk.com/2"})
        self.assertEqual(lecturer2.as_dict(subjects=True, vk=True, apmath=True),
                         {"id": lecturer2.id, "name": "Lecturer2", "the_rest_of_materials": 0,
                          "vk_discuss_url": "https://vk.com/2", "apmath": "https://apmath.ru/2",
                          "subjects": [{"id": 2, "name": "subject2"}]})\


    def test_lecturers_with_materials(self):
        lecturer1 = Lecturer.objects.get(name="Lecturer1")
        m1 = Materials.objects.get(name="Material1")
        m2 = Materials.objects.get(name="Material2")
        self.maxDiff = None

        self.assertEqual(lecturer1.as_dict(materials=True, author=AnonymousUser()),
                         {
                             "id": 1,
                             "name": "Lecturer1",
                             "the_rest_of_materials": 0,
                             "materials": [
                                 {
                                     "id_subject": 1,
                                     "name": "subject1",
                                     "source":
                                         [
                                             {"abstract": [m1.as_dict()],
                                              "questions": [],
                                              "test": [],
                                              "other": []},

                                         ]
                                 },
                                 {
                                     "id_subject": 2,
                                     "name": "subject2",
                                     "source":
                                         [
                                             {"abstract": [m2.as_dict()],
                                              "questions": [],
                                              "test": [],
                                              "other": []},

                                         ]
                                 }
                             ]
                         })


    def test_materials(self):
        m1 = Materials.objects.get(name="Material1")
        m3 = Materials.objects.get(name="Material3")
        self.assertEqual(m1.as_dict(), {
            'id': 1,
            'name': "Material1",
            'link': 'https://material.ru/1',
            'year_of_relevance': 2021,
            'only_authorized_users': False,
        })
        self.assertEqual(m3.as_dict(), {
            'id': 3,
            'name': "Material3",
            'link': 'https://material.ru/3',
            'year_of_relevance': 2020,
            'only_authorized_users': True,
        })