from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)
from django.contrib import messages
from styles.models import ShopStyles

# Create your views here.

def view_bag(request):
    """
    A view to show the contents of the shopping bag
    """

    template_name = 'bag/bag.html'
    context = {}

    return render(request, template_name, context)


def add_to_bag(request, item_id):
    """
    Add item of specified product to the shopping bag
    """
    style = ShopStyles.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        messages.error(request, 'You have already added this product to the shopping bag!')
    else:
        bag[item_id] = quantity
        messages.success(request, f"You added {style.style_name} to your bag!")
    
    request.session['bag'] = bag

    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """
    Remove the item from the shopping bag
    """
    style = get_object_or_404(ShopStyles, pk=item_id)    
    bag = request.session.get('bag', {})
    try:
        bag.pop(item_id)
        messages.success(request, f'Removed {style.style_name} from your bag')
            
        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)