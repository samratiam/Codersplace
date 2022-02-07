from django.urls import path,include
from . import views

urlpatterns = [
    path("hirecoder/",views.hirecoder,name="hirecoder"),
]