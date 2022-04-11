from django.shortcuts import get_object_or_404, redirect, render
from .models import Coder

# Create your views here.


# def hirecoder(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         coder_id = request.POST['coder_id']
#         coder_name = request.POST['coder_name']
#         city = request.POST['city']
#         coder_developer_type = request.POST['coder_developer_type']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         message = request.POST['message']
#         user_id = request.POST['user_id']

#         hirecoder = Hirecoder(first_name=first_name, last_name=last_name,
#                               coder_id=coder_id, coder_name=coder_name, city=city, phone=phone,
#                               coder_developer_type=coder_developer_type,
#                               email=email, message=message, user_id=user_id
#                               )
#         hirecoder.save()
#         messages.success(request, 'Thanks for reaching out!')
#         return redirect('coders')


def coders(request):
    coders = Coder.objects.order_by('-created_date')
    # returns distinct array with field 'developer_type' from model
    developer_type_search = Coder.objects.values_list(
        'developer_type', flat=True).distinct()
    level_type_search = Coder.objects.values_list(
        'level_type', flat=True).distinct()
    job_type_search = Coder.objects.values_list(
        'job_type', flat=True).distinct()

    data = {
        'coders': coders,
        'developer_type_search': developer_type_search,
        'level_type_search': level_type_search,
        'job_type_search': job_type_search,

    }

    return render(request, 'coders/coders.html', data)


def coders_form(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        # last_name = request.POST['last_name']
        city = request.POST['city']
        developer_type = request.POST['developertype']
        job_type = request.POST['jobtype']
        level_type = request.POST['leveltype']
        email = request.POST['email']
        skills = request.POST['skills']
        description = request.POST['description']
        photo = request.FILES['photo']

        coder = Coder(name=fullname,
                      city=city, level_type=level_type,
                      developer_type=developer_type, job_type=job_type,
                      email=email, description=description, skills=skills, photo=photo
                      )
        coder.save()
        return redirect('coders')


def coders_detail(request, id):
    coder = get_object_or_404(Coder, pk=id)
    # skill = get_object_or_404(Skill)
    data = {
        'coder': coder,
        # 'skill': skill
    }
    return render(request, 'coders/coder_detail.html', data)


def search(request):
    coders = Coder.objects.order_by('-created_date')
    # returns distinct array with field 'developer_type' from model
    developer_type_search = Coder.objects.values_list(
        'developer_type', flat=True).distinct()
    level_type_search = Coder.objects.values_list(
        'level_type', flat=True).distinct()
    job_type_search = Coder.objects.values_list(
        'job_type', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            coders = coders.filter(description__icontains=keyword)

    if 'developer_type' in request.GET:
        developer_type = request.GET['developer_type']
        if developer_type:
            coders = coders.filter(
                developer_type__iexact=developer_type)  # exact match

    if 'level_type' in request.GET:
        level_type = request.GET['level_type']
        if level_type:
            coders = coders.filter(
                level_type__iexact=level_type)  # exact match

    if 'job_type' in request.GET:
        job_type = request.GET['job_type']
        if job_type:
            coders = coders.filter(job_type__iexact=job_type)  # exact match

    data = {
        'coders': coders,
        'developer_type_search': developer_type_search,
        'level_type_search': level_type_search,
        'job_type_search': job_type_search,
    }
    return render(request, 'coders/search.html', data)
