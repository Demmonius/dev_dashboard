from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout, login

from .views import SignUp, SignIn

urlpatterns = [
    path('signup', SignUp.as_view(), name="signup"),
    path('signin', SignIn.as_view(), name='signin'),
]
