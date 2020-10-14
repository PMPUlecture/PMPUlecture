from django.contrib import admin
from .models import Subject, Lecturer, Programme, Materials

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'term', 'programme')
    list_filter = ('term', 'programme')
    fields = ['name', ('term', 'programme')]


class MaterialsInline(admin.TabularInline):
    model = Materials


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_subjects')

    fieldsets = (
        (None, {
            'fields': ('name', 'subject',)
        }),
        ('URLs', {
            'fields': ('photo_url', 'apmath_url', 'vk_discuss_url')
        }),
    )
    inlines = [MaterialsInline]


admin.site.register(Programme)

@admin.register(Materials)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'subject', 'lecturer')
    list_filter = ('type', 'subject', 'lecturer')


