from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.jobs, name="jobs"),
    path('<int:id>/', views.job_detail, name="job_detail"),
    # path("job-form/", views.job_form, name="job_form"),
    # path('search/', views.search, name="search"),
]
