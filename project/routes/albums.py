from django.urls import path
import project.views.albums as albums

from project.constant import ROOT
app_name = "albums"

urlpatterns = [
    path(ROOT, albums.index, name="index"),    
    path("<int:id>/", albums.view, name="view"),
]