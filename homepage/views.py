from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

# from django.http import HttpResponse
#
# def home(request):
#     return HttpResponse('home')
