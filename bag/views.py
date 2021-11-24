from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """
    A view to show the contents of the shopping bag
    """

    template_name = 'bag/bag.html'
    context = {}

    return render(request, template_name, context)