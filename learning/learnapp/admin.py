from re import U
from django.contrib import admin
from .models import Student, Teacher, UserProfilePicture

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(UserProfilePicture)