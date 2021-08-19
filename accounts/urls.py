from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/',views.RegistrationView.as_view(), name="register"),
    path('login/',views.LoginView.as_view(), name="login"),
    path('logout/',views.LogoutView.as_view(), name="logout"),
    path('password_change/', views.PasswordChangeView.as_view(), name="password_change"),
    path('password_reset/', views.PasswordResetView.as_view(), name="password_reset")
]