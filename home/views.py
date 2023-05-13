from django.shortcuts import render


def index(request):
    """ A view to return the indext page """
    return render(request, 'home/index.html')