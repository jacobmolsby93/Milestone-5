from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """
    A view to show the contents of the shopping bag
    """

    template_name = 'bag/bag.html'
    context = {}

    return render(request, template_name, context)


def add_to_bag(request, item_id):

    checked = request.POST.get('add_to')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] = None
    else:
        bag[item_id] += checked
    
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)