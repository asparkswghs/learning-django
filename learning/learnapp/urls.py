from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('student_form/', views.student_form, name='student_form'),
    path('teacher_form/', views.teacher_form, name='teacher_form'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]