from django.db import models

# Create your models here.


class Programme(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.URLField(max_length=256)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    programme = models.ForeignKey(Programme, on_delete=models.SET_NULL, null=True)
    term = models.IntegerField(null=True)


class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject, null=True)
    apmath_url = models.URLField(max_length=256, null=True)
    vk_discuss_url = models.URLField(max_length=256, null=True)
    photo_url = models.URLField(max_length=256, null=True)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'subject': [{'name': item.id, 'subject_id': item.name} for item in self.subject.all()]
        }


class Materials(models.Model):
    class TypeOfMaterial(models.TextChoices):
        ABSTRACT = ("abstract", "конспект")
        QUESTIONS = ("questions", "вопросы")
        TEST = ("test", "контрльная")
    type = models.CharField(max_length=16, choices=TypeOfMaterial.choices)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    link = models.URLField(max_length=256, null=True)
    name = models.CharField(max_length=256, null=True)
