from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from styles.models import ShopStyles


def bag_contents(request):
    """
    Context Proccessor
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        style = get_object_or_404(ShopStyles, pk=item_id)
        total += quantity * style.style_price
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'style': style,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context