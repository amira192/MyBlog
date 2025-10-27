from django.urls import path
from .views import UserRegistrationView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
