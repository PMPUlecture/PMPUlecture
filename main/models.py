from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=100)


class lecturer(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'subject': {'name': self.subject.name, 'subject_id': self.subject.id}
        }

