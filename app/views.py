from django.db import models
from django.http.response import FileResponse, Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.views.generic import CreateView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls.base import reverse_lazy
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Lecturer, Student, CustomUser, Course, Progress
from .forms import StudentChangeForm, LecturerChangeForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from datetime import date

# Create your views here.


def get_or_create(model_class, **kwargs):
    try:
        return model_class.objects.get(**kwargs)
    except model_class.DoesNotExist:
        record = model_class.objects.create(**kwargs)
        record.save()
        return record


def home(request):
    return render(request, 'app/index.html')


@login_required
def progress(request):
    # visible for both student and lecturer
    # lecturer can edit progress.
    context = {}
    if request.user.is_staff:

        objects = Progress.objects.filter(lecturer_id=request.user.id)
        courses = set()
        for prog in objects:
            courses.add(prog.course_id)

        course_details = []
        for cname in courses:
            count = objects.filter(course_id=cname.course_id).values(
                'course_id').count()
            earning = objects.filter(course_id=cname.course_id).aggregate(
                Sum('course_fee'))['course_fee__sum']
            course_details.append({"count": count, "earning": earning})

        context['progress'] = zip(courses, course_details)

    else:
        context['progress'] = Progress.objects.filter(
            student_id=request.user.id)

    return render(request, 'app/progress.html', context)

# def attendance(request):
#     return render(request, 'app/attendance.html')


@login_required
def certificate_generation(request, cid, lid):

    buffer = io.BytesIO()
    canv = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    textob = canv.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    student_name = f"{request.user.first_name} {request.user.last_name}"
    progress_obj = Progress.objects.get(
        course_id=cid, lecturer_id=lid, student_id=request.user.pk)
    message = [
        "~~~~~~~~~~~~~~~~~~~~~~ CERTIFICATE ~~~~~~~~~~~~~~~~~~~~~~",
        " ",
        f"Congarulations!, {student_name}".center(100),
        " ",
        "This is certify that".center(110),
        f"{student_name}".center(110),
        "has successfully completed".center(100),
        f"{progress_obj.course_id}".center(100),
        f"with Grade {progress_obj.grade}".center(110),
        " ",
        f"Enrolled on {progress_obj.enrollment_date.strftime('%B %d, %Y')} and completed on {progress_obj.completion_date.strftime('%B %d, %Y')}.",
        " ",
        "Thanks for enrolling in this course.",
        " ",
        "Lecturer,",
        f"{progress_obj.lecturer_id.lecturer.first_name} {progress_obj.lecturer_id.lecturer.last_name}",
        "Thank you."
        " ",
        " ",
        " ",
        f"Certificate generated on - {date.today().strftime('%A %B %d, %Y')}".center(85)

    ]

    for line in message:
        textob.textLine(line)
    canv.drawText(textob)
    # canv.showPage()
    canv.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename="certificate.pdf")


def SearchResultsView(request):
    query = request.GET.get('query')
    if request.user.is_staff:
        objects = Course.objects.filter(
            course_name__contains=query) | Course.objects.filter(description__contains=query)
        courses = objects  # to check view not remove
    else:
        faculties = Lecturer.objects.all()
        courses = Course.objects.none()
        aligned_faculties = []
        for faculty in faculties:
            my_courses = faculty.taught.all()
            temp = my_courses.filter(course_name__contains=query) | my_courses.filter(
                description__contains=query)
            courses = courses | temp

            for _ in range(len(temp)):
                aligned_faculties.append(
                    (faculty.pk, faculty.lecturer.first_name, faculty.lecturer.last_name))

        objects = zip(courses, aligned_faculties)

    return render(request, "app/search.html", {"courses": objects, 'count': len(courses)})


@login_required
def course_reserve(request, cid, lid):
    student = get_or_create(Student, student=request.user)
    student.enrolled.add(cid)
    course = Course.objects.get(course_id=cid)
    lecturer = Lecturer.objects.get(lecturer=lid)
    try:
        Progress.objects.create(student_id=student, lecturer_id=lecturer,
                            course_id=course, course_fee=course.course_fee)
    except Exception as e:
        print(e)
    return redirect('app:student-profile', pk=request.user.pk)


@login_required
def course_teach(request, pk):
    lecturer = get_or_create(Lecturer, lecturer=request.user)
    lecturer.taught.add(pk)
    return redirect('app:lecturer-profile', pk=request.user.pk)


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "app/details.html"


class LecturerView(LoginRequiredMixin, DetailView):
    model = Lecturer
    template_name = "app/profile.html"

    def get_object(self, queryset=None):
        return get_or_create(Lecturer, lecturer=self.request.user)


class StudentView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "app/profile.html"

    def get_object(self, queryset=None):
        return get_or_create(Student, student=self.request.user)


class AdminView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "app/profile.html"


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    form_class = StudentChangeForm
    template_name = "app/update-profile.html"

    def get_queryset(self):
        return Student.objects.filter(student=self.request.user.id)
        # return super().get_queryset()

    def get_success_url(self):
        return reverse_lazy('app:home')


class LecturerUpdateView(LoginRequiredMixin, UpdateView):
    form_class = LecturerChangeForm
    template_name = "app/update-profile.html"

    def get_queryset(self):
        return Lecturer.objects.filter(lecturer=self.request.user.id)
        # return super().get_queryset()

    def get_success_url(self):
        return reverse_lazy('app:home')


# class StudentCreateView(CreateView):
#     form_class = StudentCreationForm
#     template_name = "app/create-profile.html"

#     def get_success_url(self):
#         return reverse_lazy('app:home')

# class LecturerCreateteView(CreateView):
#     form_class = LecturerCreationForm
#     template_name = "app/create-profile.html"

#     def get_success_url(self):
#         return reverse_lazy('app:home')
