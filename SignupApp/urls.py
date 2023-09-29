from django.contrib import admin
from django.urls import path
from SignupApp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.loginUser, name="loginUser"),
    path("logout", views.logoutUser, name="logoutUser"),
    path("signup", views.signupUser, name="signupUser"),
]
