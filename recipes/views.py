from django.shortcuts import render

# renderização de templates #retorna um response

# Create your views here.


# HTTP REQUEST
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Rodrigo Pereira'
    })
    # return HTTP Response
