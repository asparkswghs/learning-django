from django.shortcuts import render
from .models import Student, Teacher
from .forms import StudentForm, TeacherForm

# Create your views here.

def root(request):
    context = {

    }
    return render(request, 'root.html', context)

def students(request):
    context = {
        'students': Student.objects.all(), # Pass all student objects
    }
    return render(request, 'students.html', context)

def teachers(request):
    context = {
        'teachers': Teacher.objects.all(), # Pass all teacher objects
    }
    return render(request, 'teachers.html', context)

def student_form(request):
    context = {

    }
    if request.method == 'POST': # For button click
        form = StudentForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print(f"{name}: ({type(value)}, {value})")
        # Save data locally, but not to DB yet
        requests = form.save(commit=False)

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        middle_name = form.cleaned_data['middle_name']
        grade = form.cleaned_data['grade']
        requests.save()
    else: # Load blank form if not a form submission
        form = StudentForm()
    
    context['method'] = request.method
    context['form'] = form

    return render(
        request,
        'student_form.html',
        context,
        )

def teacher_form(request):
    context = {

    }
    if request.method == 'POST': # For button click
        form = TeacherForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print(f"{name}: ({type(value)}, {value})")
        # Save data locally, but not to DB yet
        requests = form.save(commit=False)

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        title = form.cleaned_data['title']
        department = form.cleaned_data['department']
        requests.save()
    else: # Load blank form if not a form submission
        form = TeacherForm()
    
    context['method'] = request.method
    context['form'] = form

    return render(
        request,
        'teacher_form.html',
        context,
        )