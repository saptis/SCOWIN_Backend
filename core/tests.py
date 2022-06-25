from sqlite3 import Date
from django.test import Client, TestCase
from core.models import Student
from django.urls import reverse
from rest_framework import status
from core.serializers import StudentSerializer

client = Client()

class TestCases(TestCase):

    def setUp(self):
        Student.objects.create(
        id = 1200,
        studentName='Huckle',
        dob= Date.today(),
        gender='Male',
        grade='9',
        section='B',
        aadharID='345223345543',
        bloodGroup='A+'
        )

        # payload = {
        # 'id=1200,
        # 'studentName='Huckle',
        # 'dob=Date.today(),
        # 'gender='Male',
        # 'grade='9',
        # 'section='B',
        # 'aadharId='345223345543',
        # 'bloodGroup='A+'
        # }
        # factory = APIRequestFactory()
        # response = factory.post('http://testserver/students/', payload, format='json')
        # assert response.status_code == 200

    def test_get_all_students(self):
        # get API response
        response = client.get('http://testserver/students')
        # get data from db
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        # self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
