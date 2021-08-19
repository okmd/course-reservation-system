from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('details/<pk>', views.CourseDetailView.as_view(), name='details'),
    path('enroll/<pk>', views.enroll, name='enroll'),
    path('teacher/profile/<pk>', views.LecturerView.as_view(), name="lecturer-profile"),
    path('student/profile/<pk>', views.StudentView.as_view(), name="student-profile"),
    path('admin/profile/<pk>', views.AdminView.as_view(), name="admin-profile")

]
