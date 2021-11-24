

def bag_contents(request):
    """
    Context Proccessor
    """
    bag_items = []
    total = 0 
    products_count = 0

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'products_count': products_count,
        'grand_total': grand_total,
    }

    return context