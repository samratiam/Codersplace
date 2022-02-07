from django.shortcuts import get_object_or_404, render
from .models import Coder

# Create your views here.
def coders(request):
    coders = Coder.objects.order_by('-created_date')
    data = {
        'coders': coders,
    }
    
    return render(request, 'coders/coders.html',data)

def coders_detail(request, id):
    coder = get_object_or_404(Coder, pk=id)
    data = {
        'coder': coder
    }
    return render(request, 'coders/coder_detail.html', data)
