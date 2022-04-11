from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.coders, name="coders"),
    path("coder-form/", views.coders_form, name="coders_form"),
    path('<int:id>/', views.coders_detail, name="coders_detail"),
    path('search/', views.search, name="search"),
]
