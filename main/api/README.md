# Quick start в Django REST framework
Добавляем в файле settings.py
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_RENDERER_CLASSES': [ # выводить в JSON или красиво в браузере
        'rest_framework.renderers.JSONRenderer',  # на проде
        'rest_framework.renderers.BrowsableAPIRenderer'  # в дебаге
    ]
}
```

Для того, чтобы научить преобразовавать JSON в объекты и обратно - созать сеарилизаторы:
```python
# Серилизатор для подробной инфы о преподе
class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer # Модель, которую сериализуем
        fields = ('id', 'name', 'apmath_url', 'vk_discuss_url', 'photo_url') # Поля, которые будут включены в JSON

    def to_representation(self, instance): # Для сложных преобразований в JSON переопределяем этот метод
        ret = super().to_representation(instance)
        ret['materials'] = [MaterialSerializer(obj).data for obj in
                            Materials.objects.filter(lecturer=instance)]
        return ret

    # Если надо както сложно преобразовать JSON в объект - переопределяем .to_internal_value()
```
[подробнее](https://www.django-rest-framework.org/api-guide/serializers/)

## Вьюхи
На изи, вроде по стандарту понятно 
```python
class ProgListView(generics.ListAPIView):
    queryset = Programme.objects.all() # что показывать, откуда фильтровать, если надо
    serializer_class = ProgrammeSerializer
```
Также есть `generics.ListAPIView` - в виде списка
`generics.RetrieveAPIView` - одно конкретнее (см коментарии в views.py)
Можно ещё сделать чисто для создания или изменения
остальное [тут](https://www.django-rest-framework.org/api-guide/generic-views/#retrievemodelmixin)

## Урлы

Тоде изи, всё понятно
```python
urlpatterns = [
    url(r'^programme/$', views.ProgListView.as_view()),
    url(r'^subjects/$', views.SubjectView.as_view()),
    path('lecturer/', views.DetailLecturer.as_view()),
    ]
```