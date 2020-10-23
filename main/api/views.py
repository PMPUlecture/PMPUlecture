from rest_framework import generics, views
from rest_framework.response import Response

from ..models import Programme, Subject, Lecturer
from .serializers import ProgrammeSerializer, SubjectSerializer, LecturerSerializer


class ProgListView(generics.ListAPIView):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer


class DetailLecturer(generics.RetrieveAPIView):
    serializer_class = LecturerSerializer
    queryset = Lecturer.objects.all()

    # Переопределяем функцию, показывающую подробные данные
    # по умолчанию выбирает объект с pk в пути /api/lecturer/<pk>/
    # теперь выбирает объект по url параметру /?pk=1
    def retrieve(self, request, *args, **kwargs):
        idLecturer = request.query_params['pk']
        return Response(self.serializer_class(Lecturer.objects.get(pk=idLecturer)).data)


class SubjectView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
