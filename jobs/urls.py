from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.jobs, name="jobs"),
    path('<int:id>/', views.job_detail, name="job_detail"),
    path('search/', views.jobs_search, name="jobs_search"),
]
