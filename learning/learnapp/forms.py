from socket import fromshare
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Teacher, UserProfilePicture

# Forms
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'grade',
        ]

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'title',
            'department',
        ]

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfilePicture
        fields = [
            'picture',
            'alt',
        ]
        exclude = [
            'user',
        ]