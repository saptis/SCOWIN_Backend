from rest_framework import serializers
from core.models import Vaccine, Student, StudentVaccination

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = (
            'id',
            'vaccinationDate',
            'vaccineName',
            'dosesAvailable',
            'slots',
            'driveApproval',
            'driveStatus'
        )
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id',
            'studentName',
            'dob',
            'gender',
            'grade',
            'section',
            'aadharID',
            'existingComorbidites',
            'bloodGroup'
        )
    
class StudentVaccinationSerializer(serializers.ModelSerializer):
    # student = serializers.PrimaryKeyRelatedField(
    #     many=True, 
    #     read_only=False
    # )

    # vaccine = serializers.PrimaryKeyRelatedField(
    #     many=True, 
    #     read_only=False
    # )
    # student = serializers.StudentSerializer()
    class Meta:
        model = StudentVaccination
        fields = (
            'id',
            'vaccinationDate',
            'dosage',
            'vaccinationStatus',
            'student',
            'vaccine'
        )
        