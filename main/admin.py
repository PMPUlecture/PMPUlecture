from django.contrib import admin
from .models import Subject, Lecturer, Programme, Materials

# Register your models here.

admin.site.register(Subject)
admin.site.register(Lecturer)
admin.site.register(Programme)
admin.site.register(Materials)

