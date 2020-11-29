from rest_framework import viewsets
from school.models import Student
from school.serializer import StudentSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
