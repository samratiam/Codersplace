from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.coders,name="coders")
]

