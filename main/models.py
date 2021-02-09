from django.core.validators import URLValidator
from django.db import models
from account.models import User

from datetime import datetime


class Programme(models.Model):
    class TypeOfDegrees(models.TextChoices):
        BACHELOR = ("bachelor", "Бакалавриат")
        MASTER = ("master", "Магистратура")

    name = models.CharField(max_length=100, unique=True)
    img_url = models.URLField(max_length=256)
    degree = models.CharField(max_length=16, choices=TypeOfDegrees.choices)

    def __str__(self):
        return self.name

    def as_dict(self, *, img_url: bool = False):
        output = {'id': self.pk,
                  'name': self.name,
                  }
        if img_url:
            output['img_url'] = self.img_url
        return output


class Subject(models.Model):
    name = models.CharField(max_length=100)
    programme = models.ForeignKey(Programme, on_delete=models.SET_NULL, null=True)
    term = models.IntegerField(null=True)

    def __str__(self):
        return self.name + ' (' + str(self.term) + ')'

    def as_dict(self, lecturer: bool = False, programme: bool = False):
        output = {
            'id': self.id,
            'name': self.name,
        }
        if lecturer:
            output['lecturers'] = [lector.as_dict() for lector in Lecturer.objects.filter(subject=self)]
        if programme:
            output['programme'] = self.programme.as_dict()
        return output


class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject, null=True, blank=True)
    apmath_url = models.URLField(max_length=256, null=True)
    vk_discuss_url = models.URLField(max_length=256, null=True, blank=True)
    photo_url = models.URLField(max_length=256, default='https://sun9-68.userapi.com/impf/HyenmwTQQ1fWW0OszQm_mih7lYpbLZ0NxveoJQ/NEYM96WpZVw.jpg?size=512x512&quality=96&proxy=1&sign=62af85c2f2a71ab9252ea738532a87be')

    def as_dict(self, *, subjects: bool = False, apmath: bool = False, photo: bool = False,
                vk: bool = False,
                materials: bool = False, id_subject_for_material: int = None, author=None):
        output = {
            'id': self.id,
            'name': self.name,
            'the_rest_of_materials': 0,
        }
        if subjects:
            output['subjects'] = [item.as_dict() for item in self.subject.all()]
        if apmath:
            output['apmath'] = self.apmath_url
        if photo:
            output['photo'] = self.photo_url
        if vk:
            output['vk_discuss_url'] = self.vk_discuss_url
        if materials:
            all_materials = Materials.objects.filter(lecturer=self).order_by('year_of_relevance').reverse()

            if author.is_anonymous:
                all_materials = all_materials.filter(only_authorized_users=False)

            output['materials'] = list()
            if id_subject_for_material:
                subjects = Subject.objects.filter(lecturer=self, id=id_subject_for_material)
                output['the_rest_of_materials'] = Materials.objects.filter(lecturer=self).exclude(subject=subjects.first()).count()
            else:
                subjects = Subject.objects.filter(lecturer=self)
            for subject in subjects:
                output['materials'].append(
                    {
                        "id_subject": subject.id, "name": subject.name, "source": [
                        {type_of_material[0]: [material.as_dict(author) for material in
                                               all_materials.filter(subject=subject, type=type_of_material[0])]
                         for type_of_material in Materials.TypeOfMaterial.choices}]
                    }
                )
        return output

    def __str__(self):
        return self.name

    def display_subjects(self):
        return ', '.join([subjects.__str__() for subjects in self.subject.all()[:3]])

    display_subjects.short_description = 'Subjects'


class Materials(models.Model):
    class TypeOfMaterial(models.TextChoices):
        ABSTRACT = ("abstract", "конспект")
        QUESTIONS = ("questions", "вопросы")
        TEST = ("test", "контрльная")
        OTHER = ("other", "разное")

    name = models.CharField(max_length=256, null=True)
    type = models.CharField(max_length=16, choices=TypeOfMaterial.choices)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True)
    link = models.URLField(max_length=256, null=True, validators=[URLValidator,])
    author = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, null=True)
    last_update = models.DateTimeField(auto_now=True)
    year_of_relevance = models.IntegerField(default=datetime.now().year)
    only_authorized_users = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def as_dict(self, author=None):
        output = {
            'id': self.id,
            'name': self.name,
            'link': self.link,
            'year_of_relevance': self.year_of_relevance,
            'only_authorized_users': self.only_authorized_users,
        }
        if author:
            if author == self.author or author.groups.filter(name='admin').exists():
                output['is_author'] = True
        return output
