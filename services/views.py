from django.shortcuts import render
from .models import Services, Testamonials

# Create your views here.


def services(request):
    """
    A view to show the services which the site provides.
    """
    services = Services.objects.all()
    testamonials = Testamonials.objects.all()

    context = {
        'services': services,
        'testamonials': testamonials,
    }
    
    return render(request, 'services/services.html', context)


