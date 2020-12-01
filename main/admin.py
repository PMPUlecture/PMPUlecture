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


class TermListFilter(admin.SimpleListFilter):
    title = 'term'

    parameter_name = 'term'

    def lookups(self, request, model_admin):
        return (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
        )

    def queryset(self, request, queryset):
        if not self.value():
            return Lecturer.objects.all()

        return Lecturer.objects.filter(subject__term=int(self.value())).distinct()


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_subjects')
    list_filter = ('subject', TermListFilter)

    fieldsets = (
        (None, {
            'fields': ('name', 'subject',)
        }),
        ('URLs', {
            'fields': ('photo_url', 'apmath_url', 'vk_discuss_url')
        }),
    )
    inlines = [MaterialsInline]


@admin.register(Programme)
class PregrammeAdmin(admin.ModelAdmin):
    list_display = ['name', 'degree']

@admin.register(Materials)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'subject', 'lecturer')
    list_filter = ('type', 'subject', 'lecturer', 'last_update')
