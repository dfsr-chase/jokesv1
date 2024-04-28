from django.urls import path
import project.views.playlists as playlists

from project.constant import ROOT
app_name = "playlists"

urlpatterns = [
    path(ROOT, playlists.index, name="index"),    
    path("create/", playlists.create, name="create"),
    path("<int:id>/", playlists.view, name="view"),
]
