from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lecturer, Student, CustomUser, Course

# Create your views here.


def home(request):
    return render(request, 'app/index.html')


def search(request):
    return render(request, 'app/search.html')

# @Required(LoginRequiredMixin)
def enroll(request, pk):
    return reverse("app:home")
    

class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "app/details.html"



class LecturerView(LoginRequiredMixin, DetailView):
    model = Lecturer
    template_name = "app/lecturer-profile.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['courses'] = Course.objects.all().filter()
    #     return context


class StudentView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "app/lecturer-profile.html"


class AdminView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "app/lecturer-profile.html"
