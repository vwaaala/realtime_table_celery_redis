from django.shortcuts import render

from .models import Coin


def index(request):
    context = {
        'coins': Coin.objects.all()
    }
    return render(request, 'index.html', context)
