from django.test import TestCase
from django.test.client import Client

from main.models import Programme, Subject, Lecturer, Materials


def generate_test_database():
    prog1 = Programme.objects.create(name="First programme", degree="bachelor", img_url="https://picsum.photos/500")
    prog2 = Programme.objects.create(name="Second programme", degree="master", img_url="https://picsum.photos/500")
    s1 = Subject.objects.create(name="subject1", term=1, programme=prog1)
    s2 = Subject.objects.create(name="subject2", term=2, programme=prog2)
    s3 = Subject.objects.create(name="subject3", term=2, programme=prog2)
    s4 = Subject.objects.create(name="subject4", term=3, programme=prog2)
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


class ProgrammesApiTestCase(TestCase):
    def setUp(self) -> None:
        generate_test_database()

    def test_get_programmes(self):
        c = Client()
        r = c.get("/api/programmes/").json()
        self.assertDictEqual(r, {
            'bachelor':
                [
                    {
                        'id': 1,
                        'name': 'First programme'
                    }
                ],
            'master':
                [
                    {
                        'id': 2,
                        'name': 'Second programme'
                    }
                ]
        })

    def test_get_programmes_with_img(self):
        c = Client()
        r = c.get("/api/programmes/?fields=img_url").json()
        self.assertDictEqual(r, {
            'bachelor':
                [
                    {
                        'id': 1,
                        'name': 'First programme',
                        'img_url': 'https://picsum.photos/500'
                    }
                ],
            'master':
                [
                    {
                        'id': 2,
                        'name': 'Second programme',
                        'img_url': 'https://picsum.photos/500'
                    }
                ]
        })


