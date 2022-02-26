"""
Creating all models related to core here
"""
from django.db import models

# Create your models here.

class Student(models.Model):
    """
    Student model added here
    """
    id = models.CharField(primary_key=True, max_length=4)
    studentName = models.CharField(max_length=32)
    dob = models.DateTimeField()
    #dob = models.DateField()
    gender = models.CharField(max_length=32)
    grade = models.CharField(max_length=2)
    section = models.CharField(max_length=1)
    aadharID = models.CharField(max_length=12)
    existingComorbidites = models.CharField(max_length=300, null=True, blank=True)
    bloodGroup = models.CharField(max_length=3)

    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """

    def __str__(self):
        return "{}".format(self.studentName)

class Vaccine(models.Model):
    """
    Student model added here
    """
    vaccinationDate = models.DateTimeField()
    vaccineName = models.CharField(max_length=32)
    dosesAvailable = models.PositiveIntegerField(default=100)
    slots = models.PositiveIntegerField(default=10)
    driveApproval = models.CharField(max_length=32)
    driveStatus = models.CharField(max_length=32)

    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """

    def __str__(self):
        return "{}".format(self.vaccineName)

class StudentVaccination(models.Model):
    """
    Student model added here
    """
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name="student")
    vaccinationDate = models.DateTimeField()
    #vaccinationDate = models.DateField()
    dosage = models.PositiveIntegerField(default=1)
    vaccinationStatus = models.CharField(max_length=32)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.DO_NOTHING, related_name="vaccine")

    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """

    def __str__(self):
        return "{}".format(self.student)
