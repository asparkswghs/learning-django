from django.shortcuts import render
from .models import Student

# Create your views here.

def base(request):
    context = {

    }
    return render(request, 'base.html', context)

def root(request):
    context = {

    }
    return render(request, 'root.html', context)

def students(request):
    context = {
        'students': Student.objects.all(), # Pass all student objects
    }
    return render(request, 'students.html', context)