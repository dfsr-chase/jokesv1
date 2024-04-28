from django.urls import path
import project.views.app as app

from project.constant import ROOT
app_name = "app"

urlpatterns = [
    path(ROOT, app.index, name="index"),
    path('login/', app.login, name='login'),
    path('register/', app.register, name='register'),
    path('search/', app.search, name='search'),
    path('membership/', app.membership, name='membership'),
]