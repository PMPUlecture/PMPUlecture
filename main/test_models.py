from django.test import TestCase

from main.models import Programme, Subject, Lecturer, Materials

class ProgrammeTestCase(TestCase):
    def setUp(self) -> None:
        Programme.objects.create(name="First programme", degree="bachelor", img_url="https://picsum.photos/500")
        Programme.objects.create(name="Second programme", degree="bachelor", img_url="https://picsum.photos/500")
        Programme.objects.create(name="Third programme", degree="master", img_url="https://picsum.photos/500")


    def test_dict(self):
        programme = Programme.objects.get(name="First programme")
        self.assertEqual(programme.as_dict(), {"id": programme.id, "name": "First programme"})
        programme = Programme.objects.get(name="Second programme")
        self.assertEqual(programme.as_dict(img_url=True), {"id": programme.id, "name": "Second programme", "img_url": "https://picsum.photos/500"})
