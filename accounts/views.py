from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, \
    PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

from .models import CustomUser


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "accounts/registration/register.html"

    def get_success_url(self) -> str:
        return reverse_lazy('accounts:login')


class LoginView(LoginView):
    form_class = LoginForm
    template_name = "accounts/registration/login.html"

    def get_success_url(self) -> str:
        return reverse_lazy('app:home')

# class ProfileView(LoginRequiredMixin, DetailView):
#     model = CustomUser
#     template_name = "accounts/profile.html"


class LogoutView(LogoutView):
    next_page = reverse_lazy("app:home")


class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    model = CustomUser
    template_name = "accounts/registration/password_change_form.html"

    def get_success_url(self) -> str:
        return reverse_lazy('app:home')

class PasswordResetView(PasswordResetView):
    model = CustomUser
    template_name = "accounts/registration/password_reset_form.html"

    def get_success_url(self) -> str:
        return reverse_lazy('app:home')

class PasswordResetConfirmView(PasswordResetConfirmView):
    model = CustomUser
    template_name = "accounts/registration/password_reset_confirm.html"

    def get_success_url(self) -> str:
        return reverse_lazy('app:home')

class PasswordChangeDoneView(PasswordChangeDoneView):
    next_page = reverse_lazy("app:home")

class PasswordResetDoneView(PasswordResetDoneView):
    next_page = reverse_lazy("app:home")

class PasswordResetCompleteView(PasswordResetCompleteView):
    next_page = reverse_lazy("app:home")
