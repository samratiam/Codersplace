from django.shortcuts import render
from .models import Coder

# Create your views here.
def coders(request):
    coders = Coder.objects.order_by('-created_date')
    data = {
        'coders': coders,
    }
    
    return render(request, 'coders/coders.html',data)
