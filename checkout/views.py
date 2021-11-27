from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from styles.models import ShopStyles

# Create your views here.

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('styles'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jsk3ILrAfHBjS2NwxGgt683TQOhBU2PufQaa6Up1IWMiQV2el8KvF1eHirHvZmdIQ3SK1dTcSTsKYHGHTXR7QO500BzEhylXa',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)