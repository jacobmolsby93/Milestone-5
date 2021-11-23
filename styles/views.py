from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import ShopStyles
from services.models import Services

# Create your views here.

def shop_styles(request):
    """
    A view to show the different styles which the owner has created
    """
    services = Services.objects.all()
    styles = ShopStyles.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter anything in the search!")
                return redirect(reverse('products'))
            
            queries_styles = Q(style_name__icontains=query) | Q(style_description__icontains=query)
            styles = styles.filter(queries_styles)

    context = {
        'styles': styles,
        'search_term': query,
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
