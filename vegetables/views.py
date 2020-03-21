from django.shortcuts import render
from .models import Vegetables


def vege(request):
    vegetables = Vegetables.objects.all()
    return render(request, 'vege.html', {'vegetables': vegetables})



