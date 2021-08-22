from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
    path('details/<pk>', views.CourseDetailView.as_view(), name='details'),
    path('reserve/<pk>', views.course_reserve, name='reserve'),
    path('teach/<pk>', views.course_teach, name='teach'),
    # path('student/profile/create', views.StudentCreateView.as_view(), name="student-profile-create"),
    # path('lecturer/profile/create', views.LecturerCreateteView.as_view(), name="lecturer-profile-create"),
    path('lecturer/profile/<pk>', views.LecturerView.as_view(), name="lecturer-profile"),
    path('lecturer/profile/<pk>', views.LecturerView.as_view(), name="lecturer-profile"),
    path('student/profile/<pk>', views.StudentView.as_view(), name="student-profile"),
    path('student/profile/update/<pk>', views.StudentUpdateView.as_view(), name="student-profile-update"),
    path('lecturer/profile/update/<pk>', views.LecturerUpdateView.as_view(), name="lecturer-profile-update")

]
