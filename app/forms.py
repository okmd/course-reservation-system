from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Lecturer, Student
from django import forms

def helper(self):
    self.fields['street_address'].widget.attrs.update(
        {'class': 'form-control', })
    self.fields['locality'].widget.attrs.update(
        {'class': 'form-control', })
    self.fields['district'].widget.attrs.update(
        {'class': 'form-control', })
    self.fields['state'].widget.attrs.update({'class': 'form-control', })
    self.fields['profile_pic'].widget.attrs.update(
        {'class': 'form-control'})
    self.fields['mobile_number'].widget.attrs.update(
        {'class': 'form-control'})
    self.fields['wallet'].widget.attrs.update(
        {'class': 'form-control'})
    self.fields['pincode'].widget.attrs.update({'class': 'form-control'})
    return self

class StudentChangeForm(UserChangeForm):
    class Meta:
        model = Student
        fields = ('student', 'street_address', 'locality', 'district', 'state',
                  'pincode', 'mobile_number','wallet', 'profile_pic')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].widget.attrs.update(
            {'class': 'form-control', 'hidden': 'hidden'})
        helper(self)
        


class LecturerChangeForm(UserChangeForm):
    class Meta:
        model = Lecturer
        fields = ('lecturer', 'street_address', 'locality', 'district', 'state',
                  'pincode', 'mobile_number','wallet', 'profile_pic')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lecturer'].widget.attrs.update(
            {'class': 'form-control', 'hidden': 'hidden'})
        helper(self)

# class StudentCreationForm(forms.BaseForm):
#     class Meta:
#         model = Student
#         fields = ('student', 'street_address', 'locality', 'district', 'state',
#                   'pincode', 'mobile_number', 'profile_pic')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['student'].widget.attrs.update(
#             {'class': 'form-control'})
#         helper(self)
        


# class LecturerCreationForm(forms.BaseForm):
#     class Meta:
#         model = Lecturer
#         fields = ('lecturer', 'street_address', 'locality', 'district', 'state',
#                   'pincode', 'mobile_number', 'profile_pic')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['lecturer'].widget.attrs.update(
#             {'class': 'form-control'})
#         helper(self)