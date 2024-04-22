from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, CustomLoginForm
from django.contrib.auth.decorators import login_required



def index(request):
    # Your index view logic here
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index') 
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def register_form(request):
    print(request)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate user after registration
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                # Log user in
                login(request, user)
                # Redirect to the profile page or any other appropriate page
                return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # Log user in
                login(request, user)
                # Redirect to the profile page or any other appropriate page
                return redirect('index')
            else:
                # Authentication failed
                pass
    else:
        form = CustomLoginForm()
    return render(request, 'index.html', {'form': form})
def forgot_password_request(request):
    # Your forgot password request view logic here
    return render(request, 'forgot-password.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('login')
