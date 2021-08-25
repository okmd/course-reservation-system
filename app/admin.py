from django.contrib import admin
from django.db.models import fields
from .models import Course, Lecturer, Student, Catalog, Progress
# Register your models here.


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    fields = ['catalog_name','courses']
    list_display = ['catalog_name','created_at', 'updated_at']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ['course_name', 'prerequisites','description', 'course_fee', 'cover']
    list_display = ['course_name','course_fee','created_at' ,'updated_at','cover']

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    fields = ['taught','lecturer', 'street_address', 'locality', 'district','state', 'pincode', 'mobile_number', 'profile_pic']
    list_display = ['lecturer', 'street_address', 'locality', 'district','state', 'pincode', 'mobile_number', 'profile_pic']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ['enrolled','student','street_address', 'locality', 'district','state', 'pincode', 'mobile_number', 'profile_pic']
    list_display = ['student', 'street_address', 'locality', 'district','state', 'pincode', 'mobile_number', 'profile_pic']

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    fields = ['course_id','student_id','lecturer_id',  'progress', 'grade','course_fee', 'completion_date']
    list_display = ['course_id', 'student_id', 'lecturer_id', 'progress', 'grade','course_fee', 'completion_date', 'enrollment_date']

# @admin.register(Attendance)
# class AttendanceAdmin(admin.ModelAdmin):
#     fields = ['course_id','student_id','lecturer_id', 'status']
#     list_display = ['course_id', 'student_id', 'lecturer_id', 'status', 'class_date']