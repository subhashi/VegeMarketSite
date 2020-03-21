from django.shortcuts import render
from .models import Fruit


def fruit (request):
    fruits = Fruit.objects.all()
    return render(request, 'fruit.html', {'fruits': fruits})

