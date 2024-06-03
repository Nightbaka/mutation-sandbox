from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import receive_user_data

from users import views


urlpatterns = [
    path('', receive_user_data, name="auth-endpoint"),
]