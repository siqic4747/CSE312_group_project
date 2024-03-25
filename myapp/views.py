from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
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
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return redirect('index') 
        else:
            return render(request, 'register.html', {'form': form}) 
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})  

def forgot_password_request(request):
    # Your forgot password request view logic here
    return render(request, 'forgot-password.html')

@login_required
def profile(request):
    return render(request, 'profile.html')