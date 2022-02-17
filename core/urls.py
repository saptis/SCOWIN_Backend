from unicodedata import name
from django import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('vaccination-drive', VaccinationDrive.as_view()),
    path('vaccination-drive/<int:pk>', VaccinationDriveDetails.as_view()),
    path('students', Students.as_view()),
    path('students/<int:pk>', StudentsDetails.as_view()),
    path('student-vaccination', StudentsVaccination.as_view()),
    path('student-vaccination/<int:pk>', StudentsVaccinationDetails.as_view()),
]
