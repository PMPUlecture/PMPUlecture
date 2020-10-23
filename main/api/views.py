from rest_framework import generics, views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Programme, Subject, Lecturer
from .serializers import ProgrammeSerializer, SubjectSerializer, LecturerSerializer, LecturerStructSerializer


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
        return Response(self.serializer_class(self.queryset.get(pk=idLecturer)).data)


# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})

class ListUsers(views.APIView):
    queryset = Subject.objects.all()
    lecSer = LecturerStructSerializer
    subSer = SubjectSerializer

    def get(self, request):
        if request.query_params.get('programme'):
            programme = generics.get_object_or_404(Programme.objects.all(), name=request.query_params['programme'])
            res = Response([{'term': term, 'subjects':
                [self.subSer(subject).data for subject in self.queryset.filter(term=term, programme=programme)]} for
                            term in range(1, 9)])
        else:
            res = Response({'error': "No Such Programme"})
        res.setdefault('Access-Control-Allow-Origin', '*')
        return res
