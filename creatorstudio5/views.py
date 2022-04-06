from django.shortcuts import render


def page_not_found_view(request, exception):
    """
    View to handle 404 page.
    """
    return render(request, '404.html', status=404)