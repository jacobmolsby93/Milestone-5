from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import ShopStyles
from services.models import Services
from .forms import StyleForm

# Create your views here.

def shop_styles(request):
    """
    A view to show the different styles which the owner has created
    """
    styles = ShopStyles.objects.all()
    number_of_styles = styles.count()
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
        'number_of_styles': number_of_styles
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


def add_style(request):
    """
    A view to Add styles to the page
    """

    if request.method == 'POST':
        form = StyleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_style'))
        else:
            messages.error(request, 'Failed to add product, Please ensure the form is valid.')
    else:
        form = StyleForm()
    template = "styles/add_style.html"
    context = {
        'form': form,
    }

    return render(request, template, context)