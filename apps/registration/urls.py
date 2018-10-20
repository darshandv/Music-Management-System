from django.conf.urls import url
from django.urls import re_path, include
from . import views


urlpatterns = [
    re_path(r'^', include('allauth.urls' )),

]
