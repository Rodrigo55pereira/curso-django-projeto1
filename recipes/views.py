from django.shortcuts import render

from utils.recipes.factory import make_recipe

# renderização de templates #retorna um response

# Create your views here.


# HTTP REQUEST
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })
    # return HTTP Response


# HTTP REQUEST
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    })
    # return HTTP Response
