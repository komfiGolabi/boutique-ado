from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view that renders bag content page """

    return render(request, 'bag/bag.html')

# Create your views here.
