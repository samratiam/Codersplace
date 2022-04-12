from dataclasses import field
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout
# from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
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
            if user.account_type == 'Job':
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


@login_required(login_url='login')
def coder_dashboard(request):
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
def company_dashboard(request):
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
    return render(request, 'accounts/company/company-dashboard.html', data)


def cosine_similarity():
    fields_filter = Job.objects.values('id', 'name', 'city', 'level_type',
                                       'job_type', 'developer_type')
    coders_list = list(fields_filter)
    print("----------------------------")
    for coder_new in coders_list:
        coder_skillset = []
        pk = coder_new['id']
        coder = Job.objects.get(id=pk)
        coder_skills = coder.skills.all()
        for skill in coder_skills:
            coder_skillset.append(skill.name)
        coder_new['skills'] = coder_skillset
        # print("New coder skillsets:", coder_new['skills'])

    print("----------------------------")
    print("Final coder list:", coders_list)
    print("----------------------------")