class SubjectsApiTestCase(TestCase):
    def setUp(self) -> None:
        generate_test_database()

    def test_get_subjects(self):
        c = Client()
        r = c.get("/api/subjects/").json()
        self.assertDictEqual(r, {'subjects':
            [
                {
                    'id': 1,
                    'name': 'subject1'
                },
                {
                    'id': 2,
                    'name': 'subject2'
                },
                {
                    'id': 3,
                    'name': 'subject3'
                },
                {
                    'id': 4,
                    'name': 'subject4'
                },

            ]}, msg="$ without fields $")

    def test_get_subjects_with_lecturers(self):
        c = Client()
        r = c.get("/api/subjects/?fields=lecturers").json()
        self.assertDictEqual(r, {'subjects':
            [
                {
                    'id': 1,
                    'name': 'subject1',
                    'lecturers':
                        [
                            {
                                'id': 1,
                                'name': 'Lecturer1',
                                'the_rest_of_materials': 0
                            }
                        ]
                },
                {
                    'id': 2,
                    'name': 'subject2',
                    'lecturers':
                        [
                            {
                                'id': 1,
                                'name': 'Lecturer1',
                                'the_rest_of_materials': 0
                            },
                            {
                                'id': 2,
                                'name': 'Lecturer2',
                                'the_rest_of_materials': 0
                            },
                        ]
                },
                {
                    'id': 3,
                    'name': 'subject3',
                    'lecturers': []
                },
                {
                    'id': 4,
                    'name': 'subject4',
                    'lecturers': []
                },

            ]}, msg="fields=lecturers")

    def test_get_subjects_with_programme(self):
        c = Client()
        r = c.get("/api/subjects/?fields=programme").json()
        self.assertDictEqual(r, {'subjects':
            [
                {
                    'id': 1,
                    'name': 'subject1',
                    'programme':
                        {
                            'id': 1,
                            'name': "First programme"
                        }
                },
                {
                    'id': 2,
                    'name': 'subject2',
                    'programme':
                        {
                            'id': 2,
                            'name': "Second programme"
                        }
                },
                {
                    'id': 3,
                    'name': 'subject3',
                    'programme':
                        {
                            'id': 2,
                            'name': "Second programme"
                        }
                },
                {
                    'id': 4,
                    'name': 'subject4',
                    'programme':
                        {
                            'id': 2,
                            'name': "Second programme"
                        }
                },

            ]}, msg='fields=programme'),

    def test_get_subjects_with_terms(self):
        c = Client()
        r = c.get("/api/subjects/?fields=term").json()
        self.assertDictEqual(r, {'terms':
            [
                {
                    'term': 1,
                    'subjects':
                        [
                            {
                                'id': 1,
                                'name': 'subject1'
                            }
                        ]
                },
                {
                    'term': 2,
                    'subjects':
                        [
                            {
                                'id': 2,
                                'name': 'subject2'
                            },
                            {
                                'id': 3,
                                'name': 'subject3'
                            }
                        ]
                },
                {
                    'term': 3,
                    'subjects': [
                        {
                            'id': 4,
                            'name': 'subject4'
                        }
                    ]
                },
                {
                    'term': 4, 'subjects': []
                },
                {
                    'term': 5, 'subjects': []
                },
                {
                    'term': 6, 'subjects': []
                },
                {
                    'term': 7, 'subjects': []
                },
                {
                    'term': 8, 'subjects': []
                }
            ]}, msg='fields=term')

    def test_get_subjects_with_all(self):
        c = Client()
        r = c.get("/api/subjects/?fields=lecturers,term,programme").json()
        self.assertDictEqual(r, {'terms':
            [
                {
                    'term': 1,
                    'subjects':
                        [
                            {
                                'id': 1,
                                'name': 'subject1',
                                'programme':
                                    {
                                        'id': 1,
                                        'name': "First programme"
                                    },
                                'lecturers':
                                    [
                                        {
                                            'id': 1,
                                            'name': 'Lecturer1',
                                            'the_rest_of_materials': 0
                                        }
                                    ]
                            }
                        ]
                },
                {
                    'term': 2,
                    'subjects':
                        [
                            {
                                'id': 2,
                                'name': 'subject2',
                                'programme':
                                    {
                                        'id': 2,
                                        'name': "Second programme"
                                    },
                                'lecturers':
                                    [
                                        {
                                            'id': 1,
                                            'name': 'Lecturer1',
                                            'the_rest_of_materials': 0
                                        },
                                        {
                                            'id': 2,
                                            'name': 'Lecturer2',
                                            'the_rest_of_materials': 0
                                        },
                                    ]
                            },
                            {
                                'id': 3,
                                'name': 'subject3',
                                'programme':
                                    {
                                        'id': 2,
                                        'name': "Second programme"
                                    },
                                'lecturers': []
                            }
                        ]
                },
                {
                    'term': 3,
                    'subjects': [
                        {
                            'id': 4,
                            'name': 'subject4',
                            'programme':
                                {
                                    'id': 2,
                                    'name': "Second programme"
                                },
                            'lecturers': []
                        }
                    ]
                },
                {
                    'term': 4, 'subjects': []
                },
                {
                    'term': 5, 'subjects': []
                },
                {
                    'term': 6, 'subjects': []
                },
                {
                    'term': 7, 'subjects': []
                },
                {
                    'term': 8, 'subjects': []
                }
            ]}, msg='fields=lecturers,term,programme')

    def test_get_subjects_by_parameter(self):
        c = Client()
        r = c.get("/api/subjects/?id=1").json()
        self.assertDictEqual(r, {
            'subjects':
                [
                    {
                        'id': 1,
                        'name': 'subject1'
                    },
                ]
        }, msg='by id')

        r = c.get("/api/subjects/?lecturer=1").json()
        self.assertDictEqual(r, {
            'subjects':
                [
                    {
                        'id': 1,
                        'name': 'subject1'
                    },
                    {
                        'id': 2,
                        'name': 'subject2'
                    }
                ]
        }, msg='by lecturer')

        r = c.get("/api/subjects/?term=3").json()
        self.assertDictEqual(r, {
            'subjects':
                [
                    {
                        'id': 4,
                        'name': 'subject4'
                    },
                ]
        }, msg='by term')

        r = c.get("/api/subjects/?programme=1").json()
        self.assertDictEqual(r, {
            'programme': "First programme",
            'subjects':
                [
                    {
                        'id': 1,
                        'name': 'subject1'
                    },
                ]
        }, msg='by programme')


