from django.contrib import admin
from django.urls import path, include

app_name = "podcaster"

urlpatterns = [
    path("", include("podcaster.routes.app")),
    path("podcasts/", include("podcaster.routes.podcasts")),
]