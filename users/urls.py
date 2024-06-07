from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import receive_login_data
from .views import receive_registration_data

from users import views


urlpatterns = [
    path('login', receive_login_data, name="login-endpoint"),
    path('register', receive_registration_data, name="registration-endpoint"),
]