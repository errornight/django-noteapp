from django.shortcuts import render, redirect
from .forms import UserSignup, UserLogin, EditProfile, SendTicket
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from apps.notes.models import Note
from .utils import Firebase

# Firebase
firebase = Firebase()

def signup_user(request):
    form = UserSignup()

    if request.method == 'POST':
        form = UserSignup(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES.get('profile', False):
                image_url = firebase.profile_method(request)
                form.instance.profile = image_url

            form.save()
            login(request, form.instance)
            return redirect('DashboardPage')
    context = {'form': form}
    return render(request, 'users/signup.html', context)

def login_user(request):
    form = UserLogin()
    message = None
    if request.method == 'POST':
        form = UserLogin(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)

                return redirect('NotesPage')
        else:
            message = 'Form is not valid!'


    context = {'form': form, 'message': message}
    return render(request, 'users/login.html', context)

@login_required
def dashboard(request):
    context = {'user': request.user, 'notes': Note.objects.filter(owner=request.user)}
    return render(request, 'users/dashboard.html', context)

@login_required()
def edit_profile(request):
    form = EditProfile(instance=request.user)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            if request.FILES.get('profile', False):
                image_url = firebase.profile_method(request)
                form.instance.profile = image_url

            form.save()
            return redirect('DashboardPage')

    context = {'form': form}
    return render(request, 'users/editprofile.html', context)

@login_required()
def log_out(request):
    past_page = request.META.get("HTTP_REFERER") or '/'
    message = f'Logout from "{request.user}"'
    if request.method == 'GET':
        if request.GET.get('confirm'):
            logout(request)
            return redirect('HomePage')

    context = {'past_page': past_page, 'message': message}
    return render(request, 'confirmation.html', context)

def about_us(request):
    form = SendTicket()
    message = None
    if request.method == 'POST':
        form = SendTicket(request.POST)
        if form.is_valid():
            form.save()

            form = SendTicket()
            message = 'Ticket send successfully.'
            context = {'form': form, 'message': message}
            return render(request, 'users/about-us.html', context)


    context = {'form': form, 'message': message}
    return render(request, 'users/about-us.html', context)