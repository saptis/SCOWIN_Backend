from pyexpat import model
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Vaccine, Student, StudentVaccination
from core.serializers import VaccineSerializer, StudentSerializer, StudentVaccinationSerializer

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
    queryset = StudentVaccination.objects.values()
    serializer_class = StudentVaccinationSerializer

class StudentsVaccinationDetails(RetrieveUpdateDestroyAPIView):
    queryset = StudentVaccination.objects.all()
    serializer_class = StudentVaccinationSerializer
