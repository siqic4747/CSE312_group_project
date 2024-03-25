from django.urls import path
from django.urls import include
from . import views
from .views import register
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .forms import CustomLoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('register-form/', views.register_form, name= 'register_form'),
    path('login/', LoginView.as_view(template_name='login.html', authentication_form=CustomLoginForm), name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]
