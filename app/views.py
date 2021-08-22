from django.db import models
from django.http.response import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.views.generic import CreateView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls.base import reverse_lazy
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Lecturer, Student, CustomUser, Course
from .forms import StudentChangeForm, LecturerChangeForm
from django.contrib.auth.decorators import login_required

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


class SearchResultsView(ListView):
    model = Course
    template_name = 'app/search.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('query')
        return Course.objects.filter(course_name__contains=query) | Course.objects.filter(description__contains=query)


@login_required
def course_reserve(request, pk):
    student = get_or_create(Student, student=request.user)
    student.enrolled.add(pk)
    return redirect('app:student-profile', pk=request.user.pk)


@login_required
def course_teach(request, pk):
    lecturer = get_or_create(Lecturer, lecturer=request.user)
    lecturer.taught.add(pk)
    return redirect('app:lecturer-profile', pk=request.user.pk)


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "app/details.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if self.request.user.is_staff:
    #         context['lecturer'] = get_or_create(Lecturer, lecturer=self.request.user)
    #         return context
    #     context['student'] = get_or_create(Student, student=self.request.user)
    #     return context



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
