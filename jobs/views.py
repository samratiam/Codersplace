from django.shortcuts import get_object_or_404, redirect, render
from .models import Job

# Create your views here.


def jobs(request):
    jobs = Job.objects.order_by('-created_date')
    # returns distinct array with field 'developer_type' from model
    developer_type_search = Job.objects.values_list(
        'developer_type', flat=True).distinct()
    level_type_search = Job.objects.values_list(
        'level_type', flat=True).distinct()
    job_type_search = Job.objects.values_list(
        'job_type', flat=True).distinct()

    data = {
        'jobs': jobs,
        'developer_type_search': developer_type_search,
        'level_type_search': level_type_search,
        'job_type_search': job_type_search,

    }

    return render(request, 'jobs/jobs.html', data)


# def job_form(request):
#     pass


def job_detail(request, id):
    job = get_object_or_404(Job, pk=id)
    # skill = get_object_or_404(Skill)
    data = {
        'job': job,
        # 'skill': skill
    }
    return render(request, 'jobs/job_detail.html', data)


# def search(request):
#     pass
