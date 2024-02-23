from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is the index page.")

def home(request):
    return render(request, 'index.html')

def css(request):
    return HttpResponse("CSS content", content_type="text/css")

def js(request):
    return HttpResponse("JavaScript content", content_type="application/javascript")

def image(request):
    return HttpResponse("This would be an image response.", content_type="image/png")

