from django.urls import path
import project.views.artists as artists

from project.constant import ROOT
app_name = "artists"

urlpatterns = [
    path(ROOT, artists.index, name="index"),
    path("<int:id>/", artists.view, name="view"),
]