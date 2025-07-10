from django.urls import path
from nav.views import home;
from nav.views import id_show;

urlpatterns = [
    path("home/",home),
    path("home/<id>",id_show)
]
