from django.contrib import admin
from .models import Course, Lecturer, Student, Catalog
# Register your models here.


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    fields = ['catalog_name','courses']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # fields = ['course_name', 'prerequisites']
    pass

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    fields = ['taught','lecturer', 'street_address', 'locality', 'district','state', 'pincode', 'mobile_number', 'profile_pic']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ['enrolled','student','street_address', 'locality', 'district','state', 'pincode', 'mobile_number', 'profile_pic']