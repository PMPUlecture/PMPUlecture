from django.db import models

# Create your models here.


class Programme(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.URLField(max_length=256)

    def __str__(self):
        return self.name

    def as_dict(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    programme = models.ForeignKey(Programme, on_delete=models.SET_NULL, null=True)
    term = models.IntegerField(null=True)

    def __str__(self):
        return self.name + ' (' + str(self.term) + ')'

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'term': self.term,
        }


class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject, null=True)
    apmath_url = models.URLField(max_length=256, null=True)
    vk_discuss_url = models.URLField(max_length=256, null=True)
    photo_url = models.URLField(max_length=256, null=True)

    def as_dict(self, *args, apmath=False, photo=False, vk_discuss=False):
        dicte = {
            'id': self.id,
            'name': self.name,
            'subjects': [item.as_dict() for item in self.subject.all()]
        }
        if apmath:
            dicte['apmath'] = self.apmath_url
        if photo:
            dicte['photo'] = self.photo_url
        if vk_discuss:
            dicte['vk_discuss_url'] = self.vk_discuss_url
        return dicte

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
    name = models.CharField(max_length=256, null=True)
    type = models.CharField(max_length=16, choices=TypeOfMaterial.choices)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True)
    link = models.URLField(max_length=256, null=True)


    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            'name': self.name,
            'type': self.type,
            'subject': self.subject,
            'lecturer': self.lecturer,
            'url': self.link
        }