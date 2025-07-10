from django.urls import path
from nav.views import home;
from nav.views import id_show;
from nav.views import test_other;

urlpatterns = [
    path("home/",home),
    path("home/<id>",id_show),
    path("other/",test_other)
]
