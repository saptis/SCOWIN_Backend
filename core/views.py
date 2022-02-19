from pyexpat import model
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Vaccine, Student, StudentVaccination
from core.serializers import VaccineSerializer, StudentSerializer, StudentVaccinationSerializer
from rest_framework.response import Response

# Create your views here.

class VaccinationDrive(ListCreateAPIView):
    queryset = Vaccine.objects.all().order_by('-vaccinationDate')
    serializer_class = VaccineSerializer

class VaccinationDriveDetails(RetrieveUpdateDestroyAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer

class Students(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentsDetails(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentsVaccination(ListCreateAPIView):
    queryset = StudentVaccination.objects.all()
    serializer_class = StudentVaccinationSerializer

class StudentsVaccinationDetails(RetrieveUpdateDestroyAPIView):
    queryset = StudentVaccination.objects.all()
    serializer_class = StudentVaccinationSerializer

class StudentsVaccinationMetadata(ListCreateAPIView):

    def get(self, request):
        studentCount = Student.objects.all().count()
        vaccinatedStudentCount = StudentVaccination.objects.all().count()
        upcomingVaccinationDrive = Vaccine.objects.filter(driveStatus='Upcoming').values()
        return Response({'registeredStudentCount': studentCount, 'vaccinatedStudentCount': vaccinatedStudentCount, 'upcomingVaccinationDrive': upcomingVaccinationDrive})
