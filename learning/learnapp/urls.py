from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('student_form/', views.student_form, name='student_form')
]