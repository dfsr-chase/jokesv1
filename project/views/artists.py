from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    return render(request, "pages/artists/index.html")

def view(request, id) -> HttpResponse:
    return render(request, "pages/artists/view.html")