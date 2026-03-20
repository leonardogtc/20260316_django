from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name':'Leonardo Tavares'
    })


def contato(request):
    return render(request, 'recipes/contato.html')


def sobre(request):
    return HttpResponse('Sobre')
