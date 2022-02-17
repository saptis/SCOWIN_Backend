from django.contrib import admin

# Register your models here.
from .models import Student, StudentVaccination, Vaccine

admin.site.register(Student)
admin.site.register(StudentVaccination)
admin.site.register(Vaccine)
