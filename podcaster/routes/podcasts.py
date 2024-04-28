from django.urls import path
import podcaster.views.podcasts as podcasts

from podcaster.constant import ROOT
app_name = "podcasts"

urlpatterns = [
    path(ROOT, podcasts.index, name="index"),    
    path("<int:id>/", podcasts.view, name="view"),
    path("create/", podcasts.create, name="create"),
]
