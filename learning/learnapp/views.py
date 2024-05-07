from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Student, Teacher
from .forms import StudentForm, TeacherForm, RegistrationForm

# Create your views here.

def root(request):
    context = {

    }
    return render(request, 'root.html', context)

def students(request):
    if not request.user.is_authenticated:
        return redirect(auth_login)
    else:
        context = {
            'students': Student.objects.all(), # Pass all student objects
        }
        return render(request, 'students.html', context)
    

def teachers(request):
    if not request.user.is_authenticated:
        return redirect(auth_login)
    else:
        context = {
            'teachers': Teacher.objects.all(), # Pass all teacher objects
        }
        return render(request, 'teachers.html', context)

def student_form(request):
    context = {

    }
    if not request.user.is_authenticated:
        return redirect(auth_login)
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

        # Confirmation Message
        messages.success(request, 'New Student Added Successfully!')

        form = StudentForm() # Reset form for new submission

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
    if not request.user.is_authenticated:
        return redirect(auth_login)
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

        # Confirmation Message
        messages.success(request, 'New Teacher Added Successfully!')

        form = TeacherForm() # Reset form for new submission

    else: # Load blank form if not a form submission
        form = TeacherForm()
    
    context['method'] = request.method
    context['form'] = form

    return render(
        request,
        'teacher_form.html',
        context,
        )

def auth_login(request):
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        try:
            user = authenticate(request.POST)
            login(request, user)
            return redirect('/')
        except:
            return render(request, 'auth/login.html', {'form': form})

    return render(request, 'auth/login.html', context)

def auth_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('')
        else:
            print('Registration: FORM IS INVALID.')
            return render(request, 'auth/register.html', {'form': RegistrationForm()})

    return render(request, 'auth/register.html', {'form': RegistrationForm()})