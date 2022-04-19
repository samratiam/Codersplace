from django.shortcuts import render, redirect
from .models import  Contact
from coders.models import Coder
from django.contrib import messages
# Create your views here.
def home(request):
    
    featured_coders = Coder.objects.order_by('-created_date').filter(is_featured=True)

    data = {

        'featured_coders': featured_coders,
    }
    return render(request, 'webpages/home.html',data)



def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']
        
        #TODO: do all sanitization
        contact = Contact(full_name=full_name, phone=phone, 
                                email=email, company_name=company_name, subject=subject,message=message
                            )
        contact.save()
        messages.success(request, 'Thanks for contacting us!')
        return redirect('contact')
    
    return render(request, 'webpages/contact.html')




