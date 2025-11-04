from django.shortcuts import render

from .models import Cheese


def cheese_list(request):
    cheeses = Cheese.objects.all()

    context = {
        'cheeses': cheeses,
    }

    return render(request, 'cheese_counter/cheese_list.html', context)

def cheese_detail(request, slug):
    cheese = Cheese.objects.get(slug=slug)

    context = {
        'cheese': cheese,
    }

    return render(request, 'cheese_counter/cheese_detail.html', context)
