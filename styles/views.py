from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
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
            style = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('style_detail', args=[style.id]))
        else:
            messages.error(request, 'Failed to add product, Please ensure the form is valid.')
    else:
        form = StyleForm()
    template = "styles/add_style.html"
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_style(request, style_id):
    """
    A view to edit styles to the page
    """
    style = get_object_or_404(ShopStyles, id=style_id)
    if request.method == 'POST':
        form = StyleForm(request.POST, request.FILES, instance=style)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated style!')
            return redirect(reverse('style_detail', args=[style.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = StyleForm(instance=style)
        messages.info(request, f'You are editing {style.style_name}!')


    template = 'styles/edit_style.html'
    context = {
        'form': form,
        'style': style,
    }
    return render(request, template, context)


@login_required
def delete_style(request, style_id):
    """
    Delete a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    style = get_object_or_404(ShopStyles, pk=style_id)
    style.delete()
    messages.success(request, 'style deleted!')
    return redirect(reverse('styles'))