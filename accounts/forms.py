from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django import forms
from django.forms import widgets
from .models import CustomUser
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    is_student = forms.BooleanField()
    USERNAME_FIELD = 'email'

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'password1', 'password2', 'is_student', 'is_staff')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_student'].required = False
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': "First name", 'autofocus':True})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': "Last name"})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': "name@example.com"})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': "Password"})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': "Retype password"})

    def clean(self):
        data = super().clean()
        student = data.get('is_student')
        staff = data.get('is_staff')
        if (not student and  not staff) or (student and staff):
            self.add_error('is_student', "You have to be student or lecturer or not both.")
            self.add_error('is_staff', "You have to be student or lecturer or not both.")


class ChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'password', 'is_student', 'is_staff')


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password',)

    def __init__(self, request, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': "Email"})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': "Passeord"})
