from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Images, Contact
from .forms import ContactForm
# Create your views here.


def Home(request):
    """
    A view for the home page, and portfolio.
    """
    images = Images.objects.all()

    template_name = 'home/home.html'
    context = {
        "images": images,

    }
    return render(request, template_name, context)


def AboutMeView(request):
    """
    A view for the about me page
    """
    template_name = 'about/about.html'
    context = {}

    return render(request, template_name, context)


def ContactView(request):
    """
    A view for the contact me page/contact form
    """
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Enquiry"
            body = {
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email'],
                'phone_number': form.cleaned_data['phone_number'],
                'subject': form.cleaned_data['subject'],
                'message_box': form.cleaned_data['message_box']
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home")
    template_name = 'contact/contact.html'
    context = {
        'contact_form': form
    }
    
    return render(request, template_name, context)
