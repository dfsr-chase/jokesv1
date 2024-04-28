from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    return render(request, "podcaster/pages/podcasts/index.html")

def view(request, id) -> HttpResponse:
    return render(request, "podcaster/pages/podcasts/view.html")

def create(request) -> HttpResponse:
    return render(request, "podcaster/pages/podcasts/create.html")