from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('css/', views.css, name='css'),  
    path('js/', views.js, name='js'),  
    path('image/', views.image, name='image'),  
]
