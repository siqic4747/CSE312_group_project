from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Your index view logic here
    return render(request, 'index.html')

def register(request):
    # Your register view logic here
    return render(request, 'register.html')

def register_form(request):
    #get the data from the POST request and redirect the user to the login page
    return

def forgot_password_request(request):
    # Your forgot password request view logic here
    return render(request, 'forgot-password.html')

