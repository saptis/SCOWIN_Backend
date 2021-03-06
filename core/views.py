from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        results = Student.objects.all()
        output_serializer = StudentSerializer(results, many=True)
        data = output_serializer.data[:]
        return Response(data)

class StudentsDetails(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentsVaccination(ListCreateAPIView):
    queryset = StudentVaccination.objects.all()
    serializer_class = StudentVaccinationSerializer

class StudentsVaccinationDetails(RetrieveUpdateDestroyAPIView):
    queryset = StudentVaccination.objects.all()
    serializer_class = StudentVaccinationSerializer

class StudentsVaccinationMetadata(ListAPIView):
    def list(self, request, *args, **kwargs):
        studentCount = Student.objects.all().count()
        vaccinatedStudentCount = StudentVaccination.objects.all().count()
        upcomingVaccinationDrive = Vaccine.objects.filter(driveStatus='Upcoming').values()

        out = {
            'registeredStudentCount': studentCount,
            'vaccinatedStudentCount': vaccinatedStudentCount,
            'upcomingVaccinationDrive': upcomingVaccinationDrive,
        }
        return Response(out)    
        
