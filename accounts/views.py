from dataclasses import field
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout
# from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from jobs.forms import JobForm
from coders.models import Coder
from coders.forms import CoderForm
from jobs.models import Job

# Create your views here.
from django.contrib.auth import get_user_model

User = get_user_model()


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(
            username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.warning(request, 'You are logged in')
            if user.account_type == 'Coder':
                return redirect('coder_dashboard')
            elif user.account_type == 'Company':
                return redirect('company_dashboard')
            else:
                return redirect('coder_dashboard')

        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        account_type = request.POST['account_type']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=firstname, last_name=lastname, username=username,
                        email=email, password=password, account_type=account_type
                    )
                    user.save()
                    messages.success(
                        request, 'Account registered successfully')
                    return redirect('login')
        else:
            messages.warning(request, 'Password donot match')
            return redirect('register')

    return render(request, 'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect('home')

#Cosine similarity algorithm
import re
def cosine_similarity(coder_skills,jobs_skills):
    # coder_skills = [a for a in re.split(r'(\s|\,)', coder_skills.strip()) if a]
    jobs_skills = list(jobs_skills)
    coder_skillset = coder_skills.split(',')
    print("List of coder skills:",coder_skillset)
    print("List of jobs skills:",jobs_skills)
    
    #Convert each job skills into list of skills by splitting by commas
    jobs_skillset = []
    for jobskill in jobs_skills:
        each_jobskill = jobskill.split(',')
        jobs_skillset.append(each_jobskill)
    print("Split job skillls:",jobs_skillset)
    
    #Create a single list of all the jobs skills
    job_skills_single_list = []
    # Iterate through the outer list
    for element in jobs_skillset:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                job_skills_single_list.append(item)
        else:
            job_skills_single_list.append(element)
    print("Single job skills list:",job_skills_single_list)
    
    unique_job_skills = []
    for jobskill in job_skills_single_list:
        if jobskill not in unique_job_skills:
            unique_job_skills.append(jobskill)
    print("Distinct list of job skills:",unique_job_skills)        
    
    #Create a unique list of skills including coder and jobs skills
    # coder_job_skills = []
    # for jobskill in job_skills_single_list:
    #     for coder_skill in coder_skillset:
    #         if coder_skill not in coder_job_skills:
    #             coder_job_skills.append(coder_skill)
    
    # job_skills_single_list = [item for sublist in jobs_skillset for item in sublist]
    # print("Flat list:",single_skills_list)
    
    # import numpy as np

    # list_of_skills = []
    # for coder in df:
    #     print("Each coder skill:",each_skillset)
    #     skills_token = []
    #     for i in range(len(coder_skills)):
    #         count = 0
    #         if coder_skills[i] not in each_skillset:
    #             count = 0
    #         else :
    #             count +=1
    #             skills_token.append(count)
        
    # print("Coders Token:",skills_token)
    # list_of_skills.append(skills_token)
    # print("Skills List: ",list_of_skills)
    
    # jobs_distinct_skills= []
    # for jobskill in jobs_skillset:
    #     for skill in jobskill:
    #         if skill not in jobs_skillset:
    #             jobs_distinct_skills.append(jobskill)
    # print("Distinct job skills list:",jobs_distinct_skills)


@login_required(login_url='login')
def coder_dashboard(request):
    user_id = request.user.id
    #Check if user portfolio already exists
    if Coder.objects.filter(user__id=user_id).exists():
        
        #Select that specific coder
        coder = Coder.objects.get(user__id=user_id)
        
        # print("Coder Dataset:",coder.skills)
        
        #Select skills of coder 
        coder_skills = coder.skills
        
        #Select all the skills of jobs in form of list
        jobs_skills = Job.objects.values_list('skills',flat=True)
        # job_skills = 
        
        #Pass coder skills and list of job skills
        cosine_similarity(coder_skills,jobs_skills)
        
        data = {
            'coder': coder,
        }
        return render(request, 'accounts/coder/coder-view.html', data)
    else:
        jobchoices = Job.job_type.field.choices
        levelchoices = Job.level_type.field.choices
        developerchoices = Job.developer_type.field.choices
        jobtypes = []
        leveltypes = []
        developertypes = []

        for j in jobchoices:
            jobtypes.append(j[0])

        for l in levelchoices:
            leveltypes.append(l[0])

        for d in developerchoices:
            developertypes.append(d[0])
        data = {'developertypes': developertypes, 'jobtypes': jobtypes,
                'leveltypes': leveltypes, }
        # cosine_similarity()

        return render(request, 'accounts/coder/coder-dashboard.html', data)


@login_required(login_url='login')
def coder_update(request):
    context = {}

    obj = get_object_or_404(Coder, user__id=request.user.id)

    form = CoderForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("coder_dashboard")

    context["form"] = form

    return render(request, "accounts/coder/coder-update.html", context)


@login_required(login_url='login')
def coder_delete(request):
    context = {}

    obj = get_object_or_404(Coder, user__id=request.user.id)

    if request.method == "POST":
        obj.delete()
        return redirect("coder_dashboard")

    return render(request, "accounts/coder/coder-delete.html", context)


@login_required(login_url='login')
def company_dashboard(request):
    user_id = request.user.id
    jobs = Job.objects.filter(user__id=user_id)
    data = {
        'jobs': jobs,
    }
    return render(request, 'accounts/company/job-list.html', data)

@login_required(login_url='login')
def job_create(request):
    jobchoices = Job.job_type.field.choices
    levelchoices = Job.level_type.field.choices
    developerchoices = Job.developer_type.field.choices
    jobtypes = []
    leveltypes = []
    developertypes = []

    for j in jobchoices:
        jobtypes.append(j[0])

    for l in levelchoices:
        leveltypes.append(l[0])

    for d in developerchoices:
        developertypes.append(d[0])
    data = {'developertypes': developertypes, 'jobtypes': jobtypes,
            'leveltypes': leveltypes}
    return render(request,'accounts/company/job-create.html',data)
    # else:
        

    #     return render(request, 'accounts/company/company-dashboard.html', data)
    
@login_required(login_url='login')
def job_delete(request,pk):

    job = get_object_or_404(Job, id=pk)
    context = {'job':job}

    if request.method == "POST":
        job.delete()
        return redirect("company_dashboard")

    return render(request, "accounts/company/job-delete.html", context)

@login_required(login_url='login')
def job_update(request,pk):
    context = {}

    obj = get_object_or_404(Job, id=pk)

    form = JobForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("company_dashboard")

    context["form"] = form

    return render(request, "accounts/company/job-update.html", context)



