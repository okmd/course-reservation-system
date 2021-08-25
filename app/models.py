from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from accounts.models import CustomUser
# Create your models here.


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200)
    prerequisites = models.ManyToManyField("self", blank=True)
    description = models.TextField(blank=True)
    cover = models.ImageField(
        upload_to="courses", default="courses/default.png", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    course_fee = models.IntegerField(default=0)

    def __str__(self):
        return self.course_name

    class Meta:
        db_table = 'courses'


class Catalog(models.Model):
    catalog_id = models.AutoField(primary_key=True)
    catalog_name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.catalog_name


class BaseProfile(models.Model):
    street_address = models.CharField(max_length=100, default="Street Address")
    locality = models.CharField(max_length=100, default="Locality")
    district = models.CharField(max_length=20, default="District")
    state = models.CharField(max_length=20, default="State")
    pincode = models.IntegerField(default=000000)
    mobile_number = models.CharField(max_length=10, default="0000000000")
    profile_pic = models.ImageField(
        upload_to="profile_images", default="courses/default.png")

    class Meta:
        abstract = True


class Lecturer(BaseProfile):
    lecturer = models.OneToOneField(CustomUser, limit_choices_to={
                                    'is_staff': True}, on_delete=models.CASCADE, primary_key=True)
    taught = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.lecturer.email


class Student(BaseProfile):
    student = models.OneToOneField(CustomUser, limit_choices_to={
                                   'is_student': True}, on_delete=models.CASCADE, primary_key=True)
    enrolled = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.student.email


# class BaseInterface(models.Model):
#     course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
#     student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
#     lecturer_id = models.ForeignKey(Lecturer, on_delete=models.DO_NOTHING)
#     class Meta:
#         abstract=True
# class StudentClassStatus(models.TextChoices):
#     PRESENT = 'P'
#     ABSENT = 'A'
# class Attendance(BaseInterface):
#     status = models.CharField(choices=StudentClassStatus.choices, max_length=10)
#     class_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.course_id}-{self.student_id}-{self.lecturer_id}'

class StudentGradeChoices(models.TextChoices):
    A = 'A'
    B = 'B'
    C = 'C'
    F = 'F'
class Progress(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    lecturer_id = models.ForeignKey(Lecturer, on_delete=models.DO_NOTHING)
    progress = models.IntegerField(default=0)
    # certified = models.BooleanField(default=False)
    course_fee = models.IntegerField(default=0)
    grade = models.CharField(choices=StudentGradeChoices.choices, max_length=10, blank=True)
    completion_date = models.DateField(blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = (('course_id', 'student_id', 'lecturer_id'),)

    def __str__(self):
        return f'{self.course_id}-{self.student_id}-{self.lecturer_id}'
    
