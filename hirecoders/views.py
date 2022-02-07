from django.shortcuts import redirect, render
from django.contrib import messages

from .models import Hirecoder

# Create your views here.
def hirecoder(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        coder_id = request.POST['coder_id']
        coder_name = request.POST['coder_name']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']

        hirecoder = Hirecoder(first_name=first_name, last_name=last_name, 
                                coder_id=coder_id, coder_name=coder_name, city=city,phone=phone,
                                email=email, message=message, user_id=user_id
                            )
        hirecoder.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('coders')
