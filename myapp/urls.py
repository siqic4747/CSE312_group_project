from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('forgot-password-request/', views.forgot_password_request, name='forgot_password_request'),
    path('register-form/', views.register_form, name= 'register_form'),
]