class LecturerApiTestCase(TestCase):
    def setUp(self) -> None:
        generate_test_database()

    def test_get_lecturers(self):
        c = Client()
        r = c.get("/api/lecturers/").json()
        self.assertListEqual(r, [
            {
                'id': 1,
                'name': "Lecturer1",
                "the_rest_of_materials": 0
            },
            {
                'id': 2,
                'name': "Lecturer2",
                "the_rest_of_materials": 0
            },
        ])

    def test_get_lecturers_with_subjects(self):
        c = Client()
        r = c.get("/api/lecturers/?fields=subjects").json()
        self.assertListEqual(r, [
            {
                'id': 1,
                'name': "Lecturer1",
                "the_rest_of_materials": 0,
                'subjects':
                    [
                        {
                            'id': 1,
                            'name': 'subject1'
                        },
                        {
                            'id': 2,
                            'name': 'subject2'
                        }
                    ]
            },
            {
                'id': 2,
                'name': "Lecturer2",
                "the_rest_of_materials": 0,
                'subjects':
                [
                    {
                        'id': 2,
                        'name': 'subject2'
                    }
                ]
            },
        ])

    def test_get_lecturers_with_materials(self):
        c = Client()
        r = c.get("/api/lecturers/?fields=materials").json()
        self.assertListEqual(r, [
            {
                'id': 1,
                'name': "Lecturer1",
                "the_rest_of_materials": 0,
                'materials':
                [
                    {
                        'id_subject': 1,
                        'name': 'subject1',
                        'source':
                        [
                            {
                                'abstract':
                                [
                                    {
                                        "id": 1,
                                        "name": "Material1",
                                        "link": "https://material.ru/1",
                                        "year_of_relevance": 2021,
                                        "only_authorized_users": False
                                    }
                                ],
                                'questions': [],
                                'test': [],
                                'other': []
                            }
                        ]
                    },
                    {
                        'id_subject': 2,
                        'name': 'subject2',
                        'source':
                            [
                                {
                                    'abstract':
                                        [
                                            {
                                                "id": 2,
                                                "name": "Material2",
                                                "link": "https://material.ru/2",
                                                "year_of_relevance": 2021,
                                                "only_authorized_users": False
                                            }
                                        ],
                                    'questions': [],
                                    'test': [],
                                    'other': []
                                }
                            ]
                    }
                ]
            },
            {
                'id': 2,
                'name': "Lecturer2",
                "the_rest_of_materials": 0,
                'materials': [
                    {
                        'id_subject': 2,
                        'name': 'subject2',
                        'source':
                            [
                                {
                                    'abstract': [],
                                    'questions': [],
                                    'test': [],
                                    'other': []
                                }
                            ]
                    }
                ]
            },
        ])

    def test_get_lecturers_with_apmath_photo_vk(self):
        c = Client()
        r = c.get("/api/lecturers/?fields=apmath,photo,vk").json()
        self.assertListEqual(r, [
            {
                'id': 1,
                'name': "Lecturer1",
                "the_rest_of_materials": 0,
                'apmath': "https://apmath.ru/1",
                'vk_discuss_url': "https://vk.com/1",
                'photo': "https://picsum.photos/200"
            },
            {
                'id': 2,
                'name': "Lecturer2",
                "the_rest_of_materials": 0,
                'apmath': "https://apmath.ru/2",
                'vk_discuss_url': "https://vk.com/2",
                'photo': "https://picsum.photos/200"
            },
        ])

    def test_get_lecturers_by_id(self):
        c = Client()
        r = c.get("/api/lecturers/?id=1").json()
        self.assertListEqual(r, [
            {
                'id': 1,
                'name': "Lecturer1",
                "the_rest_of_materials": 0
            }
        ])

    def test_get_lecturers_by_name(self):
        c = Client()
        r = c.get("/api/lecturers/?name=er2").json()
        self.assertListEqual(r, [
            {
                'id': 2,
                'name': "Lecturer2",
                "the_rest_of_materials": 0
            }
        ])

    def test_get_lecturers_by_subject(self):
        c = Client()
        r = c.get("/api/lecturers/?subject=1").json()
        self.assertListEqual(r, [
            {
                'id': 1,
                'name': "Lecturer1",
                "the_rest_of_materials": 0
            }
        ])

    def test_get_lecturers_with_materials_by_subject(self):
        """Материалы преподавателей по конкретному предмету"""
        c = Client()
        r = c.get("/api/lecturers/?id_subject_for_material=2&fields=materials").json()
        self.assertListEqual(r, [
            {
                'id': 1,
                'name': "Lecturer1",
                "the_rest_of_materials": 1,
                'materials':
                    [
                        {
                            'id_subject': 2,
                            'name': 'subject2',
                            'source':
                                [
                                    {
                                        'abstract':
                                            [
                                                {
                                                    "id": 2,
                                                    "name": "Material2",
                                                    "link": "https://material.ru/2",
                                                    "year_of_relevance": 2021,
                                                    "only_authorized_users": False
                                                }
                                            ],
                                        'questions': [],
                                        'test': [],
                                        'other': []
                                    }
                                ]
                        }
                    ]
            },
            {
                'id': 2,
                'name': "Lecturer2",
                "the_rest_of_materials": 0,
                'materials': [
                    {
                        'id_subject': 2,
                        'name': 'subject2',
                        'source':
                            [
                                {
                                    'abstract': [],
                                    'questions': [],
                                    'test': [],
                                    'other': []
                                }
                            ]
                    }
                ]
            },
        ])

