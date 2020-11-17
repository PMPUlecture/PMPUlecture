from django.db import models


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


class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject, null=True)
    apmath_url = models.URLField(max_length=256, null=True)
    vk_discuss_url = models.URLField(max_length=256, null=True)
    photo_url = models.URLField(max_length=256, null=True)

    def as_dict(self, *, subjects: bool = False, apmath: bool = False, photo: bool = False,
                vk: bool = False,
                materials: bool = False):
        output = {
            'id': self.id,
            'name': self.name,
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
            all_materials = Materials.objects.filter(lecturer=self)
            output['materials'] = list()
            for subject in Subject.objects.filter(lecturer=self):
                output['materials'].append(
                    {subject.name: [
                        {type_of_material[0]: [material.as_dict() for material in
                                               all_materials.filter(type=type_of_material[0])]
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
    link = models.URLField(max_length=256, null=True)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'link': self.link,
        }
