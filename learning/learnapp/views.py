from django.shortcuts import render

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

    }
    return render(request, 'students.html', context)