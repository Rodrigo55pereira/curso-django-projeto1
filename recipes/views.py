from django.http import HttpResponse
from django.shortcuts import render  # renderização de templates

# Create your views here.


# HTTP REQUEST
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Rodrigo Pereira'
    })
    # return HTTP Response


def contato(request):
    return HttpResponse('contato')
    # return HTTP Response


def sobre(request):
    return HttpResponse('sobre')
    # return HTTP Response
