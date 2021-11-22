from django.shortcuts import render
from .models import Services

# Create your views here.

def services(request):
    """
    A view to show the services which the site provides.
    """
    services = Services.objects.all()

    context = {
        'services': services,
    }
    
    return render(request, 'services/services.html', context)