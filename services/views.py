from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Services, ServiceRequestModel, Testamonials
from .forms import RequestForm

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


def service_request(request, service_id):
    """
    A view to show a detail view of the product
    """
    request_form = RequestForm()
    service = get_object_or_404(Services, id=service_id)
    if request.method == 'POST':
        request_form = RequestForm(request.POST)
        if request_form.is_valid():
            subject = "Design Idea"
            request_form = {
                'full_name': request_form.cleaned_data['full_name'],
                'email': request_form.cleaned_data['email'],
                'phone_number': request_form.cleaned_data['phone_number'],
                'ideas': request_form.cleaned_data['ideas']
            }
            message = "\n".join(request_form.values())
            request_form = RequestForm(request_form)
            

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("message_succes")

    context = {
        'service': service,
        'request_form': request_form,
    }

    return render(request, 'services/service_request.html', context)
    

def message_sent(request):

    template = 'services/message_sent_page.html'
    context = {}
    return render(request, template, context)
