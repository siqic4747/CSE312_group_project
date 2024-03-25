from django.urls import path
from django.urls import include
from . import views
from .views import register
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('forgot-password-request/', views.forgot_password_request, name='forgot_password_request'),
    path('register-form/', views.register_form, name= 'register_form'),
    path('login/', LoginView.as_view(template_name='index.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
