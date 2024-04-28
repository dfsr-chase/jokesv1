from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    return render(request, "podcaster/pages/home.html")

def login(request) -> HttpResponse:
    return render(request, "podcaster/pages/auth/login.html")

def register(request) -> HttpResponse:
    return render(request, "podcaster/pages/auth/register.html")

def search(request) -> HttpResponse:
    return render(request, "podcaster/pages/search.html")