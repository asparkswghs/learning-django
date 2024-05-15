from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Student, Teacher, UserProfilePicture
from .forms import StudentForm, TeacherForm, RegistrationForm, ProfilePictureForm

# Create your views here.

def root(request):
    context = {

    }
    return render(request, 'root.html', context)

@user_passes_test(lambda u: u.groups.filter(name="teachers"))
@login_required
def students(request):
    context = {
        'students': Student.objects.all(), # Pass all student objects
    }
    return render(request, 'students.html', context)
    

@login_required
def teachers(request):
    context = {
        'teachers': Teacher.objects.all(), # Pass all teacher objects
    }
    return render(request, 'teachers.html', context)

@login_required
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

@login_required
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

def login(request):
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        print(request.POST)
        try:
            user = authenticate(request.POST)
            login(request, user)
            return redirect('/profile/')
        except:
            return render(request, 'registration/login.html', {'form': AuthenticationForm()})

    return render(request, 'registration/login.html', {'form': AuthenticationForm()})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/profile/')
        else:
            print('Registration: FORM IS INVALID.')
            return render(request, 'registration/register.html', {'form': RegistrationForm()})

    return render(request, 'registration/register.html', {'form': RegistrationForm()})

@login_required
def profile(request):
    try:
        profile_picture = UserProfilePicture.objects.filter(user=request.user)[0]
    except IndexError:
        profile_picture = UserProfilePicture(user=request.user)
    context = {
        'student_accounts': Student.objects.filter(last_name=request.user.last_name, first_name=request.user.first_name),
        'teacher_accounts': Teacher.objects.filter(last_name=request.user.last_name, first_name=request.user.first_name),
        'profile_picture': profile_picture,
        'profile_picture_form': ProfilePictureForm()
    }
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST)
        if form.is_valid():
            submitted = form.save(commit=False)
            profile_picture.picture = submitted.picture
            profile_picture.alt = submitted.alt
            profile_picture.save()
            return redirect('/profile/')
    return render(request, 'profile.html', context)