from rest_framework import serializers
from ..models import Programme, Subject, Lecturer, Materials


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ('id', 'name', 'link')


class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = ('__all__')


# Серилизатор для метода структуры
class LecturerStructSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('id', 'name')


# Серилизатор для подробной инфы о преподе
class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('id', 'name', 'apmath_url', 'vk_discuss_url', 'photo_url')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['materials'] = dict()
        for item in Materials.TypeOfMaterial.choices: # tuple : ('for_backend', "For frontend")
            ret['materials'][item[0]] = \
                [MaterialSerializer(obj).data for obj in Materials.objects.filter(lecturer=instance, type=item[0])]
        return ret


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['lecturers'] = [LecturerStructSerializer(obj).data for obj in
                            Lecturer.objects.filter(subject=instance)]
        return ret
