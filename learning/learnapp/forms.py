from socket import fromshare
from django import forms
from .models import Student, Teacher

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