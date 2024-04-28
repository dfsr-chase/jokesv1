from django.urls import path
import project.views.podcasts as podcasts

from project.constant import ROOT
app_name = "podcasts"

urlpatterns = [
    path(ROOT, podcasts.index, name="index"),    
    path("<int:id>/", podcasts.view, name="view"),
]
