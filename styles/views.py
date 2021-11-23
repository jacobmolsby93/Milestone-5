from django.shortcuts import render, get_object_or_404
from .models import ShopStyles

# Create your views here.

def shop_styles(request):
    """
    A view to show the different styles which the owner has created
    """
    styles = ShopStyles.objects.all()

    context = {
        'styles': styles,
    }

    return render(request, 'styles/styles.html', context)


def style_detail(request, style_id):
    """
    A view to show a detail view of the product
    """
    style = get_object_or_404(ShopStyles, pk=style_id)

    context = {
        'style': style,
    }

    return render(request, 'styles/style_detail.html', context)
