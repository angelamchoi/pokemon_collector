from django.shortcuts import render
from django.views.generic.edit import CreateView #create view
from .models import Pokemon #import Pokemon Data

# View functions
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
   pokemon = Pokemon.objects.all() #query
   return render(request, 'pokemon/index.html', {'pokemons': pokemon})

def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return render(request, 'pokemon/detail.html', {'pokemon': pokemon})

# PokemonCBV
class PokemonCreate(CreateView):
    model = Pokemon
    fields ='__all__'
    success='/pokemon/'