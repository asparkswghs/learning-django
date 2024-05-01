from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('student_form/', views.student_form, name='student_form'),
    path('teacher_form/', views.teacher_form, name='teacher_form'),
    path('auth/login/', views.auth_login, name='auth_login'),
    path('auth/register/', views.auth_register, name='auth_register')
]